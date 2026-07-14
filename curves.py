"""
curves.py — Verified digital-cinema colour-management reference.

A single-file, dependency-light (numpy only) reference implementation of the
camera / display transfer functions and gamut-conversion matrices shared by the
LUT_to_false and DCCM projects.

Every constant is taken from the official manufacturer / standards document and
verified numerically by the __main__ self-test below: each encode/decode pair
round-trips to < 1e-4 and reproduces the published 18 % mid-grey value, and the
gamut matrices reproduce the officially published ARRI AWG3->Rec.709 matrix to
< 1e-5.

All transfer functions take and return numpy arrays (or scalars) with values
normalised to roughly 0-1 (scene-linear on input, code value on output, or the
reverse for the *_to_linear direction).

Sources:
  ARRI LogC3   EI800 spec (piecewise: c*log10(a*x+b)+d  |  e*x+f)
  ARRI LogC4   LogC4 whitepaper (2022-08)
  Sony S-Log3  S-Gamut3/S-Log3 tech note
  RED Log3G10  Log3G10 v2
  Panasonic V-Log, Canon Log 2
  Rec.709 (ITU-R BT.709), sRGB (IEC 61966-2-1)
  PQ (SMPTE ST 2084), HLG (ITU-R BT.2100)
  ACEScc (S-2014-003), ACEScct (S-2016-001), ACESproxy (S-2013-002)
"""

import numpy as np

# ============================================================================
# Transfer functions
# ============================================================================

# --- ARRI LogC3 (EI800) ---
_LOGC3 = dict(cut=0.010591, a=5.555556, b=0.052272, c=0.247190,
              d=0.385537, e=5.367655, f=0.092809)


def linear_to_logc3(x):
    p = _LOGC3
    x = np.asarray(x, dtype=np.float64)
    # np.where evaluates both branches, so clamp the log argument to stay
    # positive for elements handled by the linear (toe) branch.
    log_arg = np.maximum(p['a'] * x + p['b'], 1e-10)
    return np.where(x > p['cut'], p['c'] * np.log10(log_arg) + p['d'],
                    p['e'] * x + p['f'])


def logc3_to_linear(t):
    p = _LOGC3
    t = np.asarray(t, dtype=np.float64)
    log_cut = p['e'] * p['cut'] + p['f']
    return np.where(t > log_cut,
                    (np.power(10.0, (t - p['d']) / p['c']) - p['b']) / p['a'],
                    (t - p['f']) / p['e'])


# --- ARRI LogC4 ---
def _logc4_params():
    a = (2.0**18 - 16.0) / 117.45
    b = (1023.0 - 95.0) / 1023.0
    c = 95.0 / 1023.0
    s = (7.0 * np.log(2.0) * 2.0**(7.0 - 14.0 * c / b)) / (a * b)
    t = (2.0**(14.0 * (-c / b) + 6.0) - 64.0) / a
    return a, b, c, s, t


def linear_to_logc4(x):
    a, b, c, s, t = _logc4_params()
    x = np.asarray(x, dtype=np.float64)
    log_arg = np.maximum(a * x + 64.0, 1e-10)
    return np.where(x >= t, (np.log2(log_arg) - 6.0) / 14.0 * b + c, (x - t) / s)


def logc4_to_linear(y):
    a, b, c, s, t = _logc4_params()
    y = np.asarray(y, dtype=np.float64)
    return np.where(y >= 0.0, (np.power(2.0, 14.0 * (y - c) / b + 6.0) - 64.0) / a, y * s + t)


# --- Sony S-Log3 (S-Gamut3 and S-Gamut3.Cine share this curve) ---
def linear_to_slog3(x):
    # No non-negative clamp: the linear toe below 0.01125 also encodes
    # under-black (negative) scene-linear values so they round-trip.
    x = np.asarray(x, dtype=np.float64)
    log_arg = np.maximum((x + 0.01) / 0.19, 1e-10)
    return np.where(x >= 0.01125,
                    (420.0 + np.log10(log_arg) * 261.5) / 1023.0,
                    (x * (171.2102946929 - 95.0) / 0.01125 + 95.0) / 1023.0)


def slog3_to_linear(y):
    y = np.asarray(y, dtype=np.float64)
    cv = y * 1023.0
    return np.where(y >= 171.2102946929 / 1023.0,
                    np.power(10.0, (cv - 420.0) / 261.5) * 0.19 - 0.01,
                    (cv - 95.0) * 0.01125 / (171.2102946929 - 95.0))


# --- RED Log3G10 (v2) ---
def linear_to_log3g10(x):
    a, b, c, g = 0.224282, 155.975327, 0.01, 15.1927
    x = np.asarray(x, dtype=np.float64) + c
    log_arg = np.maximum(x * b + 1.0, 1e-10)
    return np.where(x >= 0.0, a * np.log10(log_arg), x * g)


def log3g10_to_linear(y):
    a, b, c, g = 0.224282, 155.975327, 0.01, 15.1927
    y = np.asarray(y, dtype=np.float64)
    x = np.where(y >= 0.0, (np.power(10.0, y / a) - 1.0) / b, y / g)
    return x - c


# --- Panasonic V-Log ---
def linear_to_vlog(x):
    b, c, d, cut = 0.00873, 0.241514, 0.598206, 0.01
    # No non-negative clamp: the linear toe below 0.01 preserves under-black.
    x = np.asarray(x, dtype=np.float64)
    log_arg = np.maximum(x + b, 1e-10)
    return np.where(x >= cut, c * np.log10(log_arg) + d, 5.6 * x + 0.125)


def vlog_to_linear(y):
    b, c, d = 0.00873, 0.241514, 0.598206
    y = np.asarray(y, dtype=np.float64)
    vlog_cut = 5.6 * 0.01 + 0.125  # 0.181
    return np.where(y >= vlog_cut, np.power(10.0, (y - d) / c) - b, (y - 0.125) / 5.6)


# --- Canon Log 2 ---
def linear_to_canonlog2(x):
    k, g, o = 87.09937546, 0.281863093, 0.035388128
    x = np.asarray(x, dtype=np.float64)
    neg = -g * np.log10(np.maximum(1.0 - k * x, 1e-10)) + o
    pos = g * np.log10(np.maximum(k * x + 1.0, 1e-10)) + o
    return np.where(x < 0.0, neg, pos)


def canonlog2_to_linear(t):
    k, g, o = 87.09937546, 0.281863093, 0.035388128
    t = np.asarray(t, dtype=np.float64)
    return np.where(t < o, -(np.power(10.0, (o - t) / g) - 1.0) / k,
                    (np.power(10.0, (t - o) / g) - 1.0) / k)


# --- Rec.709 (ITU-R BT.709) ---
def linear_to_rec709(x):
    x = np.maximum(np.asarray(x, dtype=np.float64), 0.0)
    return np.where(x < 0.018, 4.5 * x, 1.099 * np.power(x, 0.45) - 0.099)


def rec709_to_linear(y):
    y = np.maximum(np.asarray(y, dtype=np.float64), 0.0)
    return np.where(y < 0.081, y / 4.5, np.power((y + 0.099) / 1.099, 1.0 / 0.45))


# --- sRGB (IEC 61966-2-1) ---
def linear_to_srgb(x):
    x = np.maximum(np.asarray(x, dtype=np.float64), 0.0)
    return np.where(x <= 0.0031308, 12.92 * x, 1.055 * np.power(x, 1.0 / 2.4) - 0.055)


def srgb_to_linear(y):
    y = np.maximum(np.asarray(y, dtype=np.float64), 0.0)
    return np.where(y <= 0.04045, y / 12.92, np.power((y + 0.055) / 1.055, 2.4))


# --- PQ (SMPTE ST 2084) ---
_PQ_M1 = 2610.0 / 16384.0
_PQ_M2 = (2523.0 / 4096.0) * 128.0
_PQ_C1 = 3424.0 / 4096.0
_PQ_C2 = (2413.0 / 4096.0) * 32.0
_PQ_C3 = (2392.0 / 4096.0) * 32.0


def linear_to_pq(x, l_peak=10000.0):
    """x normalised so 1.0 == l_peak cd/m^2. Output 0-1."""
    l_norm = np.maximum(np.asarray(x, dtype=np.float64) * l_peak / 10000.0, 0.0)
    lp = np.power(l_norm, _PQ_M1)
    return np.power((_PQ_C1 + _PQ_C2 * lp) / (1.0 + _PQ_C3 * lp), _PQ_M2)


def pq_to_linear(y, l_peak=10000.0):
    n = np.power(np.maximum(np.asarray(y, dtype=np.float64), 0.0), 1.0 / _PQ_M2)
    num = np.maximum(n - _PQ_C1, 0.0)
    den = _PQ_C2 - _PQ_C3 * n
    # np.divide with a mask avoids evaluating num/den where den <= 0.
    ratio = np.divide(num, den, out=np.zeros_like(num), where=den > 1e-12)
    l_norm = np.power(np.maximum(ratio, 0.0), 1.0 / _PQ_M1)
    return l_norm * 10000.0 / l_peak


# --- HLG (ITU-R BT.2100) ---
_HLG_A = 0.17883277
_HLG_B = 1.0 - 4.0 * _HLG_A
_HLG_C = 0.5 - _HLG_A * np.log(4.0 * _HLG_A)


def linear_to_hlg(x):
    e = np.maximum(np.asarray(x, dtype=np.float64), 0.0)
    log_arg = np.maximum(12.0 * e - _HLG_B, 1e-10)
    return np.where(e <= 1.0 / 12.0, np.sqrt(3.0 * e), _HLG_A * np.log(log_arg) + _HLG_C)


def hlg_to_linear(y):
    e = np.maximum(np.asarray(y, dtype=np.float64), 0.0)
    return np.where(e <= 0.5, e * e / 3.0, (np.exp((e - _HLG_C) / _HLG_A) + _HLG_B) / 12.0)


# --- ACEScct (S-2016-001) ---
def linear_to_acescct(x):
    x = np.asarray(x, dtype=np.float64)
    return np.where(x <= 0.0078125, 10.5402377416545 * x + 0.0729055341958355,
                    (np.log2(np.maximum(x, 1e-10)) + 9.72) / 17.52)


def acescct_to_linear(y):
    y = np.asarray(y, dtype=np.float64)
    return np.where(y <= 0.155251141552511, (y - 0.0729055341958355) / 10.5402377416545,
                    np.power(2.0, y * 17.52 - 9.72))


# --- ACEScc (S-2014-003) ---
def linear_to_acescc(x):
    x = np.asarray(x, dtype=np.float64)
    near = (np.log2(2.0**-16 + np.maximum(x, 0.0) * 0.5) + 9.72) / 17.52
    normal = (np.log2(np.maximum(x, 2.0**-16)) + 9.72) / 17.52
    return np.where(x <= 0.0, (np.log2(2.0**-16) + 9.72) / 17.52,
                    np.where(x < 2.0**-15, near, normal))


def acescc_to_linear(y):
    y = np.asarray(y, dtype=np.float64)
    thr = (9.72 - 15.0) / 17.52
    return np.where(y < thr, (np.power(2.0, y * 17.52 - 9.72) - 2.0**-16) * 2.0,
                    np.power(2.0, y * 17.52 - 9.72))


# --- ACESproxy 10-bit (S-2013-002) ---
def linear_to_acesproxy10(x):
    x = np.asarray(x, dtype=np.float64)
    cv = np.clip(np.log2(np.maximum(x, 2.0**-9.72)) * 50.0 + 550.0, 64.0, 940.0)
    return cv / 1023.0


def acesproxy10_to_linear(y):
    cv = np.asarray(y, dtype=np.float64) * 1023.0
    return np.power(2.0, (cv - 550.0) / 50.0)


# ============================================================================
# Gamut conversion matrices (RGB -> RGB, both at D65)
# ============================================================================

# Official published primaries (x, y).  White D65 = (0.3127, 0.3290) for all
# camera gamuts below.
PRIMARIES = {
    "rec709":          (0.6400, 0.3300, 0.3000, 0.6000, 0.1500, 0.0600),
    "sgamut3":         (0.7300, 0.2800, 0.1400, 0.8550, 0.1000, -0.0500),
    "sgamut3_cine":    (0.7660, 0.2750, 0.2250, 0.8000, 0.0890, -0.0870),
    "arri_wide_gamut3": (0.6840, 0.3130, 0.2210, 0.8480, 0.0861, -0.1020),
    "arri_wide_gamut4": (0.7347, 0.2653, 0.1424, 0.8576, 0.0991, -0.0308),
    "red_wide_gamut_rgb": (0.780308, 0.304253, 0.121595, 1.493994, 0.095612, -0.084589),
}
D65 = (0.3127, 0.3290)


def normalized_primary_matrix(primaries, white=D65):
    """RGB->XYZ matrix for the given xy primaries and white point."""
    xr, yr, xg, yg, xb, yb = primaries
    xw, yw = white
    m = np.array([[xr / yr, xg / yg, xb / yb],
                  [1.0, 1.0, 1.0],
                  [(1 - xr - yr) / yr, (1 - xg - yg) / yg, (1 - xb - yb) / yb]])
    w = np.array([xw / yw, 1.0, (1 - xw - yw) / yw])
    return m * np.linalg.solve(m, w)


def gamut_matrix(src, dst="rec709"):
    """3x3 matrix converting linear src-gamut RGB to linear dst-gamut RGB (D65)."""
    return np.linalg.solve(normalized_primary_matrix(PRIMARIES[dst]),
                           normalized_primary_matrix(PRIMARIES[src]))


# Precomputed src-gamut -> Rec.709 matrices (rounded copies live in the apps).
MATRICES_TO_REC709 = {name: gamut_matrix(name) for name in PRIMARIES if name != "rec709"}


def apply_matrix(rgb, matrix):
    """Apply a 3x3 gamut matrix to an Nx3 (or length-3) array of RGB rows."""
    rgb = np.asarray(rgb, dtype=np.float64)
    return rgb @ matrix.T


# ============================================================================
# .cube 3D-LUT helpers (Adobe spec: RED varies fastest)
# ============================================================================

def reshape_cube(flat_data, size):
    """Reshape flat (size^3, 3) .cube data to an [R, G, B, ch] grid.

    The Adobe Cube spec writes the red component varying fastest, so a plain
    C-order reshape yields [blue, green, red]; we transpose to [red, green,
    blue] so axis 0 indexes R.
    """
    flat_data = np.asarray(flat_data, dtype=np.float64)
    return np.transpose(flat_data.reshape((size, size, size, 3)), (2, 1, 0, 3))


# ============================================================================
# Self-test
# ============================================================================

if __name__ == "__main__":
    ok = True

    def check(name, got, expected, tol=2e-4):
        global ok
        got = float(np.asarray(got).ravel()[0])
        good = abs(got - expected) <= tol
        ok = ok and good
        print(f"  [{'PASS' if good else 'FAIL'}] {name:24s} got={got:.6f} expected={expected:.6f}")

    print("18% mid-grey encoded values (vs official specs):")
    g = np.array([0.18])
    check("LogC3", linear_to_logc3(g), 0.391007)
    check("LogC4", linear_to_logc4(g), 0.278396)
    check("S-Log3", linear_to_slog3(g), 0.410557)
    check("Log3G10", linear_to_log3g10(g), 1.0 / 3.0)
    check("V-Log", linear_to_vlog(g), 0.423311)
    check("Canon Log 2", linear_to_canonlog2(g), 0.379865)
    check("Rec.709", linear_to_rec709(g), 0.409008)
    check("sRGB", linear_to_srgb(g), 0.461356)
    check("ACEScc", linear_to_acescc(g), 0.413588)
    check("ACEScct", linear_to_acescct(g), 0.413588)
    check("ACESproxy10", linear_to_acesproxy10(g), 0.416716)

    print("\nEncode/decode round-trips (max |err| over 0..1):")
    xs = np.linspace(0.0, 1.0, 51)
    pairs = [
        ("LogC3", linear_to_logc3, logc3_to_linear),
        ("LogC4", linear_to_logc4, logc4_to_linear),
        ("S-Log3", linear_to_slog3, slog3_to_linear),
        ("Log3G10", linear_to_log3g10, log3g10_to_linear),
        ("V-Log", linear_to_vlog, vlog_to_linear),
        ("Canon Log 2", linear_to_canonlog2, canonlog2_to_linear),
        ("Rec.709", linear_to_rec709, rec709_to_linear),
        ("sRGB", linear_to_srgb, srgb_to_linear),
        ("PQ", linear_to_pq, pq_to_linear),
        ("HLG", linear_to_hlg, hlg_to_linear),
        ("ACEScc", linear_to_acescc, acescc_to_linear),
        ("ACEScct", linear_to_acescct, acescct_to_linear),
        ("ACESproxy10", linear_to_acesproxy10, acesproxy10_to_linear),
    ]
    for name, enc, dec in pairs:
        # ACESproxy clips below CV 64, so test it above its low-end floor;
        # every curve here is invertible over [0, 1] with no clipping, so the
        # full range (including the top endpoint) is validated.
        xr = xs if name != "ACESproxy10" else np.clip(xs, 2e-3, 1.0)
        rt = np.asarray(dec(enc(xr))).ravel()
        err = float(np.max(np.abs(rt - xr)))
        good = err < 1e-4
        ok = ok and good
        print(f"  [{'PASS' if good else 'FAIL'}] {name:24s} max|err|={err:.2e}")

    print("\nGamut matrices:")
    off_awg3 = np.array([[1.617523, -0.537287, -0.080237],
                         [-0.070573, 1.334613, -0.264039],
                         [-0.021102, -0.226954, 1.248056]])
    d = float(np.max(np.abs(gamut_matrix("arri_wide_gamut3") - off_awg3)))
    good = d < 1e-5
    ok = ok and good
    print(f"  [{'PASS' if good else 'FAIL'}] AWG3->Rec.709 vs official ARRI matrix  max|d|={d:.2e}")
    for name, M in MATRICES_TO_REC709.items():
        rs = float(np.max(np.abs(M.sum(axis=1) - 1.0)))
        good = rs < 1e-9
        ok = ok and good
        print(f"  [{'PASS' if good else 'FAIL'}] {name:22s} row-sums==1 (D65->D65)  err={rs:.1e}")

    print("\n" + ("ALL CHECKS PASSED" if ok else "*** SOME CHECKS FAILED ***"))
    import sys
    sys.exit(0 if ok else 1)
