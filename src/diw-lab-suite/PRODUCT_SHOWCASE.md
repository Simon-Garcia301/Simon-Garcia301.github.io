# DIW Lab Suite — Product Showcase

## Product Information

| Attribute | Detail |
|-----------|--------|
| **Product Name** | DIW Lab Suite |
| **Version** | 4.0.0 |
| **Target Audience** | DIW research scientists, graduate students, process engineers, quality assurance technicians, and additive manufacturing labs |
| **Platform** | Windows 10/11 (primary), macOS/Linux (compatible) |
| **License** | Internal — Lee Research Group, University of St. Thomas |
| **Tech Stack** | Python, ttkbootstrap, matplotlib, OpenCV, NumPy, PyInstaller |

---

## Problem Statement

Digital Ink Writing (DIW) research laboratories face a fragmented ecosystem of analytical tools that slows down scientific discovery and introduces measurement variability:

### Manual Workflows
- **G-Code inspection** is done by reading raw text files — no visual verification of toolpaths, layer ordering, or print bed alignment before committing expensive ink to substrate.
- **Line width measurement** relies on manual cursor placement in image software (ImageJ, Photoshop) — operator-dependent, slow, and irreproducible across users or sessions.
- **Surface roughness assessment** is qualitative ("looks smooth") or requires expensive profilometry equipment that is not available in every lab.

### Data Fragmentation
- Measurements from each analysis stage live in different formats, folders, and naming conventions.
- Calibration constants (lens scale, pixel-to-micron factors) must be manually entered and verified each time, introducing unit conversion errors.
- There is no standard output format for lab notebooks or publication supplemental materials.

### Analysis Bottlenecks
- Batch processing of multi-sample experiments requires repeated manual operations.
- QA traceability (per-row edge detection logs, threshold values used per image) is not captured.
- Optical artifacts (vignetting, glare) are not systematically corrected, inflating CV% metrics and reducing measurement accuracy.

---

## Solution Overview

The DIW Lab Suite solves these problems with three integrated desktop applications sharing a common design language, calibration constants, and output conventions:

| App | Problem Solved | Key Capability |
|-----|---------------|----------------|
| **G-Code Converter & Visualizer** | No toolpath visualization | 2D/3D interactive layer preview, PNG export, drag-and-drop |
| **Line Width Image Analysis** | Manual, inconsistent measurement | Adaptive Otsu thresholding, tracking-window edge detection, robust CV% |
| **Surface Roughness Analysis** | Qualitative roughness assessment | Self-calibrating flat-field correction, interactive ROI/polygon masks, quantitative CV% |

---

## Before / After Comparison

### G-Code Inspection

| Aspect | Before (Manual) | After (DIW Lab Suite) |
|--------|----------------|----------------------|
| **Toolpath visibility** | Read raw G-code text | Interactive 2D/3D plot with travel vs. print paths |
| **Layer inspection** | Count G-code Z-moves by hand | Click numbered layer buttons, see isolated layer |
| **Bed alignment** | Mentally compute coordinates | Overlay printer bed rectangle on the path |
| **Output** | Screenshot of text editor | 300 DPI publication-quality PNG, snapshot export |
| **Multi-file** | Open each file separately | Drag-and-drop, instant render |

### Line Width Measurement

| Aspect | Before (Manual) | After (DIW Lab Suite) |
|--------|----------------|----------------------|
| **Edge detection** | Click two points per measurement | Automated per-row tracking-window detection |
| **Thresholding** | Fixed guess-and-check | Adaptive Otsu per image, or manual override |
| **CV% reporting** | Manual calculation in spreadsheet | Classic + robust CV% (MAD-based) auto-computed |
| **Multi-image stitching** | Manual alignment, separate spreadsheets | Overlap-aware stitching with QA overlay cycling |
| **Traceability** | None | Per-image threshold log, row-level detection logs, QA overlays |

### Surface Roughness

| Aspect | Before (Manual) | After (DIW Lab Suite) |
|--------|----------------|----------------------|
| **ROI selection** | Crop in image editor | Interactive rectangle selector on live preview |
| **Glare exclusion** | None | Polygon mask tool + intensity threshold cap |
| **Flat-field correction** | None (measure raw) | Self-calibrating: inpaint + blur + normalize |
| **Lens enforcement** | User must remember | 4x backlight automatically blocked, 5x enforced |
| **CSV output** | Manual spreadsheet | Auto-generated with lens metadata, 3sf formatting |

---

## Real Lab Workflow Example

### Scenario: Printing and Characterizing Conductive Silver Ink Lines

**Researcher:** Dr. Chen, postdoctoral fellow in printed electronics

**Sample:** 24 silver-ink lines printed on a glass substrate at varying print speeds

**Step 1 — Pre-print Verification (G-Code Converter)**
1. Dr. Chen opens the AeroScript file by dragging it onto the G-Code Converter window.
2. The 3D All Layers view shows all 8 print layers color-coded by Z height.
3. She clicks Layer 3 to inspect the toolpath, confirms the nozzle path matches the CAD design, and that the bed boundary (140×100 mm) is correctly configured.
4. She exports a 300 DPI PNG snapshot for the lab notebook.

**Step 2 — Post-print Line Width Analysis (Image Analysis)**
1. Under the 5x coaxial microscope, Dr. Chen captures 2 overlapping images per line (48 images total).
2. She selects all 48 images, sets the objective to "5x", and checks "Adaptive Threshold (Otsu)".
3. She clicks **Analyze & Preview** — the suite processes all images, detects edges, stitches overlapping frames, and computes CV% for each line.
4. The QA overlay shows red dots marking detected edge positions; she cycles through images to verify detection quality.
5. She clicks **Save Output Files** — the suite writes a combined CSV with width-vs-position profiles, per-image statistics, and aggregate CV%.

**Step 3 — Surface Roughness Assessment (Surface Roughness Analysis)**
1. Using the same microscope images, Dr. Chen opens the Surface Roughness module.
2. She draws an ROI rectangle around the printed line and adds exclusion polygons around glare spots.
3. She clicks **Compute Surface CV%** — the flat-field correction removes optical vignetting, and the histogram shows the corrected intensity distribution.
4. The results: overall mean CV = 3.2% (well within the 5% target for her experiment).
5. She saves the CSV summary for inclusion in the manuscript supplemental materials.

**Total time:** ~15 minutes for all 24 samples — previously 3-4 hours using manual methods.

---

## Key Differentiators

### 🎯 DIW-Specific, Not General-Purpose
Built specifically for Digital Ink Writing research workflows, not repurposed from general image analysis tools. Every feature — from Aerotech G-Code parsing to 5x coaxial flat-field correction — is purpose-built for DIW.

### 🔬 Self-Calibrating Optics Correction
The flat-field correction algorithm in the Surface Roughness module requires no calibration reference image. It inpaints the sample region and estimates the illumination profile from the background alone — a unique capability for labs without access to reference standards.

### 📊 Two CV% Metrics
Line Width Analysis reports both classic CV% (standard deviation / mean) and robust CV% (Median Absolute Deviation / median). This gives researchers confidence that outlier measurements do not inflate their reported variability.

### 🛡️ Lens Enforcement
The Surface Roughness module explicitly blocks the 4x backlight objective, which is incompatible with reflectance-based surface measurement. This prevents a common lab error that would produce invalid CV% data.

### 🔗 Integrated Workflow
All three apps share a common theme, calibration constants (`LENS_CALIBRATION_UM_PER_PX`), header/footer components, About dialog, and status bar conventions. Switching between tools feels seamless because they are built from the same component library.

### 📦 Standalone & Portable
The PyInstaller build produces a single `lee_tool_suite.exe` with all dependencies bundled. No Python installation or package management is required on the target machine — ideal for shared lab computers, instrument workstations, or conference demonstrations.

### 📋 QA Traceability
Every analysis step is traceable: per-image threshold values, per-row detection logs, and QA overlay images are all saved alongside the summary CSV. This meets the data provenance requirements of peer-reviewed publication and regulated laboratory environments.

---

## UI Walkthrough (Description for Screenshot Capture)

### Launcher Menu
A 620×480 dark-themed window with the title "Lee Research Group — Tool Suite" and subtitle "University of St. Thomas v4.0.0". Three large labeled buttons are stacked vertically:
- **G-Code Converter & Visualizer** (blue/primary) — tooltip: "Convert Aerotech G-Code files into high-res PNGs & inspect 2D/3D nozzle paths"
- **Line Width Image Analysis** (cyan/info) — tooltip: "Measure line width, edge profile, and CV% across microscopic image scans"
- **Surface Roughness Analysis** (green/success) — tooltip: "Reflectance surface roughness analysis with 5x coaxial flat-field correction"
A footer reads "Lee Research Group — University of St. Thomas" and an "ⓘ About" button in the top-right opens the About dialog.

### G-Code Converter Window
1400×900 with a left scrollable control panel (300px) and a right matplotlib canvas (1100px). The left panel has sections:
1. **G-Code Input File** — readonly entry with Browse button
2. **Output Folder** — readonly entry with Browse button
3. **Printer Bed Bounds** — two numeric entry fields (width × height in mm)
4. **View Mode** — three radio buttons: 2D Top, 3D Interactive, 3D All Layers
5. **Layers** — numbered grid buttons (5 columns) for layer selection
6. **Actions** — "Convert to PNG + Load Preview" (green), "Save View Snapshot" (gray), "Open Output Folder" (gray)
The right canvas shows the matplotlib toolpath plot with dark background, plasma-colored print paths, and a matplotlib toolbar at the bottom.

### Line Width Analysis Window
1400×900 with a similar split layout. The right canvas shows two vertically stacked matplotlib subplots:
- **Top:** QA overlay image with detected edge positions overlaid in red
- **Bottom:** Width vs. Position line plot with statistics
Below the canvas: QA navigation bar with "◀ Prev" / "Next ▶" buttons and a "0 / 0" counter.
Left panel: Input Images (listbox + Select Images button), Output Folder, Analysis Parameters (objective lens combo, adaptive threshold checkbox, threshold entry, smoothing window, frame overlap, orientation combo, unit radio buttons), and Execution section with Analyze & Preview / Save / Open buttons.

### Surface Roughness Window
1400×900 with the same split layout. The right canvas shows two vertically stacked matplotlib subplots:
- **Top:** Current microscope image with ROI rectangle (green) and glare exclusion polygons (red, semi-transparent)
- **Bottom:** Histogram of flat-field corrected pixel intensities
Left panel: Image Selection (listbox + Add Images / Clear buttons), Lens / Calibration (5x enforced), Output Directory, ROI & Mask Region (Draw ROI Rectangle, Draw Glare Mask Polygon, Clear Masks), Glare Thresholding (enable checkbox + cutoff value), and Analysis Actions (Compute Surface CV% / Save CSV Summary buttons).

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Python source files | 8 |
| Total lines of code | ~16,500 |
| PyInstaller bundle size | ~85 MB |
| Supported image formats | PNG, JPEG, TIFF, BMP |
| Supported G-Code dialects | Aerotech AeroScript, G-Code (G0-G3) |
| Max analysis throughput | 100+ images per batch |
| Output resolution | 300 DPI PNG |
| Cross-platform | Windows (primary), macOS, Linux |

---

*For technical architecture details, see [docs/architecture.md](docs/architecture.md).*