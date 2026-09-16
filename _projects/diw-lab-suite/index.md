---
layout: post
title: "DIW Lab Suite — Digital Ink Writing Research Tools"
description: Desktop application toolkit for DIW research labs — G-Code toolpath visualization, automated line width microscopy analysis, and reflectance-based surface roughness profiling. Built for the Lee Research Group at the University of St. Thomas.
skills: 
  - Digital Ink Writing (DIW)
  - G-Code / AeroScript parsing
  - Microscope image analysis (OpenCV, Edge detection)
  - Surface roughness quantification (flat-field correction)
  - Python (tkinter/ttkbootstrap, matplotlib, OpenCV, NumPy)
  - PyInstaller packaging

main-image: /diw-suite-showcase.png
---

## Overview

The **DIW Lab Suite** is a unified desktop application toolkit that streamlines three core workflows in Digital Ink Writing (DIW) research laboratories: **G-Code toolpath visualization**, **automated line width microscopy analysis**, and **reflectance-based surface roughness profiling**. It replaces manual, error-prone, multi-tool workflows with integrated, automated, and scientifically rigorous analysis pipelines — all under one consistent interface.

{% include image-gallery.html images="launcher-menu.png" %}

## Applications

### 1. G-Code Converter & Visualizer

Convert Aerotech G-Code / AeroScript files into high-resolution PNG renderings with interactive 2D/3D toolpath inspection. Features include:

- Full support for G0 (travel), G1 (linear print), G2/G3 (arc interpolation), variables, and expressions
- Layer-by-layer Z-height grouping with smart merging when counts exceed 20
- Interactive preview with 2D Top, 3D Interactive, and 3D All Layers view modes
- Plasma-colormap gradient rendering from print start (green) to finish (red)
- Drag-and-drop file loading, optional bed boundary overlay, snapshot export

### 2. Line Width Image Analysis

Automated measurement of printed line width, edge profile tracking, and coefficient of variation (CV%) from microscope image scans:

- Adaptive Otsu thresholding per image, or manual override
- Tracking-window edge detection algorithm that follows the line centerline row by row
- Classic CV% plus robust CV% (MAD-based) for outlier resistance
- Overlap-aware frame stitching with QA overlay cycling across images
- Per-row detection logs, batch QA summary reports

### 3. Surface Roughness Analysis

Reflectance-based surface roughness (CV%) quantification using 5x coaxial illumination images with self-calibrating flat-field correction:

- Novel self-calibrating vignetting correction — no reference image needed
- Interactive ROI rectangle selector and glare-exclusion polygon tool
- Lens enforcement (4x backlight explicitly blocked as incompatible)
- Per-image and aggregate mean CV%, std dev, pixel count
- Histogram view of corrected intensities

## Technology stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| GUI Framework | ttkbootstrap | Modern dark-themed Tkinter widgets |
| Plotting | matplotlib | 2D/3D toolpath visualization, histograms |
| Image Processing | OpenCV 4.x | Edge detection, flat-field correction |
| Numerical | NumPy, SciPy | Statistics, array operations |
| Packaging | PyInstaller | Standalone .exe bundle (~85 MB) |

## Before vs. after

| Aspect | Before (Manual) | After (DIW Lab Suite) |
|--------|----------------|----------------------|
| Toolpath inspection | Read raw text files | Interactive 2D/3D plots |
| Line width measurement | Manual cursor placement | Automated edge detection |
| Surface roughness | Qualitative ("looks smooth") | Quantitative CV% with optics correction |
| Multi-sample processing | Hours of manual work | Batch analysis, minutes |
| Output format | Scattered spreadsheets | Standardized CSV + PNG |

## Real lab workflow example

A researcher prints 24 silver-ink lines on glass at varying speeds. Pre-print, the G-Code Converter verifies the toolpath across all 8 layers. Post-print, the Line Width module processes 48 overlapping microscope images through adaptive Otsu thresholding and stitches them with overlap reconciliation. The Surface Roughness module applies flat-field correction and reports an overall mean CV of 3.2% — well within target. Total time: ~15 minutes vs. 3–4 hours manually.

## Architecture

The suite follows a modular **Engine-GUI Separation** architecture. Computational logic lives in pure-Python engine modules importable without Tkinter; GUI windows wire user interactions to these engines via background threads. All three apps share calibration constants (LENS_CALIBRATION_UM_PER_PX), theme palette, and widget factories from a common ui_common library.

Full architecture documentation and source code are available in the [src/diw-lab-suite/](../../src/diw-lab-suite/) directory.

## Installation

```bash
pip install ttkbootstrap matplotlib opencv-python numpy
pip install scipy scikit-image pillow tkinterdnd2

# Launch the launcher menu
python src/diw-lab-suite/gcode-converter/main.py
```

To build a standalone executable:
```bash
cd src/diw-lab-suite/gcode-converter
pyinstaller lee_tool_suite.spec --additional-hooks-dir=.
```

## Status

**Completed v4.0.0** — All three tools built, documented, packaged. Ready for lab deployment.
