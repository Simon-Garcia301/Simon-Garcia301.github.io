---
layout: post
order: 2
title: "DIW Laboratory Software: Toolpaths and Microscopy Analysis"
description: "A Python desktop tool suite for visualizing direct ink writing toolpaths and analyzing microscopy images for the Lee Research Group."
skills:
  - Direct ink writing
  - G-code / AeroScript parsing
  - Python / NumPy / OpenCV
  - Tkinter / ttkbootstrap
  - Matplotlib
  - Image-analysis quality control
main-image: diw-suite-showcase.png
main-image-alt: "Illustration of the suite's toolpath, line-width, and image-intensity analysis modules."
main-image-caption: 'Illustrative module overview generated for the portfolio; the plotted shapes are not experimental measurements. [[5]](#ref-5)'
---

## Context and problem

Direct ink writing research uses both programmed nozzle paths and post-print microscopy. The suite brought toolpath visualization, line-width analysis, and image-intensity analysis into a shared desktop interface for the Lee Research Group at the University of St. Thomas. [[1]](#ref-1)–[[4]](#ref-4)

## My role and contributions

I developed the Python tool suite and co-developed calibrated line-width analysis with a research partner. That work used automated edge detection and CSV measurement exports to support experimental analysis. The available résumé identifies the shared contribution but does not name the partner or assign every module individually. [[6]](#ref-6)

{% include image-gallery.html images="launcher-menu.png" alts="Portfolio illustration of a launcher with buttons for the suite's three analysis modules." captions="Illustrative launcher layout, not a captured application screenshot. [[5]](#ref-5)" %}

## Methods and tools

### Toolpath visualization

The parser implements linear and arc motion handling, position/unit tracking, variables, and layer grouping. Matplotlib renders the parsed paths, and the interface provides 2D and 3D views. These implemented features do not establish compatibility with every G-code or AeroScript program. [[1]](#ref-1), [[4]](#ref-4)

### Line-width microscopy analysis

The image-analysis engine supports automatic Otsu or user-selected thresholding, row-wise edge tracking, overlap reconciliation, and measurement exports. It reports a classical coefficient of variation from the mean and standard deviation, plus a median/MAD-based robust statistic. Edge overlays and row logs allow the detected boundaries to be inspected alongside the measurements. [[2]](#ref-2)

### Image-intensity variation

The module labeled “Surface Roughness Analysis” computes the mean, standard deviation, and coefficient of variation of grayscale intensity within a selected region, with exclusion masks and an optional illumination correction. Its output describes image-intensity variation; it does not measure surface height or establish a calibrated Ra or Rq roughness value. [[3]](#ref-3)

### Interface and organization

The implementation uses Python, Tkinter/ttkbootstrap, NumPy, OpenCV, and Matplotlib. Computational and interface code reside in separate modules, with shared interface components. A PyInstaller specification is included in the source tree. [[1]](#ref-1)–[[4]](#ref-4)

## Results and outputs

The source implements toolpath plots, line-width profiles, image overlays, intensity histograms, and CSV summaries. These outputs support inspection and traceability of the analysis settings. No measured speedup, accuracy benchmark, physical-roughness calibration, or deployment certification is claimed here. [[1]](#ref-1)–[[4]](#ref-4)

## Outcomes, limitations, and next steps

The suite organized related laboratory analysis tasks around a shared launcher and export workflow. Line-width results depend on image calibration, boundary detection, and frame alignment; intensity results also depend on illumination and masking. The included source does not establish that the packaged executable matches every source module. [[1]](#ref-1)–[[4]](#ref-4)

The next verification steps are to compare automated widths with reference measurements, review the illumination-correction mask behavior, and confirm the packaged application's imports and required assets. Unpublished experimental results and microscopy examples remain outside this portfolio entry.

## References

<ol class="references">
  <li id="ref-1">[1] Lee Research Group, <a href="{{ '/src/diw-lab-suite/gcode-converter/engines/gcode_engine.py' | relative_url }}">“gcode_engine.py,”</a> DIW Lab Suite source, parser and rendering functions.</li>
  <li id="ref-2">[2] Lee Research Group, <a href="{{ '/src/diw-lab-suite/gcode-converter/engines/line_width_engine.py' | relative_url }}">“line_width_engine.py,”</a> DIW Lab Suite source, edge tracking, stitching, statistics, and export functions.</li>
  <li id="ref-3">[3] Lee Research Group, <a href="{{ '/src/diw-lab-suite/gcode-converter/engines/surface_roughness_engine.py' | relative_url }}">“surface_roughness_engine.py,”</a> DIW Lab Suite source, intensity-analysis and masking functions.</li>
  <li id="ref-4">[4] Lee Research Group, DIW Lab Suite source: <a href="{{ '/src/diw-lab-suite/gcode-converter/main.py' | relative_url }}">launcher</a>, <a href="{{ '/src/diw-lab-suite/gcode-converter/gui/gcode_converter_gui.py' | relative_url }}">toolpath interface</a>, <a href="{{ '/src/diw-lab-suite/gcode-converter/gui/image_analysis_gui.py' | relative_url }}">line-width interface</a>, <a href="{{ '/src/diw-lab-suite/gcode-converter/gui/surface_roughness_gui.py' | relative_url }}">intensity interface</a>, <a href="{{ '/src/diw-lab-suite/gcode-converter/shared/ui_common.py' | relative_url }}">shared interface components</a>, and <a href="{{ '/src/diw-lab-suite/gcode-converter/lee_tool_suite.spec' | relative_url }}">PyInstaller specification</a>.</li>
  <li id="ref-5">[5] “generate_diw_images.py,” portfolio illustration-generation script. <a href="{{ '/scripts/generate_diw_images.py' | relative_url }}">Source</a>.</li>
  <li id="ref-6">[6] S. Garcia Salmeron, “Simon Garcia Salmeron Resume,” ver. 6, p. 1, “Lee Research Group Tool Suite.” Source résumé retained in the project review archive.</li>
</ol>
