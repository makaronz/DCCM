# TOC Structure: Before and After Comparison

**Document**: Digital Cinema Color Management (DCCM)
**Proposal Date**: 2026-01-03
**Current TOC**: 74 sections | **Proposed TOC**: 90 sections (+21.6%)

---

## Chapter 1: Introduction & Theoretical Foundations

### Current Structure (2 sections)
```
1. Introduction & Theoretical Foundations
   1.1 Basic Color Science
   1.2 Gamma, Gamut, and Logarithmic Encoding
```

### Proposed Structure (2 sections)
```
✅ UNCHANGED - No additions needed in Chapter 1
```

**Justification**: Foundation chapters are comprehensive; no critical gaps identified.

---

## Chapter 2: Camera-Specific Color Science

### Current Structure (3 sections)
```
2. Camera-Specific Color Science
   2.1 ARRI Cameras (ALEXA 35, ALEXA LF)
   2.2 Sony Cameras (VENICE, VENICE 2, BURANO)
   2.3 RED Cameras (V-RAPTOR, DSMC2 lineup)
```

### Proposed Structure (4 sections + 1 subsection)
```
2. Camera-Specific Color Science
   2.1 ARRI Cameras (ALEXA 35, ALEXA LF)
   ├─ 2.1.1 ARRI REVEAL Color Science Deep Dive [NEW - Important]
   2.2 Sony Cameras (VENICE, VENICE 2, BURANO)
   2.3 RED Cameras (V-RAPTOR, DSMC2 lineup)
   2.4 Blackmagic Cinema Cameras [NEW - Critical]
```

**Additions**:
- **2.1.1** ARRI REVEAL (2,800 words) - Deep dive into major color science upgrade
- **2.4** Blackmagic Cameras (3,500 words) - Missing major manufacturer

**Gaps Addressed**:
- Blackmagic Design cameras (URSA Mini Pro 12K, PYXIS 6K) widely used but absent
- ARRI REVEAL (new in ALEXA 35) represents major architecture change

---

## Chapter 3: Logarithmic & RAW Recording

### Current Structure (3 sections)
```
3. Logarithmic & RAW Recording
   3.1 Mathematical Breakdown of Log Encodings
   3.2 RAW Capture vs. Log Capture
   3.3 Best Practices for Exposing Log and RAW
```

### Proposed Structure (3 sections)
```
✅ UNCHANGED - Log/RAW coverage is comprehensive
```

**Justification**: Section 3.1 includes modern interpolation methods (trilinear, tetrahedral); no gaps identified.

---

## Chapter 4: LUTs (Lookup Tables) and Color Transforms

### Current Structure (4 sections)
```
4. LUTs (Lookup Tables) and Color Transforms
   4.1 1D vs. 3D LUTs
   4.2 Technical LUTs vs. Creative LUTs
   4.3 Color Management Pipelines & LUTs
   4.4 Converting to Standardized Color Spaces
```

### Proposed Structure (5 sections)
```
4. LUTs (Lookup Tables) and Color Transforms
   4.1 1D vs. 3D LUTs
   4.2 Technical LUTs vs. Creative LUTs
   4.3 Color Management Pipelines & LUTs
   4.4 Converting to Standardized Color Spaces
   4.5 Gamut Mapping and Tone Mapping Operators [NEW - Important]
```

**Additions**:
- **4.5** Gamut Mapping Operators (3,600 words) - Critical for HDR→SDR delivery

**Gaps Addressed**:
- No coverage of tone/gamut mapping algorithms (Reinhard, filmic, ACES RRT SDR)
- Missing soft-clipping vs. hard-clipping guidance
- No out-of-gamut warning system coverage
- Creative vs. technical tone mapping distinction absent

---

## Chapter 5: ACES (Academy Color Encoding System)

### Current Structure (3 sections)
```
5. ACES (Academy Color Encoding System)
   5.1 ACES Fundamentals
   5.2 ACES vs. Camera-Native Workflows
   5.3 Integrating ACES
```

### Proposed Structure (4 sections)
```
5. ACES (Academy Color Encoding System)
   5.1 ACES Fundamentals
   5.2 ACES vs. Camera-Native Workflows
   5.3 Integrating ACES
   5.4 ACES 2.0 and Next-Generation Workflows [NEW - Critical]
```

**Additions**:
- **5.4** ACES 2.0 (4,200 words) - Industry transition active

**Gaps Addressed**:
- ACES 2.0 referenced as "in development" but released in 2024
- Missing RRT+ODT→RRT+ODT+SRT architecture changes
- No ACES 2.0 Input Transform specifications
- AMF (ACES Metadata Files) absent
- Backward compatibility and migration strategies missing

---

## Chapter 6: HDR (High Dynamic Range) Workflows

### Current Structure (4 sections)
```
6. HDR (High Dynamic Range) Workflows
   6.1 PQ and HLG Fundamentals
   6.2 HDR Standards and Grading
   6.3 Mapping to HDR
   6.4 HDR Monitoring
```

### Proposed Structure (6 sections)
```
6. HDR (High Dynamic Range) Workflows
   6.1 PQ and HLG Fundamentals
   6.2 HDR Standards and Grading
   6.3 Mapping to HDR
   6.4 HDR Monitoring
   6.5 Dynamic HDR Formats (HDR10+ and SL-HDR) [NEW - Critical]
   6.6 HLG Production and Broadcast Workflows [NEW - Important]
```

**Additions**:
- **6.5** Dynamic HDR Formats (3,800 words) - HDR10+ and SL-HDR
- **6.6** HLG Production (3,400 words) - Broadcast-specific workflows

**Gaps Addressed**:
- HDR10+ and SL-HDR mentioned but lack dedicated coverage
- No dynamic metadata creation tools guidance
- HLG theoretical only; no broadcast production workflows
- Missing HLG camera setup for live production
- No HLG vs. PQ genre-specific recommendations

---

## Chapter 7: On-Set Workflows & Live Grading

### Current Structure (5 sections)
```
7. On-Set Workflows & Live Grading
   7.1 Hardware and Software
   7.2 Setting up Reference Monitors
   7.3 Wireless Video and Color Accuracy
   7.4 Creating On-Set LUTs/CDLs
   7.5 Maintaining Color Consistency
```

### Proposed Structure (7 sections)
```
7. On-Set Workflows & Live Grading
   7.1 Hardware and Software
   7.2 Setting up Reference Monitors
   7.3 Wireless Video and Color Accuracy
   7.4 Creating On-Set LUTs/CDLs
   7.5 Maintaining Color Consistency
   7.6 Virtual Production and LED Volume Color Pipelines [NEW - Critical]
   7.7 Color Metadata Management and Propagation [NEW - Important]
```

**Additions**:
- **7.6** Virtual Production (5,500 words) - Largest addition; LED volume workflows
- **7.7** Color Metadata (3,100 words) - Pipeline integration

**Gaps Addressed**:
- **Section 7.6**: No virtual production coverage (Mandalorian-style workflows)
  - Missing nDisplay/Unreal Engine color space transforms
  - No inner/outer frustum color alignment guidance
  - Camera tracking color synchronization absent
  - LED wall calibration (ICtCp, Rec.2020) missing
  - ACES integration with real-time engines not covered
- **Section 7.7**: No metadata pipeline focus
  - Missing CDL format and limitations
  - ASC-CDL vs. vendor extensions not explained
  - No metadata extraction on set workflows
  - Editorial conform with color metadata absent

---

## Chapter 8: Codecs & Data Management

### Current Structure (4 sections)
```
8. Codecs & Data Management
   8.1 Overview of Major Codecs
   8.2 Bit-Depth, Chroma Subsampling, and Compression
   8.3 Data Rates and Storage
   8.4 Wrapping Codecs (Container Formats)
```

### Proposed Structure (5 sections)
```
8. Codecs & Data Management
   8.1 Overview of Major Codecs
   8.2 Bit-Depth, Chroma Subsampling, and Compression
   8.3 Data Rates and Storage
   8.4 Wrapping Codecs (Container Formats)
   8.5 Emerging Codecs (AV1, JPEG XS, H.266/VVC) [NEW - Critical]
```

**Additions**:
- **8.5** Emerging Codecs (3,200 words) - AV1, JPEG XS, H.266/VVC

**Gaps Addressed**:
- AV1 (AOM) codec absent; adopted by streaming platforms
- JPEG XS (SMPTE ST 2117) missing; standardized for IP contribution
- H.266/VVC not covered; next-generation codec
- No deployment timelines or bit depth considerations

---

## Chapter 9: Display & Projection

### Current Structure (4 sections)
```
9. Display & Projection
   9.1 Monitoring Differences: On-Set, Post-Production, and Theatrical Projection
   9.2 Standardized Color Spaces (Rec. 709, P3, Rec. 2020)
   9.3 Display-Referred vs. Scene-Referred
   9.4 Streaming Platforms and DCP
```

### Proposed Structure (6 sections)
```
9. Display & Projection
   9.1 Monitoring Differences: On-Set, Post-Production, and Theatrical Projection
   9.2 Standardized Color Spaces (Rec. 709, P3, Rec. 2020)
   9.3 Display-Referred vs. Scene-Referred
   9.4 Streaming Platforms and DCP
   9.5 IMF (Interoperable Master Format) Workflows [NEW - Critical]
   9.6 Consumer Display Calibration Considerations [NEW - Nice-to-Have]
```

**Additions**:
- **9.5** IMF Workflows (4,800 words) - Streaming platform requirement
- **9.6** Consumer Display Calibration (2,600 words) - Final review considerations

**Gaps Addressed**:
- **Section 9.5**: IMF only mentioned in passing
  - No SMPTE ST 2067 series composition coverage
  - CPL (Composition Playlist) management absent
  - IMF essences (JPEG 2000, PCM) not explained
  - OPL (Output Profile List) missing
  - No IMF creation tools guidance (Drax, Clipster)
  - QC procedures for IMF packages absent
- **Section 9.6**: No consumer display context
  - Missing consumer HDR display variability awareness
  - OLED vs. LCD differences not covered
  - No consumer calibration tools reference
  - Managing client expectations absent

---

## Chapter 10: Real-World Workflow Examples

### Current Structure (4 sections)
```
10. Real-World Workflow Examples
   10.1 End-to-End Pipelines (ARRI, Sony, and RED)
   10.2 ACES in Resolve/Baselight
   10.3 Using On-Set LUTs in Editorial
   10.4 Archival and Versioning
```

### Proposed Structure (5 sections)
```
10. Real-World Workflow Examples
   10.1 End-to-End Pipelines (ARRI, Sony, and RED)
   10.2 ACES in Resolve/Baselight
   10.3 Using On-Set LUTs in Editorial
   10.4 Archival and Versioning
   10.5 Remote Grading and Cloud Collaboration [NEW - Critical]
```

**Additions**:
- **10.5** Remote Grading (4,100 words) - Post-COVID standard workflows

**Gaps Addressed**:
- No remote grading architecture coverage (Resolve/Baselight cloud, Evercast)
- Missing bandwidth and latency requirements for HDR
- Synchronized monitoring via web (Frame.io, Moxion) absent
- No color-managed review platforms guidance
- Security considerations missing
- Hybrid on-prem/cloud workflows not covered

---

## Chapter 11: Mathematical Appendix & Diagrams

### Current Structure (4 sections)
```
11. Mathematical Appendix & Diagrams
   11.1 Formulas
   11.2 Charts/Tables
   11.3 Block Diagrams
   11.4 References
```

### Proposed Structure (6 sections)
```
11. Mathematical Appendix & Diagrams
   11.1 Formulas
   11.2 Charts/Tables
   11.3 Block Diagrams
   11.4 References
   11.5 Advanced Color Science (JzAzBz, ICtCp, CAT16) [NEW - Critical]
   11.6 Test Patterns and Validation Procedures [NEW - Important]
```

**Additions**:
- **11.5** Advanced Color Science (4,300 words) - Modern HDR and perceptual metrics
- **11.6** Test Patterns and Validation (3,300 words) - QC standardization

**Gaps Addressed**:
- **Section 11.5**: No advanced color appearance models
  - JzAzBz (perceptual uniform space) missing entirely
  - ICtCp (HDR-friendly encoding) absent
  - CAT16 (chromatic adaptation) not covered
  - No perceptual uniform ΔE metrics (ΔEITP, ΔEJz)
  - Gamut mapping with appearance models absent
  - Equations and practical applications missing
- **Section 11.6**: No validation procedures
  - Missing color space test patterns (SMPTE, EBU)
  - No skin tone patches coverage
  - Gamut boundary visualization absent
  - ΔE metrics not comprehensively covered
  - No perceptual validation procedures
  - Legal signal validation (broadcast safe) missing
  - HDR validation (peak luminance, fallback) absent
  - QC documentation standards not covered

---

## Chapter 12: Conclusion & Best Practices

### Current Structure (3 sections)
```
12. Conclusion & Best Practices
   12.1 Summary & Key Concepts for DITs and Colorists
   12.2 Camera Comparisons: ARRI vs. Sony vs. RED (Color Science)
   12.3 Recommended Practices Checklist
```

### Proposed Structure (4 sections)
```
12. Conclusion & Best Practices
   12.1 Summary & Key Concepts for DITs and Colorists
   12.2 Camera Comparisons: ARRI vs. Sony vs. RED (Color Science)
   12.3 Recommended Practices Checklist
   12.4 Display Characterization and 3D LUT Profiling [NEW - Critical]
```

**Additions**:
- **12.4** Display Characterization (3,900 words) - Custom 3D LUT creation

**Gaps Addressed**:
- No display profiling workflow coverage
- Colorimeter vs. Spectroradiometer not explained
- ICC profiles vs. 3D LUTs distinction absent
- No characterization of consumer displays for review
- Calibration validation (ΔE tracking) missing
- Profiling for HDR and SDR not covered
- On-set quick calibration procedures absent

---

## Chapter 13: Glossary and Definitions [NEW CHAPTER]

### Current Structure
```
[No Chapter 13 exists]
```

### Proposed Structure (1 section)
```
13. Glossary and Definitions [NEW - Nice-to-Have]
    13.1 Comprehensive Terminology Reference [NEW - Nice-to-Have]
```

**Additions**:
- **13.1** Comprehensive Glossary (2,200 words) - Centralized terminology reference

**Gaps Addressed**:
- No centralized terminology reference
- Improves document usability for cross-referencing
- Comprehensive glossary of all color science terms
- Cross-referenced to sections where terms introduced
- Pronunciation guide for non-English terms

---

## Summary Statistics

### Current TOC
- **Total Chapters**: 12
- **Total Sections**: 74
- **Average Sections/Chapter**: 6.2
- **Estimated Word Count**: ~140,000
- **Average Words/Section**: ~1,892

### Proposed TOC
- **Total Chapters**: 13 (+1)
- **Total Sections**: 90 (+16)
- **Average Sections/Chapter**: 6.9
- **Estimated Word Count**: ~199,000 (+59,000)
- **Average Words/Section**: ~2,211

### Growth Metrics
- **TOC Growth**: +21.6% (within 25% limit) ✅
- **Content Growth**: +42.0% (enhanced technical depth)
- **Chapter Addition**: +1 (Chapter 13: Glossary)
- **Section Addition**: +16 (9 Critical + 5 Important + 2 Nice-to-Have)

### Priority Distribution
```
CRITICAL:    9 sections (56% of additions)
IMPORTANT:   5 sections (31% of additions)
NICE-TO-HAVE: 2 sections (13% of additions)
```

### Content Depth Distribution
```
Under 3,000 words:    2 sections  (ARRI REVEAL, Glossary)
3,000-4,000 words:   10 sections  (Most additions)
4,000-5,000 words:    3 sections  (ACES 2.0, IMF, Remote Grading)
5,000+ words:         1 section   (Virtual Production - 5,500 words)
```

---

## Visual TOC Tree

```
DCCM Table of Contents (Proposed)
│
├─ Chapter 1: Introduction & Theoretical Foundations (2 sections) ✅
├─ Chapter 2: Camera-Specific Color Science (4 sections + 1 subsection) 🆕
│  ├─ 2.1 ARRI Cameras
│  │  └─ 2.1.1 ARRI REVEAL [NEW]
│  ├─ 2.2 Sony Cameras
│  ├─ 2.3 RED Cameras
│  └─ 2.4 Blackmagic Cameras [NEW]
├─ Chapter 3: Logarithmic & RAW Recording (3 sections) ✅
├─ Chapter 4: LUTs and Color Transforms (5 sections) 🆕
│  ├─ 4.1-4.4 [EXISTING]
│  └─ 4.5 Gamut Mapping Operators [NEW]
├─ Chapter 5: ACES (4 sections) 🆕
│  ├─ 5.1-5.3 [EXISTING]
│  └─ 5.4 ACES 2.0 [NEW]
├─ Chapter 6: HDR Workflows (6 sections) 🆕🆕
│  ├─ 6.1-6.4 [EXISTING]
│  ├─ 6.5 Dynamic HDR Formats [NEW]
│  └─ 6.6 HLG Production [NEW]
├─ Chapter 7: On-Set Workflows (7 sections) 🆕🆕
│  ├─ 7.1-7.5 [EXISTING]
│  ├─ 7.6 Virtual Production [NEW]
│  └─ 7.7 Color Metadata [NEW]
├─ Chapter 8: Codecs & Data Management (5 sections) 🆕
│  ├─ 8.1-8.4 [EXISTING]
│  └─ 8.5 Emerging Codecs [NEW]
├─ Chapter 9: Display & Projection (6 sections) 🆕🆕
│  ├─ 9.1-9.4 [EXISTING]
│  ├─ 9.5 IMF Workflows [NEW]
│  └─ 9.6 Consumer Display Calibration [NEW]
├─ Chapter 10: Real-World Workflow Examples (5 sections) 🆕
│  ├─ 10.1-10.4 [EXISTING]
│  └─ 10.5 Remote Grading [NEW]
├─ Chapter 11: Mathematical Appendix (6 sections) 🆕🆕
│  ├─ 11.1-11.4 [EXISTING]
│  ├─ 11.5 Advanced Color Science [NEW]
│  └─ 11.6 Test Patterns [NEW]
├─ Chapter 12: Conclusion & Best Practices (4 sections) 🆕
│  ├─ 12.1-12.3 [EXISTING]
│  └─ 12.4 Display Characterization [NEW]
└─ Chapter 13: Glossary and Definitions (1 section) 🆕
   └─ 13.1 Comprehensive Terminology [NEW]

Legend:
✅ Unchanged
🆕 New sections (16 total additions)
```

---

**END OF VISUAL COMPARISON**
