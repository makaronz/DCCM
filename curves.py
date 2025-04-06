import numpy as np
import subprocess

def parse_lut_data(file_path):
    """
    Parses a .cube LUT file and returns the LUT size and data as a NumPy array.
    """
    try:
        # Get LUT size
        result = subprocess.run(['head', '-n', '1', file_path], capture_output=True, text=True, check=True)
        lut_size = int(result.stdout.strip().split()[-1])

        # Extract data lines
        result = subprocess.run(['tail', '-n', '+2', file_path], capture_output=True, text=True, check=True)
        data_lines = result.stdout.strip().split('\n')

        # Parse data into a 3D NumPy array
        lut_data = np.zeros((lut_size, lut_size, lut_size, 3), dtype=np.float64)
        index = 0
        for z in range(lut_size):
            for y in range(lut_size):
                for x in range(lut_size):
                    r, g, b = map(float, data_lines[index].split())
                    lut_data[x, y, z] = [r, g, b]
                    index += 1

        return lut_size, lut_data
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error parsing LUT file: {e}")
        return None, None

def trilinear_interpolation(r, g, b, lut_data, lut_size):
    """
    Performs trilinear interpolation on the given LUT data.
    """
    # Normalize input values to the range 0-(lut_size-1)
    x = r * (lut_size - 1)
    y = g * (lut_size - 1)
    z = b * (lut_size - 1)

    # Get the integer and fractional parts of the coordinates
    x0 = int(np.floor(x))
    y0 = int(np.floor(y))
    z0 = int(np.floor(z))
    x1 = int(np.ceil(x))
    y1 = int(np.ceil(y))
    z1 = int(np.ceil(z))

    xd = x - x0
    yd = y - y0
    zd = z - z0

    # Handle edge cases where input is exactly on a LUT boundary
    x1 = min(x1, lut_size - 1)
    y1 = min(y1, lut_size - 1)
    z1 = min(z1, lut_size - 1)
    
    # Perform trilinear interpolation
    c000 = lut_data[x0, y0, z0]
    c100 = lut_data[x1, y0, z0]
    c010 = lut_data[x0, y1, z0]
    c110 = lut_data[x1, y1, z0]
    c001 = lut_data[x0, y0, z1]
    c101 = lut_data[x1, y0, z1]
    c011 = lut_data[x0, y1, z1]
    c111 = lut_data[x1, y1, z1]

    c00 = c000 * (1 - xd) + c100 * xd
    c01 = c001 * (1 - xd) + c101 * xd
    c10 = c010 * (1 - xd) + c110 * xd
    c11 = c011 * (1 - xd) + c111 * xd

    c0 = c00 * (1 - yd) + c10 * yd
    c1 = c01 * (1 - yd) + c11 * yd

    c = c0 * (1 - zd) + c1 * zd

    return c

# --- Placeholder functions for LUT-based LogC4 conversion ---
def arri_logc4_to_linear_lut(log_value, lut_data, lut_size):
    """
    Converts an ARRI LogC4 encoded value to linear using the LUT and trilinear interpolation.
    """
    # Assume grayscale input and use it for all color channels
    r = g = b = log_value
    
    # Perform trilinear interpolation
    interpolated_rgb = trilinear_interpolation(r, g, b, lut_data, lut_size)
    
    # Return the average of the interpolated RGB values (simplification)
    return np.mean(interpolated_rgb)

def linear_to_arri_logc4_lut(linear_value, lut_data, lut_size):
    """
    Converts a linear value to ARRI LogC4 encoded value using a reverse lookup table (simplified).
    """
    # Create a reverse lookup table (LogC4 -> Linear)
    reverse_lookup = {}
    for log_value in np.linspace(0, 1, 1000):  # Sample 1000 LogC4 values
        linear = arri_logc4_to_linear_lut(log_value, lut_data, lut_size)
        reverse_lookup[linear] = log_value

    # Find the closest linear value in the lookup table
    closest_linear = min(reverse_lookup.keys(), key=lambda x: abs(x - linear_value))
    
    # Return the corresponding LogC4 value
    return reverse_lookup[closest_linear]

# --- Validation Tests ---
if __name__ == "__main__":
    # Load the LUT data
    lut_file = "ARRI_LogC4_v1_LUT_Package/LUTs/ARRI_LogC4-to-Gamma24_Rec709-D65_v1-65.cube"
    lut_size, lut_data = parse_lut_data(lut_file)

    if lut_data is not None:
        # Define test values (linear light values)
        test_values = np.array([0.01, 0.1, 0.5, 1.0, 10.0])

        # Test LogC4 to Linear
        print("Testing LogC4 to Linear:")
        for linear_value in test_values:
            log_value = linear_to_arri_logc4_lut(linear_value, lut_data, lut_size)
            recovered_linear = arri_logc4_to_linear_lut(log_value, lut_data, lut_size)
            print(f"  Linear: {linear_value:.4f}, LogC4: {log_value:.6f}, Recovered: {recovered_linear:.6f}")

        # Test Linear to LogC4
        print("\nTesting Linear to LogC4:")
        for log_value in np.linspace(0, 1, 5):  # Test a few LogC4 values
            linear_value = arri_logc4_to_linear_lut(log_value, lut_data, lut_size)
            recovered_log = linear_to_arri_logc4_lut(linear_value, lut_data, lut_size)
            print(f"  LogC4: {log_value:.4f}, Linear: {linear_value:.6f}, Recovered: {recovered_log:.6f}")
    else:
        print("LUT data could not be loaded. Validation tests skipped.")
