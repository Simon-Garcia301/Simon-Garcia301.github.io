---
layout: post
title: "Aerodynamic Drag Analysis: Open Windows vs. Air Conditioning"
description:  A Physics Internal Assessment investigating whether opening a car's
    windows increases fuel consumption more than running the air
    conditioning. Used CFD simulation (SimFlow/OpenFOAM) on a 3D-modeled
    2020 Hyundai Santa Fe to compare drag force and drag coefficient
    across five speeds, in both open- and closed-window configurations.
skills: 
  - Computational Fluid Dynamics (CFD)
  - OpenFOAM / SimFlow
  - 3D modeling (Blender)
  - Aerodynamic analysis
  - Data analysis (Python, Matplotlib, Excel)
  - Uncertainty analysis

main-image: /drag-cfd-contour-main.png
---

## Overview
Opening the windows on a highway drive versus keeping them closed and
running the AC is a common fuel-saving debate. This investigation used
Computational Fluid Dynamics (CFD) to settle it quantitatively: I built a
3D model of a 2020 Hyundai Santa Fe, created open- and closed-window
versions in Blender, and ran a digital wind tunnel in SimFlow (an
OpenFOAM-based CFD platform) at five velocities spanning city to highway
speeds (5–40 m/s).

{% include image-gallery.html images="car-model-open-windows.png, car-model-closed-windows.png" height="400" %}

## Method
- **Geometry:** 2020 Hyundai Santa Fe STL model, edited in Blender 4.2.3
  to produce matched open-window and closed-window versions with a fixed
  ~3.86 m² frontal area.
- **Solver setup:** k–ω SST turbulence model, moving-wall ground plane to
  replicate real driving conditions, no-slip car surface, slip tunnel
  walls.
- **Test matrix:** 5 velocities (5, 10, 20, 30, 40 m/s) × 2 window states
  × 3 iteration counts (500 / 1000 / 1500) to check convergence — 30 runs
  total.

{% include image-gallery.html images="frontal-area-measurement.png" height="400" %}

## Results

| Configuration | Avg. Drag Coefficient (C_d) | Uncertainty |
|----------|----------|----------|
| Closed windows | 0.2807 | ± 0.0014 |
| Open windows | 0.2909 | ± 0.0011 |

Opening the windows raised the drag coefficient by about 3.6% and the
gap held steady across every tested speed.

{% include image-gallery.html images="graph-drag-force-vs-velocity.png, graph-drag-coefficient-vs-velocity.png" height="400" %}

At highway speed (40 m/s), the open-window configuration demanded about
**1.57 kW** more power than closed windows with AC — roughly **5.66 MJ**
of extra energy over one hour of driving.

## Takeaway
Even a small geometric change — cracking the windows — measurably
increases aerodynamic drag, and that penalty grows fast with speed
(drag ∝ v², power ∝ v³). At city speeds the difference is negligible; at
highway speeds, running the AC with the windows up is the more
fuel-efficient choice.

*Full write-up (methodology, uncertainty propagation, CFD boundary
conditions, and evaluation): [link to PDF if hosted].*