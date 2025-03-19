# Digital Cinema Color Management: A Comprehensive Guide

## Introduction

This document provides a comprehensive guide to color management in digital cinema production. It covers the theoretical foundations of color science, practical workflows, and best practices for DITs (Digital Imaging Technicians), colorists, and other digital cinema professionals. The guide is structured into multiple chapters, each addressing a specific aspect of color management.

## Table of Contents

1.  **Introduction & Theoretical Foundations**
    *   [1.1 Basic Color Science](Digital_Cinema_Color_Management.md#11-basic-color-science)
    *   [1.2 Gamma, Gamut, and Logarithmic Encoding](Digital_Cinema_Color_Management.md#12-gamma-gamut-and-logarithmic-encoding)

2.  **Camera-Specific Color Science**
    *   [2.1 ARRI Cameras (ALEXA 35, ALEXA LF)](Digital_Cinema_Color_Management.md#21-arri-cameras-alexa-35-alexa-lf)
    *   [2.2 Sony Cameras (VENICE, VENICE 2, BURANO)](Digital_Cinema_Color_Management.md#22-sony-cameras-venice-venice-2-burano)
    *   [2.3 RED Cameras (V-RAPTOR, DSMC2 lineup)](Digital_Cinema_Color_Management.md#23-red-cameras-v-raptor-dsmc2-lineup)

3.  **Logarithmic & RAW Recording**
    *   [3.1 Mathematical Breakdown of Log Encodings](Digital_Cinema_Color_Management.md#31-mathematical-breakdown-of-log-encodings)
    *   [3.2 RAW Capture vs. Log Capture](Digital_Cinema_Color_Management.md#32-raw-capture-vs-log-capture)
    *   [3.3 Best Practices for Exposing Log and RAW](Digital_Cinema_Color_Management.md#33-best-practices-for-exposing-log-and-raw)

4.  **LUTs (Lookup Tables) and Color Transforms**
    *   [4.1 1D vs. 3D LUTs](Digital_Cinema_Color_Management.md#41-1d-vs-3d-luts)
    *   [4.2 Technical LUTs vs. Creative LUTs](Digital_Cinema_Color_Management.md#42-technical-luts-vs-creative-luts)
    *   [4.3 Color Management Pipelines & LUTs](Digital_Cinema_Color_Management.md#43-color-management-pipelines--luts)
    *   [4.4 Converting to Standardized Color Spaces](Digital_Cinema_Color_Management.md#44-converting-to-standardized-color-spaces)

5.  **ACES (Academy Color Encoding System)**
    *   [5.1 ACES Fundamentals](Digital_Cinema_Color_Management.md#51-aces-fundamentals)
    *   [5.2 ACES vs. Camera-Native Workflows](Digital_Cinema_Color_Management.md#52-aces-vs-camera-native-workflows)
    *   [5.3 Integrating ACES](Digital_Cinema_Color_Management.md#53-integrating-aces)

6.  **HDR (High Dynamic Range) Workflows**
    *   [6.1 PQ and HLG Fundamentals](Digital_Cinema_Color_Management.md#61-pq-and-hlg-fundamentals)
    *   [6.2 HDR Standards and Grading](Digital_Cinema_Color_Management.md#62-hdr-standards-and-grading)
    *   [6.3 Mapping to HDR](Digital_Cinema_Color_Management.md#63-mapping-to-hdr)
    *   [6.4 HDR Monitoring](Digital_Cinema_Color_Management.md#64-hdr-monitoring)

7.  **On-Set Workflows & Live Grading**
    *   [7.1 Hardware and Software](Digital_Cinema_Color_Management.md#71-hardware-and-software)
    *   [7.2 Setting up Reference Monitors](Digital_Cinema_Color_Management.md#72-setting-up-reference-monitors)
    *   [7.3 Wireless Video and Color Accuracy](Digital_Cinema_Color_Management.md#73-wireless-video-and-color-accuracy)
    *   [7.4 Creating On-Set LUTs/CDLs](Digital_Cinema_Color_Management.md#74-creating-on-set-lutscdls)
    *   [7.5 Maintaining Color Consistency](Digital_Cinema_Color_Management.md#75-maintaining-color-consistency)

8.  **Codecs & Data Management**
    *   [8.1 Overview of Major Codecs](Digital_Cinema_Color_Management.md#81-overview-of-major-codecs)
    *   [8.2 Bit-Depth, Chroma Subsampling, and Compression](Digital_Cinema_Color_Management.md#82-bit-depth-chroma-subsampling-and-compression)
    *   [8.3 Data Rates and Storage](Digital_Cinema_Color_Management.md#83-data-rates-and-storage)
    *   [8.4 Wrapping Codecs (Container Formats)](Digital_Cinema_Color_Management.md#84-wrapping-codecs-container-formats)

9.  **Display & Projection**
    *   [9.1 Monitoring Differences: On-Set, Post-Production, and Theatrical Projection](Digital_Cinema_Color_Management.md#91-monitoring-differences-on-set-post-production-and-theatrical-projection)
    *   [9.2 Standardized Color Spaces (Rec. 709, P3, Rec. 2020)](Digital_Cinema_Color_Management.md#92-standardized-color-spaces-rec-709-p3-rec-2020)
    *   [9.3 Display-Referred vs. Scene-Referred](Digital_Cinema_Color_Management.md#93-display-referred-vs-scene-referred)
    *   [9.4 Streaming Platforms and DCP](Digital_Cinema_Color_Management.md#94-streaming-platforms-and-dcp)

10. **Real-World Workflow Examples**
    *   [10.1 End-to-End Pipelines (ARRI, Sony, and RED)](Digital_Cinema_Color_Management.md#101-end-to-end-pipelines-arri-sony-and-red)
    *   [10.2 ACES in Resolve/Baselight](Digital_Cinema_Color_Management.md#102-aces-in-resolvebaselight)
    *   [10.3 Using On-Set LUTs in Editorial](Digital_Cinema_Color_Management.md#103-using-on-set-luts-in-editorial)
    *   [10.4 Archival and Versioning](Digital_Cinema_Color_Management.md#104-archival-and-versioning)

11. **Mathematical Appendix & Diagrams**
    *   [11.1 Formulas](Digital_Cinema_Color_Management.md#111-formulas)
    *   [11.2 Charts/Tables](Digital_Cinema_Color_Management.md#112-chartstables)
    *   [11.3 Block Diagrams](Digital_Cinema_Color_Management.md#113-block-diagrams)
    *   [11.4 References](Digital_Cinema_Color_Management.md#114-references)

12. **Conclusion & Best Practices**
    *   [12.1 Summary & Key Concepts for DITs and Colorists](Digital_Cinema_Color_Management.md#121-summary--key-concepts-for-dits-and-colorists)
    *   [12.2 Camera Comparisons: ARRI vs. Sony vs. RED (Color Science)](Digital_Cinema_Color_Management.md#122-camera-comparisons-arri-vs-sony-vs-red-color-science)
    *   [12.3 Recommended Practices Checklist](Digital_Cinema_Color_Management.md#123-recommended-practices-checklist)
