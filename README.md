# DCCM — The Digital Cinema Color Management Guide

> A field manual for DITs, colorists, and post-production professionals who need color to work — from the camera sensor to the final DCP.

## What This Is

Color management breaks on set. It breaks in post. It breaks in the DCP theater. This guide is the reference you pull up when it does.

DCCM covers the full pipeline: camera color science, log/RAW encoding, LUTs, ACES, HDR, codecs, on-set workflows, virtual production, remote grading, display calibration, and the math behind it all. No fluff. No marketing speak. Just the technical details you actually need to make informed decisions under pressure.

## Who This Is For

- **DITs** setting up LUTs, managing exposure, and keeping color consistent across 50+ setups per day
- **Colorists** working in Resolve, Baselight, Nucoda, or Lustre who need to understand the pipeline upstream
- **Post supervisors** choosing codecs, delivery specs, and color spaces for Netflix, Amazon, Apple, or theatrical
- **Cinematographers** who want to understand what happens to their image after the sensor
- **VFX artists** receiving plates and wondering why the colors look different on every monitor

## What's Inside

14 chapters, 50+ files, covering everything from CIE 1931 to the latest Dolby Vision 2 spec.

### 1. Foundations
- [1.1 Basic Color Science](1.1_Basic_Color_Science.md) — CIE XYZ, color matching functions, spectral power distributions. The physics of why color works the way it does.
- [1.2 Gamma, Gamut, and Logarithmic Encoding](1.2_Gamma_Gamut_Log.md) — Why gamma exists, why log curves look flat, and why gamut matters more than resolution.

### 2. Camera Color Science
- [2.1 ARRI Cameras](2.1_ARRI_Cameras.md) — ALEXA 35, ALEXA 265, ALEXA LF, Log C3, ARRI Wide Gamut 4. Updated for SUP 6.0 and the 2025–2026 release cycle.
- [2.2 Sony Cameras](2.2_Sony_Cameras.md) — VENICE 2, BURANO, FX6, FR7. S-Gamut3.Cine, S-Log3, and the latest firmware updates.
- [2.3 RED Cameras](2.3_RED_Cameras.md) — V-RAPTOR, KOMODO, DSMC2. REDWideGamutRGB, IPP2, and the firmware 2.2 changes.
- [2.4 Blackmagic Cameras](2.4_Blackmagic_Cameras.md) — URSA Cine 100G, Cinema 6K, BRAW. Gen 5 and Gen 6 color science.

### 3. Recording
- [3.1 Log Encodings](3.1_Log_Encodings.md) — The math behind Log C, S-Log3, RED Log3G10, and BMD Film Gen 5.
- [3.2 RAW vs. Log](3.2_RAW_vs_Log.md) — When to shoot RAW, when to shoot log, and when neither matters.
- [3.3 Exposing Log and RAW](3.3_Exposing_Log_RAW.md) — False color, waveform, and why your meter is lying to you.

### 4. LUTs and Color Transforms
- [4.1 1D vs. 3D LUTs](4.1_1D_vs_3D_LUTs.md) — What LUTs actually do, and why 1D LUTs can't fix hue shifts.
- [4.2 Technical vs. Creative LUTs](4.2_Technical_vs_Creative_LUTs.md) — The difference between a color space transform and a "look."
- [4.3 Color Management Pipelines](4.3_Color_Management_Pipelines_LUTs.md) — How to chain LUTs without destroying your image.
- [4.4 Converting Color Spaces](4.4_Converting_Color_Spaces.md) — Rec. 709, DCI-P3, Rec. 2020, and the traps in between.

### 5. ACES
- [5.1 ACES Fundamentals](5.1_ACES_Fundamentals.md) — What ACES is, why it exists, and when to use it.
- [5.2 ACES vs. Camera-Native](5.2_ACES_vs_Camera_Native.md) — The trade-offs between ACES and manufacturer-specific workflows.
- [5.3 Integrating ACES](5.3_Integrating_ACES.md) — How to set up ACES in Resolve, Baselight, Nuke, and Maya.
- [5.4 ACES 2.0 Deep Dive](5.4_ACES_2.0_Deep_Dive.md) — Released April 2025. The new RRT, the vendor matrix, and what changed from 1.x. Updated for the OCIO 2.5.0 era.

### 6. HDR
- [6.1 PQ and HLG Fundamentals](6.1_PQ_HLG.md) — ST 2084 vs. HLG, and why your mastering room needs to be dark.
- [6.2 HDR Standards and Grading](6.2_HDR_Standards_Grading.md) — Dolby Vision 2, HDR10+ Advanced, and the platform delivery matrix (Netflix, Amazon, Apple, Disney+, WBD).
- [6.3 Mapping to HDR](6.3_Mapping_to_HDR.md) — SDR-to-HDR, HDR-to-SDR, and why tone mapping is harder than it looks.
- [6.4 HDR Monitoring](6.4_HDR_Monitoring.md) — QD-OLED reference monitors, calibration, and why your client monitor is not reference.
- [6.5 Dynamic HDR Formats](6.5_Dynamic_HDR_Formats.md) — HDR10+, Dolby Vision, AV1 HDR delivery. The 2026 streaming platform requirements.

### 7. On-Set Workflows
- [7.1 On-Set Hardware and Software](7.1_On_Set_Hardware_Software.md) — LUT boxes, live grading systems, and the DIT cart.
- [7.2 Reference Monitors](7.2_Reference_Monitors.md) — Calibration, environment control, and why 6500K is not "neutral."
- [7.3 Wireless Video and Color Accuracy](7.3_Wireless_Video_Color.md) — Teradek, Bolt, and the latency/color trade-off.
- [7.4 On-Set LUTs and CDLs](7.4_On_Set_LUTs_CDLs.md) — Creating looks that survive the pipeline to the color suite.
- [7.5 Maintaining Color Consistency](7.5_Maintaining_Color_Consistency.md) — From camera to dailies to final grade without drift.
- [7.6 Virtual Production](7.6_Virtual_Production.md) — LED volumes, OpenVPCal, hybrid workflows, and why your LED wall is not a monitor. Updated for P1.5mm and 2026 VP standards.

### 8. Codecs and Data
- [8.1 Codecs Overview](8.1_Codecs_Overview.md) — ProRes, DNxHR, EXR, and why you care about bit depth.
- [8.2 Bit Depth, Chroma Subsampling, and Compression](8.2_Bit_Depth_Chroma_Compression.md) — 422 vs. 444, 8-bit vs. 10-bit, and where the artifacts hide.
- [8.3 Data Rates and Storage](8.3_Data_Rates_Storage.md) — How much space you actually need, and why LTO-9 exists.
- [8.4 Wrapping Codecs](8.4_Wrapping_Codecs.md) — MXF, MOV, and the container chaos.
- [8.5 Emerging Codecs](8.5_Emerging_Codecs.md) — VVC hardware decode, AV1 patent risk, LCEVC, AV2 (May 2026), and the three-codec ladder strategy.

### 9. Display and Delivery
- [9.1 Monitoring Differences](9.1_Monitoring_Differences.md) — On-set, post, and theatrical. Three different images, one master.
- [9.2 Standardized Color Spaces](9.2_Standardized_Color_Spaces.md) — Rec. 709, DCI-P3, Rec. 2020, and what "covers 100%" actually means.
- [9.3 Display-Referred vs. Scene-Referred](9.3_Display_Scene_Referred.md) — Why your grade looks different on every screen.
- [9.4 Streaming and DCP](9.4_Streaming_DCP.md) — Platform specs, IMF, and the delivery spec maze.
- [9.5 IMF Workflows](9.5_IMF_Workflows.md) — Application #2E, supplemental packages, and the Netflix/Amazon/Apple requirements.

### 10. Real-World Workflows
- [10.1 End-to-End Pipelines](10.1_End_to_End_Pipelines.md) — ARRI, Sony, RED. From sensor to DCP.
- [10.2 ACES in Resolve and Baselight](10.2_ACES_Resolve_Baselight.md) — Setup, configuration, and the common failure modes.
- [10.3 On-Set LUTs in Editorial](10.3_On_Set_LUTs_Editorial.md) — How editorial gets the look without breaking the pipeline.
- [10.4 Archival and Versioning](10.4_Archival_Versioning.md) — LTO, cloud storage, and the 10-year archive problem.
- [10.5 Remote Grading](10.5_Remote_Grading.md) — DaVinci Resolve Cloud, Google Stream, Sohonet ClearView Pivot, and the reality of cloud color grading.

### 11. Math and Deep Science
- [11.1 Formulas](11.1_Formulas.md) — CIE XYZ, YCbCr, ICtCp, PQ, HLG, JzAzBz, and OKLab. The equations you reference when you need them.
- [11.2 Charts and Tables](11.2_Charts_Tables.md) — Reference data for quick lookup.
- [11.3 Block Diagrams](11.3_Block_Diagrams.md) — Visual pipeline references.
- [11.4 References](11.4_References.md) — 70+ standards, papers, and industry documents from 2025–2026.
- [11.5 Advanced Color Science](11.5_Advanced_Color_Science.md) — Gamut mapping, color appearance modeling, metamerism, multi-primary displays, NeRF, and 3D Gaussian Splatting.

### 12. Practical Guide
- [12.1 Summary and Key Concepts](12.1_Summary.md) — The cheat sheet. Core principles, DIT responsibilities, colorist responsibilities, and the workflow timeline.
- [12.2 Camera Comparisons](12.2_Camera_Comparisons.md) — ARRI vs. Sony vs. RED. Color science, not spec sheets.
- [12.3 Recommended Practices Checklist](12.3_Recommended_Practices.md) — Pre-production, production, post-production. The checklist you print and tape to your cart.
- [12.4 Display Characterization](12.4_Display_Characterization.md) — How to measure and verify your monitor is actually calibrated.

### 13. AI and Machine Learning in Color Management
- [13.0 AI & ML in Color Management](13.0_AI_ML_Color_Management.md) — AI color matching, denoising, upscaling, LUT generation, and the ethics of algorithmic grading. What works, what doesn't, and what to disclose.

### 14. Sustainability and Green Production
- [14.0 Sustainability & Green Production](14.0_Sustainability_Green_Production.md) — The carbon footprint of post-production, energy-efficient codecs, cloud rendering carbon optimization, and the 14-item DIT sustainability checklist. Because 500 TB of RAW has a cost beyond the hard drive.

### Verified reference code
- [`curves.py`](curves.py) — a single-file, numpy-only implementation of the transfer functions (LogC3/LogC4, S-Log3, Log3G10, V-Log, Canon Log 2, Rec.709, sRGB, PQ, HLG, ACEScc/ACEScct/ACESproxy) and camera→Rec.709 gamut matrices. **Every constant is verified against the official specs** — run `python curves.py` to self-test each curve's 18% mid-grey value, round-trips, and the gamut matrices. When a formula in the prose and `curves.py` disagree, `curves.py` is authoritative.

---

## How to Use This Guide

**New to color management?** Start with [1.1 Basic Color Science](1.1_Basic_Color_Science.md) and [1.2 Gamma, Gamut, and Log](1.2_Gamma_Gamut_Log.md). Then jump to your camera chapter (2.1–2.4) and the workflow summary in [12.1](12.1_Summary.md).

**Working on a specific problem?** Use the TOC above. Each chapter is self-contained. The [11.4 References](11.4_References.md) section has direct links to standards and manufacturer documentation.

**Preparing for a shoot?** Print [12.3 Recommended Practices Checklist](12.3_Recommended_Practices.md). It covers the decisions you need to make before the first slate.

**Need the math?** [11.1 Formulas](11.1_Formulas.md) has the equations. [11.2 Charts and Tables](11.2_Charts_Tables.md) has the reference data.

## How This Guide Is Maintained

DCCM is updated continuously. The original content was written in early 2024. In June 2026, the repository underwent a comprehensive modernization:

- **ACES 2.0** — Updated from "in development" to released (April 2025), with full vendor matrix and OCIO 2.5.0 configs
- **Camera firmware** — All four camera chapters updated through 2025–2026 release cycles
- **HDR** — Dolby Vision 2, HDR10+ Advanced, QD-OLED monitors, and the complete platform delivery matrix
- **Virtual Production** — OpenVPCal, hybrid workflows, P1.5mm LED standards, Relightable Gaussian Splatting
- **Codecs** — VVC hardware decode, AV1 patent risk, LCEVC, AV2 release, ProRes RAW cross-platform
- **Cloud grading** — DaVinci Resolve Cloud, Google Stream, Sohonet ClearView Pivot
- **AI/ML** — New chapter on AI color tools, denoising, upscaling, and ethics
- **Sustainability** — New chapter on carbon footprint, energy-efficient codecs, and green production standards
- **Math** — JzAzBz, ICtCp, OKLab (CSS Color Module Level 4 compliant), multi-primary displays, NeRF, 3D Gaussian Splatting

All updates follow an **additive-only methodology** — original content is preserved intact, with new sections appended using clear archival headers. Nothing is deleted.

## Contributing

Found an error? Missing a standard? Outdated firmware reference? Open an issue or submit a PR. This guide improves when the people using it every day contribute back.

For major additions, follow the additive-only convention: append new sections after the existing content, clearly marked with a `---` separator and an archival header. This preserves the historical accuracy of the original text while keeping the guide current.

## License

This guide is provided as a free resource for the digital cinema community. Use it, share it, and improve it.

---

*Last updated: June 2026. DCCM is a living document — the color science in Chapter 1 is as true today as it was in 1931, but the camera firmware in Chapter 2 changes every quarter. Check the archival headers in each chapter for the specific update date of that section.*
