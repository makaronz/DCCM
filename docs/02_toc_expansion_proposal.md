# Digital Cinema Color Management: TOC Expansion Proposal

**Document Version**: 1.0
**Date**: 2026-01-03
**Analyst**: Hive Mind Collective - Analyst Agent
**Objective**: Targeted TOC expansion with maximum +25% growth (74 → ~93 sections)
**Focus**: Production-critical additions only, contemporary technologies, and modern workflows

---

## Executive Summary

This proposal identifies **16 high-priority additions** (+21.6% growth) to the Digital Cinema Color Management TOC, addressing critical gaps in:
- Virtual production and LED volume workflows
- Modern HDR delivery formats and standards
- Cloud-based collaboration and remote grading
- Contemporary color science advances (JzAzBz, ICtCp, CAT16)
- New camera models and codecs
- IMF and professional delivery formats
- Advanced testing and validation procedures

**Rationale**: Each addition addresses a documented production workflow gap with clear technical justification and alignment with current SMPTE/ITU/ACES standards.

---

## Part 1: Gap & Staleness Audit

### Critical Gaps Identified (18 issues)

#### 1. **Virtual Production & LED Volume Workflows**
- **Issue**: No coverage of color-critical LED wall rendering, nDisplay/Unreal Engine color pipelines, or camera tracking color alignment
- **Impact**: Productions increasingly use virtual production; incorrect color management breaks immersion
- **Production Risk**: High - requires specialized transforms and monitoring

#### 2. **Missing Contemporary HDR Formats**
- **Issue**: HDR10+ and SL-HDR are mentioned but lack dedicated sections; no coverage of consumer HDR ecosystem
- **Impact**: Colorists lack practical grading strategies for dynamic metadata formats
- **Production Risk**: Medium - affects deliverable quality

#### 3. **IMF (Interoperable Master Format) Insufficient Coverage**
- **Issue**: Only mentioned in streaming section; no dedicated workflow guidance
- **Impact**: Technical misunderstandings about IMF composition and CPL management
- **Production Risk**: High - required by major streaming platforms

#### 4. **No Cloud-Based Collaboration Coverage**
- **Issue**: Remote grading workflows, cloud dailies, and virtual screening rooms absent
- **Impact**: Post-COVID workflows require cloud collaboration; color accuracy risks high
- **Production Risk**: Medium - monitoring dependencies critical

#### 5. **Advanced Color Science Missing**
- **Issue**: JzAzBz (perceptual uniform space), ICtCp (HDR transport), CAT16 (chromatic adaptation) not covered
- **Impact**: Modern HDR workflows and perceptual metrics require these
- **Production Risk**: Medium - affects HDR quality assessment

#### 6. **Outdated Camera Coverage**
- **Issue**: Missing ARRI ALEXA 26V, Sony VENICE 2 extensions, RED KOMODO 6K/6K SLEPT
- **Impact**: Colorists lack IDT and rendering knowledge for current cameras
- **Production Risk**: High - new sensors have different color response

#### 7. **Insufficient Codec Coverage**
- **Issue**: AV1 (AOM), JPEG XS (SMPTE ST 2117), H.266/VVC not covered
- **Impact**: Future delivery formats and contribution feeds misunderstood
- **Production Risk**: Medium - emerging standards for streaming contribution

#### 8. **No ACES 2.0 Coverage**
- **Issue**: Document references ACES 2.0 as "in development" without details
- **Impact**: Missing next-generation ACES workflow changes (RRT+ODT architecture replacement)
- **Production Risk**: High - industry transition in progress

#### 9. **Insufficient Display Characterization**
- **Issue**: No 3D LUT profiling, ICC profiles, or display calibration workflows
- **Impact**: Monitoring trust compromised; color matching failures
- **Production Risk**: Critical - affects all grading decisions

#### 10. **Missing Wireless + HDR Intersection**
- **Issue**: Section 7.3 covers wireless but no HDR-specific wireless monitoring challenges
- **Impact**: On-set HDR monitoring via wireless (increasingly common) lacks guidance
- **Production Risk**: Medium - compromises on-set HDR evaluation

#### 11. **No Gamut Mapping Operator Coverage**
- **Issue**: Missing tone/gamut mapping algorithms (ICC, CMM, hue-locked vs. non-locked)
- **Impact**: Color volume mapping between disparate gamuts not understood
- **Production Risk**: Medium - affects HDR→SDR and wide→narrow gamut conversions

#### 12. **Insufficient Test Pattern/Validation Coverage**
- **Issue**: No standardized test patterns for color space validation, ΔE metrics, or perceptual testing
- **Impact**: Quality control lacks objective validation methods
- **Production Risk**: Medium - subjective QC risks

#### 13. **Missing Next-Gen Audio-Visual Sync**
- **Issue**: No coverage of SMPTE ST 2110-40 (IP-based audio-visual sync with color metadata)
- **Impact**: IP facility workflows lack color metadata transport guidance
- **Production Risk**: Low-Medium - facility-specific but growing

#### 14. **No HLG Production-Specific Guidance**
- **Issue**: HLG covered only theoretically; no broadcast production workflows
- **Impact**: Live/broadcast productions (EFP, sports) lack practical HLG grading
- **Production Risk**: Medium - HLG dominant in broadcast

#### 15. **Missing Out-of-Gamut Warning Systems**
- **Issue**: No coverage of soft-clipping, gamut warning, or legal signal validation
- **Impact**: Colorists unknowingly create out-of-gamut content for delivery targets
- **Production Risk**: High - delivery rejections

#### 16. **Insufficient Metadata Management**
- **Issue**: No coverage of metadata propagation (camera → editorial → grading → delivery)
- **Impact**: Color decisions lost in pipeline; EDL/XML/AAF metadata gaps
- **Production Risk**: Medium - conform issues

#### 17. **Missing DRT (Dynamic Range Toning) Coverage**
- **Issue**: No separate coverage of creative tone mapping vs. technical tone mapping
- **Impact**: Artistic HDR shaping not distinguished from display adaptation
- **Production Risk**: Low-Medium - creative control issue

#### 18. **No Consumer Device Calibration Context**
- **Issue**: Focus on professional monitors without consumer display limitations
- **Impact**: Final review fails to account for consumer HDR variability
- **Production Risk**: Medium - audience experience mismatch

---

## Part 2: Proposed TOC Additions (16 sections, +21.6%)

### Priority: CRITICAL (9 additions)

#### **1. Section 2.4: Blackmagic Cinema Cameras**
- **Placement**: After 2.3 RED Cameras
- **Justification**: Blackmagic Design cameras (URSA Mini Pro 12K, PYXIS 6K) now widely used in mid-tier productions; lacking dedicated color science coverage
- **Content Scope**: Generation 5 color science, Film Extended Dynamic Range, DaVinci Wide Gamut integration, RAW vs. ProRes encoding decisions
- **Estimated Depth**: 3,500 words
- **Dependencies**: None (builds on Section 1 foundations)

#### **2. Section 5.4: ACES 2.0 and Next-Generation Workflows**
- **Placement**: After 5.3 Integrating ACES
- **Justification**: ACES 2.0 (released 2024) replaces RRT+ODT with RRT+ODT+SRT, introduces ACES 2.0 Input Transforms; industry transition is active
- **Content Scope**: Architecture changes from ACES 1.x, new IDT specifications, AMF (ACES Metadata Files), backward compatibility, migration strategies
- **Estimated Depth**: 4,200 words
- **Dependencies**: 5.1, 5.3 (understands ACES 1.x first)

#### **3. Section 6.5: Dynamic HDR Formats (HDR10+ and SL-HDR)**
- **Placement**: After 6.4 HDR Monitoring
- **Justification**: Dynamic metadata formats increasingly required by broadcasters and streaming; distinct grading challenges from static HDR10
- **Content Scope**: HDR10+ (SMPTE ST 2094-40) metadata creation tools, SL-HDR (EBU Tech 3328) broadcast workflows, backward compatibility strategies, creative intent preservation with scene-by-scene metadata
- **Estimated Depth**: 3,800 words
- **Dependencies**: 6.1, 6.2 (understands PQ/HLG and static HDR first)

#### **4. Section 7.6: Virtual Production and LED Volume Color Pipelines**
- **Placement**: After 7.5 Maintaining Color Consistency
- **Justification**: Virtual production (The Mandalorian-style workflows) requires specialized color management between LED walls, camera, and final render; missing entirely
- **Content Scope**: nDisplay/Unreal Engine color space transforms, inner/outer frustum color alignment, camera tracking color synchronization, LED wall calibration (ICtCp, Rec.2020), on-set monitoring vs. final pixel matching, ACES integration with real-time engines
- **Estimated Depth**: 5,500 words
- **Dependencies**: 7.2 (reference monitoring), 6.x (HDR fundamentals)

#### **5. Section 8.5: Emerging Codecs (AV1, JPEG XS, H.266/VVC)**
- **Placement**: After 8.4 Wrapping Codecs
- **Justification**: AV1 adopted by streaming platforms; JPEG XS standardized for SMPTE ST 2110 contribution; H.266 in early adoption
- **Content Scope**: AV1 (AOM) characteristics and HDR support, JPEG XS (SMPTE ST 2117) visually lossless compression for IP workflows, H.266/VVC next-generation codec, bit depth and chroma subsampling considerations, deployment timelines
- **Estimated Depth**: 3,200 words
- **Dependencies**: 8.1 (codec fundamentals)

#### **6. Section 9.5: IMF (Interoperable Master Format) Workflows**
- **Placement**: After 9.4 Streaming Platforms and DCP
- **Justification**: IMF now required/recommended by Netflix, Disney+, Apple TV+; insufficient coverage in streaming section
- **Content Scope**: SMPTE ST 2067 series composition, CPL (Composition Playlist) management, IMF essences (JPEG 2000, PCM), OPL (Output Profile List), multi-version delivery, IMF creation tools (Drax, Clipster), QC procedures for IMF packages
- **Estimated Depth**: 4,800 words
- **Dependencies**: 9.4 (understands delivery formats)

#### **7. Section 10.5: Remote Grading and Cloud Collaboration**
- **Placement**: After 10.4 Archival and Versioning
- **Justification**: Post-COVD remote workflows now standard; color accuracy over WAN links, virtual screening rooms, cloud-based grading
- **Content Scope**: Remote grading architecture (Resolve/Baselight cloud, Evercast), bandwidth and latency requirements for HDR, synchronized monitoring via web (Frame.io, Moxion), color-managed review platforms, security considerations, hybrid on-prem/cloud workflows
- **Estimated Depth**: 4,100 words
- **Dependencies**: 7.3 (wireless video), 10.x (workflow examples)

#### **8. Section 11.5: Advanced Color Science (JzAzBz, ICtCp, CAT16)**
- **Placement**: After 11.4 References
- **Justification**: Modern HDR and perceptual metrics require color appearance models beyond CIE XYZ; missing entirely
- **Content Scope**: JzAzBz (perceptual uniform color space, ΔE calculations), ICtCp (HDR-friendly color encoding, PQ/HLG transport), CAT16 (chromatic adaptation transform for surround fields), perceptual uniform color difference metrics (ΔEITP, ΔEJz), gamut mapping with appearance models, equations and practical applications
- **Estimated Depth**: 4,300 words
- **Dependencies**: 1.1 (basic color science), 11.1 (formulas)

#### **9. Section 12.4: Display Characterization and 3D LUT Profiling**
- **Placement**: After 12.3 Recommended Practices Checklist
- **Justification**: Creating custom display transforms (3D LUTs) for non-standard monitors and projection; essential for accurate monitoring
- **Content Scope**: Display profiling workflow (Colorimeter vs. Spectroradiometer), 3D LUT creation (LightSpace, Calman), ICC profiles vs. 3D LUTs, characterization of consumer displays for review, calibration validation (ΔE tracking), profiling for HDR and SDR, on-set quick calibration procedures
- **Estimated Depth**: 3,900 words
- **Dependencies**: 7.2 (reference monitors), 9.1 (monitoring differences)

---

### Priority: IMPORTANT (5 additions)

#### **10. Section 2.1.1: ARRI REVEAL Color Science Deep Dive (Subsection)**
- **Placement**: As subsection within 2.1 ARRI Cameras
- **Justification**: REVEAL (new in ALEXA 35) represents major architecture change from previous ARRI color science; deserves dedicated technical coverage
- **Content Scope**: REVEAL pipeline architecture, improvements over Legacy ARRI Color Science, Log C4 encoding, highlight rolloff behavior, skin tone rendering characteristics, impact on ACES IDTs
- **Estimated Depth**: 2,800 words
- **Dependencies**: 2.1 (ARRI cameras overview)

#### **11. Section 4.5: Gamut Mapping and Tone Mapping Operators**
- **Placement**: After 4.4 Converting to Standardized Color Spaces
- **Justification**: Critical for HDR→SDR delivery, wide-gamut→narrow-gamut conversions; absent from current coverage
- **Content Scope**: Gamut mapping algorithms (hue-locked, chroma-preserving), tone mapping operators (Reinhard, filmic, ACES RRT SDR), soft-clipping vs. hard-clipping, creative vs. technical tone mapping, perceptual uniform mapping, out-of-gamut warning systems, implementation in Resolve/Baselight
- **Estimated Depth**: 3,600 words
- **Dependencies**: 4.4 (color space conversions)

#### **12. Section 6.6: HLG Production and Broadcast Workflows**
- **Placement**: After 6.5 Dynamic HDR Formats
- **Justification**: HLG is dominant in broadcast (EBU, NHK); current coverage is theoretical only
- **Content Scope**: HLG camera setup (Sony, ARRI, Panasonic), broadcast live production considerations, HLG vs. PQ for different genres, HLG monitoring on set, grading for HLG target displays, backward compatibility validation, HLG + WCG (Wide Color Gamut) workflows
- **Estimated Depth**: 3,400 words
- **Dependencies**: 6.1 (HLG fundamentals)

#### **13. Section 7.7: Color Metadata Management and Propagation**
- **Placement**: After 7.6 Virtual Production
- **Justification**: Color decisions (CDL, LUTs, grades) must propagate from camera through editorial to grading; current coverage lacks metadata pipeline focus
- **Content Scope**: Metadata containers (EDL, XML, AAF, OTIO), CDL (Color Decision List) format and limitations, ASC-CDL vs. vendor extensions, embedded LUTs in camera metadata, metadata extraction on set, editorial conform with color metadata, grading session metadata (Resolve/Baselight project files), version control for color decisions
- **Estimated Depth**: 3,100 words
- **Dependencies**: 7.4 (on-set LUTs/CDLs), 10.x (workflow examples)

#### **14. Section 11.6: Test Patterns and Validation Procedures**
- **Placement**: After 11.5 Advanced Color Science
- **Justification**: QC requires objective validation; no standardized test patterns or ΔE measurement coverage
- **Content Scope**: Color space test patterns (SMPTE, EBU, custom), skin tone patches, gamut boundary visualization, ΔE metrics (ΔE76, ΔE94, ΔE2000, ΔEJz), perceptual validation procedures, legal signal validation (broadcast safe), HDR validation (peak luminance, fallback), QC documentation standards
- **Estimated Depth**: 3,300 words
- **Dependencies**: 11.1 (formulas), 11.5 (advanced color science)

---

### Priority: NICE-TO-HAVE (2 additions)

#### **15. Section 9.6: Consumer Display Calibration Considerations**
- **Placement**: After 9.5 IMF Workflows
- **Justification**: Understanding consumer display limitations improves final review and delivery decisions
- **Content Scope**: Consumer HDR display variability (tone mapping, peak brightness), OLED vs. LCD differences, consumer calibration tools ( Spears & Munsil, AVS HD 709), managing client expectations, reference monitoring vs. consumer reality, reviewing on consumer displays before delivery
- **Estimated Depth**: 2,600 words
- **Dependencies**: 9.1 (monitoring differences), 9.4 (streaming platforms)

#### **16. Section 13: Glossary and Definitions (New Chapter)**
- **Placement**: After 12.4 Display Characterization
- **Justification**: Centralized terminology reference improves document usability for cross-referencing
- **Content Scope**: Comprehensive glossary of all color science terms used throughout document (AP0/AP1, IDT/ODT, PQ/HLG, CDL, LUT types, codec terms, etc.), cross-referenced to sections where terms are introduced, pronunciation guide for non-English terms (gamut, chroma, etc.)
- **Estimated Depth**: 2,200 words
- **Dependencies**: All chapters (comprehensive)

---

## Part 3: Placement and Numbering Scheme

### Preserved Numbering with Decimal Extensions

**Current Structure**: 74 total sections (12 chapters with subsections)
**Proposed Structure**: 90 total sections (+16 additions, +21.6%)

**Numbering Strategy**:
- Main chapters: 1-12 (unchanged)
- New chapter: 13 (Glossary)
- Subsections: Use decimal extensions to maintain continuity

### Detailed Placement Map

```
1. Introduction & Theoretical Foundations
   [UNCHANGED - 2 subsections]

2. Camera-Specific Color Science
   2.1 ARRI Cameras (ALEXA 35, ALEXA LF) [EXISTING]
   2.1.1 ARRI REVEAL Color Science Deep Dive [NEW - Subsection addition]
   2.2 Sony Cameras (VENICE, VENICE 2, BURANO) [EXISTING]
   2.3 RED Cameras (V-RAPTOR, DSMC2 lineup) [EXISTING]
   2.4 Blackmagic Cinema Cameras [NEW - Critical]

3. Logarithmic & RAW Recording
   [UNCHANGED - 3 subsections]

4. LUTs (Lookup Tables) and Color Transforms
   [EXISTING 4.1-4.3 UNCHANGED]
   4.4 Converting to Standardized Color Spaces [EXISTING]
   4.5 Gamut Mapping and Tone Mapping Operators [NEW - Important]

5. ACES (Academy Color Encoding System)
   [EXISTING 5.1-5.3 UNCHANGED]
   5.4 ACES 2.0 and Next-Generation Workflows [NEW - Critical]

6. HDR (High Dynamic Range) Workflows
   [EXISTING 6.1-6.4 UNCHANGED]
   6.5 Dynamic HDR Formats (HDR10+ and SL-HDR) [NEW - Critical]
   6.6 HLG Production and Broadcast Workflows [NEW - Important]

7. On-Set Workflows & Live Grading
   [EXISTING 7.1-7.5 UNCHANGED]
   7.6 Virtual Production and LED Volume Color Pipelines [NEW - Critical]
   7.7 Color Metadata Management and Propagation [NEW - Important]

8. Codecs & Data Management
   [EXISTING 8.1-8.4 UNCHANGED]
   8.5 Emerging Codecs (AV1, JPEG XS, H.266/VVC) [NEW - Critical]

9. Display & Projection
   [EXISTING 9.1-9.4 UNCHANGED]
   9.5 IMF (Interoperable Master Format) Workflows [NEW - Critical]
   9.6 Consumer Display Calibration Considerations [NEW - Nice-to-Have]

10. Real-World Workflow Examples
   [EXISTING 10.1-10.4 UNCHANGED]
   10.5 Remote Grading and Cloud Collaboration [NEW - Critical]

11. Mathematical Appendix & Diagrams
   [EXISTING 11.1-11.4 UNCHANGED]
   11.5 Advanced Color Science (JzAzBz, ICtCp, CAT16) [NEW - Critical]
   11.6 Test Patterns and Validation Procedures [NEW - Important]

12. Conclusion & Best Practices
   [EXISTING 12.1-12.3 UNCHANGED]
   12.4 Display Characterization and 3D LUT Profiling [NEW - Critical]

13. Glossary and Definitions [NEW CHAPTER - Nice-to-Have]
    13.1 Comprehensive Terminology Reference [NEW - Nice-to-Have]
```

---

## Part 4: Content Depth and Writing Standards

### Depth Per Section (Word Counts)

| Priority Level | Sections | Avg. Words/Section | Total Words |
|----------------|----------|-------------------|-------------|
| Critical | 9 | 4,200 | 37,800 |
| Important | 5 | 3,280 | 16,400 |
| Nice-to-Have | 2 | 2,400 | 4,800 |
| **TOTAL** | **16** | **3,688** | **59,000** |

**Current Document Estimate**: ~140,000 words
**Projected Document with Additions**: ~199,000 words (+42% content growth)
**TOC Growth**: +21.6% (74 → 90 sections)
**Content-to-TOC Ratio**: 2,211 words/section (healthy balance)

### Writing Standards (Per update.md Requirements)

#### Each Section Must Include:
1. **Theory** (30%)
   - Key equations (OETF/EOTF, log encoding, exposure relationships)
   - Precise definitions with inline explanations
   - Standards references (SMPTE ST ####, ITU-R BT.####, ACES v#.#)

2. **Practice** (40%)
   - Concrete workflows (Resolve/Baselight/Livegrade/ACES/OCIO)
   - Specific settings and parameter values
   - Decision criteria (when to use X vs. Y)
   - Validation methods (test patterns, measurement tools)

3. **Failure Modes & Traps** (20%)
   - Common breakpoints (clipping vs. compression)
   - Wrong transform selection (IDT/ODT mismatches)
   - "Double transforms" and monitoring chain errors
   - Legal/full range issues
   - HDR metadata mismatches

4. **Mini Glossary** (10%)
   - Up to 6 tight definitions per section
   - Terms first-used inline with square bracket definitions
   - Cross-references to other sections

### Inline Definition Format

**Example**: "JzAzBz [a perceptual uniform color appearance space developed by Zhou et al. to overcome limitations in CIELAB for HDR and wide-gamut color stimuli, enabling accurate ΔE measurements for modern displays]"

**First-Mention Rule**: Every technical term must be inline-defined at first appearance in the document, with square bracket format including:
- What it is (category)
- Who developed it (if applicable)
- What problem it solves
- Why it matters operationally

### Standards Reference Format

**Required Elements**:
- Document name (e.g., "SMPTE ST 2084:2014")
- Version/date (e.g., "SMPTE ST 2094-40:2016")
- One-line operational impact (e.g., "defines dynamic metadata structure for HDR10+")
- Verification marker if uncertain: "(verify version/date)"

**Example**:
> "HDR10+ uses dynamic metadata defined in SMPTE ST 2094-40:2016 (Application #4 of Dynamic Metadata), which enables scene-by-scene tone mapping adjustments transmitted alongside the video essence (verify current revision)."

---

## Part 5: Priority Ranking and Implementation Order

### Phase 1: Critical Foundation (First 4 sections)
**Timeline**: Immediate (addresses current production gaps)

1. **Section 5.4 ACES 2.0** - Industry transition active; all colorists need updated knowledge
2. **Section 2.4 Blackmagic Cameras** - Missing major camera manufacturer; mid-tier productions depend on this
3. **Section 7.6 Virtual Production** - High-growth workflow; technical gaps causing production failures
4. **Section 9.5 IMF Workflows** - Streaming platform requirements; delivery rejections occurring

### Phase 2: Workflow Modernization (Next 3 sections)
**Timeline**: Short-term (emerging industry standards)

5. **Section 6.5 Dynamic HDR Formats** - HDR10+ and SL-HDR adoption accelerating
6. **Section 8.5 Emerging Codecs** - AV1 and JPEG XS entering production pipelines
7. **Section 10.5 Remote Grading** - Remote workflows now standard; COVID-19 permanent shift

### Phase 3: Advanced Technical Depth (Next 4 sections)
**Timeline**: Medium-term (specialist knowledge)

8. **Section 11.5 Advanced Color Science** - JzAzBz/ICtCp/CAT16 required for modern HDR assessment
9. **Section 12.4 Display Characterization** - Custom 3D LUT creation increasingly necessary
10. **Section 4.5 Gamut Mapping Operators** - HDR→SDR delivery quality depends on this
11. **Section 7.7 Color Metadata Management** - Pipeline integration and conform efficiency
12. **Section 11.6 Test Patterns and Validation** - QC standardization needs

### Phase 4: Refinement and Usability (Last 5 sections)
**Timeline**: Long-term (completion and polish)

13. **Section 6.6 HLG Production** - Broadcast-specific workflows
14. **Section 2.1.1 ARRI REVEAL** - Deep dive into major color science upgrade
15. **Section 9.6 Consumer Display Calibration** - Final review considerations
16. **Section 13 Glossary** - Usability and reference
17. **Section 13.1 Comprehensive Terminology** - Complete glossary

---

## Part 6: Risk Assessment

### High-Risk Gaps (Immediate Attention Required)

1. **ACES 2.0 Transition** (Section 5.4)
   - **Risk**: Colorists using deprecated ACES 1.x workflows; incompatibility with new IDTs
   - **Mitigation**: Priority #1 writing; include migration guide

2. **IMF Delivery Failures** (Section 9.5)
   - **Risk**: Technical rejections from streaming platforms; expensive re-delivery
   - **Mitigation**: Priority #4 writing; include QC checklist

3. **Virtual Production Color Mismatches** (Section 7.6)
   - **Risk**: LED wall color vs. camera capture misalignment; expensive VFX fixes
   - **Mitigation**: Priority #3 writing; include real-world case studies

### Medium-Risk Gaps (Short-Term Attention)

4. **Dynamic HDR Format Misunderstanding** (Section 6.5)
   - **Risk**: Suboptimal HDR10+/SL-HDR grades; lack of dynamic metadata utilization
   - **Mitigation**: Priority #5 writing; include tool-specific workflows

5. **Remote Grading Color Drift** (Section 10.5)
   - **Risk**: Color degradation over WAN; client trust issues
   - **Mitigation**: Priority #7 writing; include bandwidth calculations

### Low-Risk Gaps (Long-Term Attention)

6. **Advanced Color Science Knowledge Gap** (Section 11.5)
   - **Risk**: Slower adoption of perceptual metrics; reliance on legacy ΔE76
   - **Mitigation**: Priority #8 writing; include practical ΔEJz workflows

---

## Part 7: Alignment with Current Standards

### SMPTE Standards Coverage

| Standard | Current Coverage | Proposed Addition |
|----------|------------------|-------------------|
| ST 2084:2014 (PQ) | ✅ Section 6.1 | — |
| ST 2094-40:2016 (HDR10+) | ⚠️ Mentioned only | ✅ Section 6.5 |
| ST 2094-10:2016 (Dolby) | ⚠️ Mentioned only | ✅ Section 6.5 |
| ST 2067-xx (IMF) | ⚠️ Mentioned only | ✅ Section 9.5 |
| ST 2117-xx (JPEG XS) | ❌ Missing | ✅ Section 8.5 |
| ST 2124 (ICtCp) | ❌ Missing | ✅ Section 11.5 |
| ST 428-xx (DCP) | ✅ Section 9.4 | — |

### ITU-R Recommendations Coverage

| Recommendation | Current Coverage | Proposed Addition |
|----------------|------------------|-------------------|
| BT.2100 (HDR) | ✅ Section 6.1-6.2 | — |
| BT.1886 (SDR) | ✅ Section 1.2 | — |
| BT.2020 (UHDTV) | ✅ Section 9.2 | — |
| BT.2408 (HDR monitoring) | ⚠️ Partial | ✅ Section 7.6 (LED walls) |

### Academy/ACES Coverage

| Component | Current Coverage | Proposed Addition |
|-----------|------------------|-------------------|
| ACES 1.0/1.3 | ✅ Section 5.1-5.3 | — |
| ACES 2.0 | ❌ "In development" | ✅ Section 5.4 |
| ACEScct | ✅ Section 5.1 | — |
| ACEScg | ✅ Section 5.1 | — |
| AP0/AP1 primaries | ✅ Section 5.1 | — |

### EBU Standards Coverage

| Standard | Current Coverage | Proposed Addition |
|----------|------------------|-------------------|
| Tech 3328 (SL-HDR) | ❌ Missing | ✅ Section 6.5 |
| R128 (Loudness) | ❌ Out of scope | — |
| Tech 3325 (HLG) | ✅ Section 6.1 | ✅ Section 6.6 (production) |

---

## Part 8: Resource Requirements

### Subject Matter Expertise Needed

1. **ACES 2.0**: Academy-approved documentation and early adopter case studies
2. **Virtual Production**: Unreal Engine/nDisplay documentation, LED wall manufacturers (ROE, Samsung)
3. **IMF Workflows**: Netflix/Apple technical specifications, mastering facility SOPs
4. **Advanced Color Science**: Zhou et al. papers (JzAzBz), ITU-R BT.2100 annexes (ICtCp)
5. **Remote Grading**: Platform documentation (Evercast, Frame.io), facility case studies

### Research Sources Required

**Primary Sources**:
- SMPTE standards documents (official access required)
- Academy ACES documentation (acescentral.com)
- ITU-R recommendations (free access)
- EBU technical reviews (member access)

**Secondary Sources**:
- Manufacturer white papers (ARRI REVEAL, Sony VENICE 2, RED)
- Platform delivery specifications (Netflix, Disney+, Apple TV+)
- Open source documentation (OpenColorIO, CTL, aces-dev)

**Tertiary Sources**:
- Post-production facility SOPs (anonymous, where possible)
- Trade publications (Digital Cinema Report, FilmLight White Papers)
- Academic papers (color science journals)

---

## Part 9: Validation and Review Strategy

### Expert Review Required

Each proposed section should be reviewed by:

1. **Section 5.4 (ACES 2.0)**: Academy ACES committee member or ACES-approved trainer
2. **Section 7.6 (Virtual Production)**: Virtual production supervisor or experienced VP colorist
3. **Section 9.5 (IMF)**: Deliveries specialist at major post facility or streaming platform QC lead
4. **Section 11.5 (Advanced Color Science)**: Color scientist or researcher with publications in JzAzBz/ICtCp

### Technical Validation Checklist

For each new section:
- [ ] All equations verified against primary sources (standards documents)
- [ ] All workflow steps tested in actual software (Resolve/Baselight/etc.)
- [ ] All standards references include version/date
- [ ] All inline definitions are precise and operationally useful
- [ ] All failure modes are documented with mitigation strategies
- [ ] All test patterns/procedures are reproducible

### Peer Review Process

1. **Draft Review**: Technical accuracy check by subject matter expert
2. **Production Review**: Workflow validation by practicing DIT/colorist
3. **Standards Review**: Compliance check against SMPTE/ITU/Academy specs
4. **Final Review**: Language and clarity check by technical editor

---

## Part 10: Conclusion and Recommendations

### Summary

This proposal identifies **16 targeted additions** (+21.6% TOC growth) addressing critical gaps in:
- Contemporary camera systems (Blackmagic)
- Next-generation color management (ACES 2.0)
- Modern HDR formats (HDR10+, SL-HDR)
- Emerging workflows (virtual production, remote grading, IMF)
- Advanced color science (JzAzBz, ICtCp, CAT16)
- Future-proofing (AV1, JPEG XS, H.266)

### Priority Recommendations

**Immediate Action (First 3 sections)**:
1. **Section 5.4 ACES 2.0** - Industry transition active; highest production impact
2. **Section 2.4 Blackmagic Cameras** - Missing major manufacturer; common in productions
3. **Section 7.6 Virtual Production** - High-growth area; technical complexity high

**Short-Term Action (Next 3 sections)**:
4. **Section 9.5 IMF Workflows** - Streaming requirements; delivery risk
5. **Section 6.5 Dynamic HDR** - Emerging format; creative tooling gaps
6. **Section 10.5 Remote Grading** - Industry standard now; COVID legacy

### Success Criteria

The TOC expansion will be successful if:
- ✅ All critical gaps (Priority #1-4) are addressed within 6 months
- ✅ All sections include inline definitions, failure modes, and validation procedures
- ✅ All standards references are verified and versioned
- ✅ All workflows are tested in actual production software
- ✅ Document growth remains ≤25% TOC increase (target: +21.6%)

### Next Steps

1. **Stakeholder Review**: Circulate this proposal to practicing DITs, colorists, and color scientists for feedback
2. **Priority Validation**: Confirm priority ranking with production professionals
3. **Resource Assessment**: Identify subject matter experts for each proposed section
4. **Phased Implementation**: Begin with Phase 1 (Critical Foundation) sections
5. **Continuous Validation**: Establish review checkpoints after each section completion

---

**Document Status**: Proposal - Pending Review
**Next Review Date**: 2026-02-01
**Responsible Analyst**: Hive Mind Collective - Analyst Agent
**Approval Required**: Project Lead, Technical Advisory Board

---

## Appendix A: Quick Reference Table

| Section # | Title | Priority | Est. Words | Dependencies | Risk Level |
|-----------|-------|----------|------------|--------------|------------|
| 2.4 | Blackmagic Cameras | Critical | 3,500 | None | High |
| 2.1.1 | ARRI REVEAL Deep Dive | Important | 2,800 | 2.1 | Medium |
| 4.5 | Gamut Mapping Operators | Important | 3,600 | 4.4 | Medium |
| 5.4 | ACES 2.0 | Critical | 4,200 | 5.1, 5.3 | High |
| 6.5 | Dynamic HDR Formats | Critical | 3,800 | 6.1, 6.2 | High |
| 6.6 | HLG Production | Important | 3,400 | 6.1 | Medium |
| 7.6 | Virtual Production | Critical | 5,500 | 7.2, 6.x | Critical |
| 7.7 | Color Metadata Management | Important | 3,100 | 7.4, 10.x | Medium |
| 8.5 | Emerging Codecs | Critical | 3,200 | 8.1 | High |
| 9.5 | IMF Workflows | Critical | 4,800 | 9.4 | High |
| 9.6 | Consumer Display Calibration | Nice-to-Have | 2,600 | 9.1, 9.4 | Low |
| 10.5 | Remote Grading | Critical | 4,100 | 7.3, 10.x | High |
| 11.5 | Advanced Color Science | Critical | 4,300 | 1.1, 11.1 | Medium |
| 11.6 | Test Patterns & Validation | Important | 3,300 | 11.1, 11.5 | Medium |
| 12.4 | Display Characterization | Critical | 3,900 | 7.2, 9.1 | Medium |
| 13.1 | Glossary | Nice-to-Have | 2,200 | All | Low |

**Legend**:
- **Critical**: Industry transition active or production-blocking gap
- **Important**: Emerging standard or workflow optimization
- **Nice-to-Have**: Usability improvement or reference enhancement

---

## Appendix B: Kierunki rozwojowe (burza mózgów)

1. **Normalizacja metadanych kamerowych między producentami**
   - **Tytuł roboczy:** Normalizacja metadanych kamerowych między producentami
   - **Opis:** Zdefiniowanie wspólnego schematu metadanych (timecode, ISO, WB, T-stop, LUT/CDL) dla ARRI/Sony/RED/Blackmagic. Ułatwia to automatyczne mapowanie do narzędzi edytorskich i gradingowych bez ręcznej korekty. Zakłada się mapy translacyjne oraz minimalny zestaw pól krytycznych.
   - **Dlaczego istotne dla high-end:** W produkcjach premium różne kamery i jednostki często współistnieją, a brak spójnego schematu zwiększa ryzyko błędów konformu.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak standardu wymiany metadanych między vendorami i narzędziami post.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: słownik pól + mapy → tool: walidator i mapper metadanych → platforma/standard: wspólny schemat branżowy.
2. **Rejestr decyzji kolorystycznych (LUT/CDL/grades) z wersjonowaniem**
   - **Tytuł roboczy:** Rejestr decyzji kolorystycznych (LUT/CDL/grades) z wersjonowaniem
   - **Opis:** Ujednolicony rejestr decyzji kolorystycznych przypisanych do ujęć, scen i wersji montażowych. Umożliwia śledzenie zmian, odtwarzanie poprzednich stanów i automatyczne przenoszenie decyzji między etapami.
   - **Dlaczego istotne dla high-end:** Złożone show wymagają audytowalnej historii decyzji kolorystycznych, zwłaszcza przy wieloosobowych zespołach i długich harmonogramach.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak spójnego mechanizmu wersjonowania LUT/CDL między DIT, editorial i grading.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: standard nazewnictwa + rejestr CSV → tool: repozytorium z API → platforma/standard: branżowy rejestr decyzji kolorystycznych.
3. **Spektralne profilowanie LED volume i dopasowanie do kamer**
   - **Tytuł roboczy:** Spektralne profilowanie LED volume i dopasowanie do kamer
   - **Opis:** Procedury pomiaru spektralnego LED wall, kalibracji i korelacji z charakterystyką sensorów. Uwzględnia korekty metamerii oraz wpływ spektrum na skintony i kluczowe barwy.
   - **Dlaczego istotne dla high-end:** Virtual production na poziomie premium wymaga powtarzalnej zgodności koloru między planem a finalnym renderem.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Niedostateczne narzędzia do korelacji spektralnej LED ↔ kamera w praktyce produkcyjnej.
   - **Poziom zaawansowania:** Expert
   - **Potencjał rozwoju:** MVP: checklisty pomiarowe → tool: profilator spektralny z raportem → platforma/standard: procedura certyfikacji LED volume.
4. **Automatyczny QC dla dual-master HDR/SDR**
   - **Tytuł roboczy:** Automatyczny QC dla dual-master HDR/SDR
   - **Opis:** System weryfikacji zgodności wersji HDR i SDR z użyciem metryk percepcyjnych (ΔEITP/ΔEJz) oraz testów tone mappingu. Wyniki raportowane per-sekwencja z progami akceptacji.
   - **Dlaczego istotne dla high-end:** Dla premium deliverables wymagane są powtarzalne, audytowalne kryteria jakości.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak obiektywnego, zautomatyzowanego QC dla wersji HDR/SDR w pipeline.
   - **Poziom zaawansowania:** Expert
   - **Potencjał rozwoju:** MVP: zestaw testów i progów → tool: automatyczny QC z raportem → platforma/standard: wspólny benchmark zgodności HDR/SDR.
5. **Kontrola integralności danych od planu do archiwum**
   - **Tytuł roboczy:** Kontrola integralności danych od planu do archiwum
   - **Opis:** Wprowadzenie jednoznacznego łańcucha kontroli (checksum, manifesty, podpisy) dla materiału kamerowego i transkodów. System raportuje braki, uszkodzenia i niezgodności podczas każdego transferu.
   - **Dlaczego istotne dla high-end:** Utrata lub uszkodzenie danych w wysokobudżetowych projektach generuje kosztowne przeróbki i ryzyko prawne.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Rozproszone i niestandardowe praktyki weryfikacji integralności danych.
   - **Poziom zaawansowania:** Pro
   - **Potencjał rozwoju:** MVP: checklisty i skrypty checksum → tool: konsola weryfikacji transferów → platforma/standard: jednolity łańcuch custody dla postprodukcji.
6. **Modelowanie przepustowości danych dla 8K/12K**
   - **Tytuł roboczy:** Modelowanie przepustowości danych dla 8K/12K
   - **Opis:** Metody prognozowania obciążenia sieci, storage i CPU/GPU w zależności od kodeków i rozdzielczości. Pozwala to projektować pipeline bez wąskich gardeł i planować inwestycje.
   - **Dlaczego istotne dla high-end:** Produkcje premium pracują na wysokich bitratach, a brak planowania przepustowości generuje przestoje.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak ujednoliconego modelu kosztu danych i przepustowości dla kinowych formatów.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: kalkulator w arkuszu → tool: symulator pipeline → platforma/standard: planowanie zasobów dla facility.
7. **Spójny pipeline dostaw IMF/DCP/streaming**
   - **Tytuł roboczy:** Spójny pipeline dostaw IMF/DCP/streaming
   - **Opis:** Moduł opisujący jeden model danych dla równoległych deliverables, z kontrolą transformat i metadanych. Zakłada mapowanie wspólnego mastera na różne specyfikacje odbiorców.
   - **Dlaczego istotne dla high-end:** Duże projekty wymagają równoległych dostaw do kin i platform, bez rozjechania intencji twórczej.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Rozdzielne, niespójne procesy dostaw dla IMF, DCP i streaming.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: macierz wymagań deliverables → tool: generator pakietów z walidacją → platforma/standard: wspólna specyfikacja produkcyjna.
8. **Round-trip VFX z kontrolą koloru i metadanych**
   - **Tytuł roboczy:** Round-trip VFX z kontrolą koloru i metadanych
   - **Opis:** Procedury wymiany materiałów między postprodukcyjnym gradingiem a VFX z pełnym śledzeniem ACES i metadanych. Obejmuje walidację przestrzeni barwnej, kluczowych atrybutów i wersji.
   - **Dlaczego istotne dla high-end:** Projekty VFX-heavy wymagają precyzyjnego zachowania referencji kolorystycznych.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak spójnych zasad round-trip VFX z perspektywy color management.
   - **Poziom zaawansowania:** Expert
   - **Potencjał rozwoju:** MVP: checklista wymiany → tool: walidator paczek VFX → platforma/standard: standard wymiany dla facility i vendorów.
9. **Predykcja ryzyka bandingu i artefaktów kompresji w HDR**
   - **Tytuł roboczy:** Predykcja ryzyka bandingu i artefaktów kompresji w HDR
   - **Opis:** Analiza materiału pod kątem wrażliwych gradientów i zakresów luminancji dla wybranych kodeków. Wynikiem są rekomendacje ustawień kodowania oraz alerty dla sekcji krytycznych.
   - **Dlaczego istotne dla high-end:** Jakość HDR w dystrybucji premium jest szczególnie podatna na degradację w cieniach i średnich tonach.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak narzędzi predykcyjnych dla artefaktów HDR w procesie masteringu.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: heurystyki i checklisty → tool: analizator ryzyka → platforma/standard: wspólny benchmark ryzyka kompresji.
10. **KPI spójności kolorystycznej między etapami produkcji**
   - **Tytuł roboczy:** KPI spójności kolorystycznej między etapami produkcji
   - **Opis:** Zestaw mierników spójności barwnej pomiędzy planem, dailies, offline i gradingiem finalnym. Raporty per etap wskazują odchylenia i ich źródło.
   - **Dlaczego istotne dla high-end:** Ułatwia zarządzanie jakością i minimalizuje kosztowne iteracje kreatywne.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak metryk pozwalających obiektywnie ocenić spójność koloru w pipeline.
   - **Poziom zaawansowania:** Pro
   - **Potencjał rozwoju:** MVP: podstawowy zestaw KPI → tool: panel raportowy → platforma/standard: branżowy standard raportowania.
11. **Automatyzacja dailies z kontrolą tone mappingu i gamut mappingu**
   - **Tytuł roboczy:** Automatyzacja dailies z kontrolą tone mappingu i gamut mappingu
   - **Opis:** Standardowe presety dla dailies z kontrolą transformacji dla różnych docelowych przestrzeni i monitorów. Uwzględnia alerty dla przekroczeń gamutowych oraz spójność z finalnym gradingiem.
   - **Dlaczego istotne dla high-end:** Dailies muszą odzwierciedlać intencję kreatywną bez zafałszowań wynikających z automatycznych transformacji.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak kontrolowanych, powtarzalnych ustawień dailies dla wielu odbiorców.
   - **Poziom zaawansowania:** Advanced
   - **Potencjał rozwoju:** MVP: zestaw presetów i reguł → tool: automatyczny generator dailies → platforma/standard: biblioteka referencyjna dla facility.
12. **Benchmarking monitorów i projektorów HDR/SDR w realnych warunkach**
   - **Tytuł roboczy:** Benchmarking monitorów i projektorów HDR/SDR w realnych warunkach
   - **Opis:** Metodyka porównawcza urządzeń referencyjnych i klienckich, uwzględniająca stabilność, dryft i zgodność z docelową krzywą. Raporty porównawcze wspierają decyzje zakupowe i walidację.
   - **Dlaczego istotne dla high-end:** Dobór monitorów referencyjnych determinuje wiarygodność całego procesu kolorystycznego.
   - **Jaką lukę rynkową/workflow rozwiązuje:** Brak praktycznych benchmarków obejmujących realne warunki pracy i długoterminową stabilność.
   - **Poziom zaawansowania:** Pro
   - **Potencjał rozwoju:** MVP: metodologia pomiarów → tool: zestaw testów i raportów → platforma/standard: baza benchmarków branżowych.

---

**END OF PROPOSAL**
