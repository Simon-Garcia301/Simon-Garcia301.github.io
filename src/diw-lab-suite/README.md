# DIW Lab Suite ⚙🔬📊

**Digital Ink Writing — Scientific Toolchain for Advanced Manufacturing Research**

The DIW Lab Suite is a unified desktop application toolkit that streamlines three core workflows in Digital Ink Writing (DIW) research laboratories: **G-Code toolpath visualization**, **automated line width microscopy analysis**, and **reflectance-based surface roughness profiling**. Built for the Lee Research Group at the University of St. Thomas, this suite replaces manual, error-prone, multi-tool workflows with integrated, automated, and scientifically rigorous analysis pipelines.

---

## Table of Contents

- [Overview](#overview)
- [Applications](#applications)
    - [1. G-Code Converter & Visualizer](#1-g-code-converter--visualizer)
    - [2. Line Width Image Analysis](#2-line-width-image-analysis)
    - [3. Surface Roughness Analysis](#3-surface-roughness-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Use Cases](#use-cases)
- [Value Proposition](#value-proposition)
- [Project Structure](#project-structure)
- [License & Attribution](#license--attribution)

---

## Overview

DIW (Digital Ink Writing) is an extrusion-based additive manufacturing technique used to print functional inks — conductive, dielectric, biological, or structural — onto substrates via a precision nozzle mounted on a multi-axis motion stage. Quality assurance in DIW research requires analysis at multiple stages of the print workflow:

1. **Pre-print:** Verify the G-Code toolpath for layer correctness, print order, and bed alignment.
2. **Post-print:** Measure printed line widths under microscope to assess dimensional accuracy and consistency.
3. **Surface quality:** Evaluate surface roughness via coaxial reflectance imaging to quantify print quality.

The DIW Lab Suite integrates all three stages into a single, consistent interface — eliminating context switching between separate tools, standardizing analysis parameters, and producing publication-ready outputs.

---

## Applications

### 1. G-Code Converter & Visualizer

**Purpose:** Convert Aerotech G-Code (AeroScript) files into high-resolution PNG renderings with interactive 2D/3D toolpath inspection.

**How it works:**
- Reads Aerotech G-Code / AeroScript files with full support for G0 (rapid travel), G1 (linear print), G2/G3 (arc interpolation), variables, expressions, and comments.
- Parses the file into discrete layers grouped by Z-height, intelligently merging layers when the count exceeds 20 for readability.
- Renders a publication-quality PNG with a dark-themed scientific palette: travel moves as dashed gray lines, print moves as a plasma-colormap gradient from start (green) to finish (red).
- Displays an interactive matplotlib preview with three view modes:
    - **2D Top:** Orthographic top-down view of the selected layer.
    - **3D Interactive:** Rotatable 3D view of the selected layer at its Z-height.
    - **3D All Layers:** Full stacked 3D view of every layer, color-coded by layer index.
- Supports optional printer bed boundary overlay, drag-and-drop file loading, and snapshot export.

**Tech stack:** Python, tkinter/ttkbootstrap, matplotlib, NumPy, Pillow, tkinterdnd2.

---

### 2. Line Width Image Analysis

**Purpose:** Automated measurement of printed line width, edge profile tracking, and coefficient of variation (CV%) from microscope image scans.

**How it works:**
- Loads one or more overlapping microscope images (PNG, JPEG, TIFF, BMP) of a printed DIW line.
- Performs adaptive Otsu thresholding (or manual threshold) to segment the printed line from the substrate.
- Uses a tracking-window edge detection algorithm that follows the line's centerline row by row, computing left and right edge positions.
- Reports both classic and robust CV% (using Median Absolute Deviation) for resistance to outliers.
- Stitches overlapping frames with overlap-aware alignment for continuous profiles across image boundaries.
- Generates visual QA overlays showing detected edge positions, with navigation buttons to cycle through all input images.
- Outputs: width-vs-position CSV profile, per-image QA overlay PNGs, aggregate statistics.

**Tech stack:** Python, OpenCV, NumPy, matplotlib, scikit-image, SciPy, ttkbootstrap.

---

### 3. Surface Roughness Analysis

**Purpose:** Reflectance-based surface roughness (CV%) quantification using 5x coaxial illumination microscope images with self-calibrating flat-field correction.

**How it works:**
- Loads multiple microscope images captured with a 5x coaxial (through-the-lens) illumination objective. The 4x backlight objective is explicitly blocked as incompatible.
- Provides an interactive ROI rectangle selector and glare-exclusion polygon tool drawn directly on the preview image.
- Applies a novel self-calibrating flat-field correction algorithm: the sample region is inpainted out of the image, the remaining field is heavily blurred to estimate the optical vignetting profile, and the raw image is normalized by this profile — eliminating the need for a separate calibration reference image.
- Masks user-drawn glare polygons and intensity-capped pixels from statistical computation.
- Computes per-image and aggregate mean CV%, standard deviation, and pixel count, displayed in both GUI and histogram views.
- Outputs: CSV summary with per-image metrics, lens metadata, and scale calibration.

**Tech stack:** Python, OpenCV, NumPy, matplotlib, SciPy, ttkbootstrap.

---

## Installation

### Prerequisites

- Python 3.10+
- Windows 10/11 (primary target; macOS/Linux compatible with minor Tkinter adjustments)

### Dependencies

```bash
pip install ttkbootstrap matplotlib opencv-python numpy
```

Optional but recommended:

```bash
pip install scipy scikit-image pillow tkinterdnd2
```

### Clone & Run

```bash
git clone <repository-url> diw-lab-suite
cd diw-lab-suite

# Launch the launcher menu
python apps/gcode-converter/main.py
```

To run a specific tool standalone:

```bash
# G-Code Converter
python -c "import sys; sys.path.insert(0, 'apps/gcode-converter'); from gui.gcode_converter_gui import build_gui; build_gui().mainloop()"

# Line Width Analysis
python -c "import sys; sys.path.insert(0, 'apps/gcode-converter'); from gui.image_analysis_gui import build_image_analysis_gui; build_image_analysis_gui().mainloop()"

# Surface Roughness Analysis
python -c "import sys; sys.path.insert(0, 'apps/gcode-converter'); from gui.surface_roughness_gui import build_surface_roughness_gui; build_surface_roughness_gui().mainloop()"
```

### Building a Standalone Executable

```bash
cd apps/gcode-converter
pip install pyinstaller
pyinstaller lee_tool_suite.spec --additional-hooks-dir=.
```

---

## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **GUI Framework** | ttkbootstrap (v3+) | Modern dark-themed Tkinter widget library |
| **Plotting** | matplotlib 3.x | 2D/3D toolpath visualization, QA overlays, histograms |
| **Image Processing** | OpenCV 4.x | Edge detection, morphological operations, flat-field correction |
| **Numerical** | NumPy 1.x | Array operations, statistics, linear algebra |
| **Scientific** | SciPy, scikit-image | Additional filtering, interpolation, image metrics |
| **Packaging** | PyInstaller 6.x | Standalone .exe bundling with custom hooks |
| **Drag & Drop** | tkinterdnd2 | File drag-and-drop support for G-Code import |

---

## Use Cases

### Research Lab Workflow

1. **Design → Simulate → Print:** A researcher designs a DIW pattern in CAD, generates AeroScript G-Code, and opens it in the G-Code Converter to verify the toolpath before committing ink to substrate.
2. **Inspect → Measure → Quantify:** After printing, the researcher places the substrate under the 5x coaxial microscope, captures images of printed lines, and runs Line Width Analysis to measure line consistency (target CV% < 5%).
3. **Surface Quality → Validate:** The same microscope images are run through Surface Roughness Analysis to quantify print surface quality, ensuring the printed structure meets the experimental specification.

### Batch Processing

A researcher processing a 96-sample experiment can batch-analyze all microscope images through the Line Width pipeline, producing a single merged CSV with per-sample CV% metrics — turning hours of manual measurement into minutes of automated analysis.

### Quality Control

A production DIW line operator can use the G-Code Converter to do a quick pre-print toolpath sanity check, then validate post-print quality with the two analysis modules, all from a single launch menu.

---

## Value Proposition

### Before DIW Lab Suite

- ❌ G-Code viewed in text editors — no visual toolpath verification.
- ❌ Line width measured manually with digital calipers on a screen — slow, inconsistent, subject to operator bias.
- ❌ Surface roughness assessed qualitatively by eye.
- ❌ Data scattered across CSV files, screenshots, and lab notebooks.
- ❌ Different tools for each analysis stage with incompatible workflows.

### After DIW Lab Suite

- ✅ Interactive 2D/3D toolpath preview with layer-by-layer inspection.
- ✅ Automated edge detection with adaptive thresholding — consistent, unbiased, scalable.
- ✅ Quantitative surface roughness CV% with optical vignetting correction.
- ✅ Unified interface, shared calibration constants, consistent output formats.
- ✅ Publication-ready PNGs, CSVs, and QA overlays generated in seconds.

---

## Project Structure

```
diw-lab-suite/
├── README.md
├── PRODUCT_SHOWCASE.md
├── apps/
│   ├── gcode-converter/          ← Primary application package
│   │   ├── main.py               ← Launcher menu
│   │   ├── gui/                  ← GUI layer (tkinter windows)
│   │   │   ├── gcode_converter_gui.py
│   │   │   ├── image_analysis_gui.py
│   │   │   └── surface_roughness_gui.py
│   │   ├── engines/              ← Engine layer (computation)
│   │   │   ├── gcode_engine.py
│   │   │   ├── line_width_engine.py
│   │   │   └── surface_roughness_engine.py
│   │   └── shared/               ← Shared UI components
│   │       └── ui_common.py
│   ├── line-width-analysis/      ← Standalone app (junction to gcode-converter)
│   └── surface-roughness/        ← Standalone app (junction to gcode-converter)
└── docs/
    └── architecture.md
```

---

## License & Attribution

**DIW Lab Suite** is developed for the **Lee Research Group** at the **University of St. Thomas**.

© Lee Research Group — University of St. Thomas. All rights reserved.

Version 4.0.0

---

*Built with Python, open-source scientific libraries, and a commitment to reproducible research workflows.*