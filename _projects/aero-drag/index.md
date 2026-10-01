---
layout: post
order: 4
title: "Aerodynamic Drag with Open and Closed Vehicle Windows"
description: "A CFD study comparing the aerodynamic drag of open- and closed-window vehicle geometries across five airflow speeds."
skills:
  - Computational fluid dynamics
  - SimFlow / OpenFOAM
  - Blender / ParaView
  - Python / Matplotlib / Excel
  - Uncertainty analysis
main-image: drag-cfd-contour-main.png
main-image-alt: "Velocity-magnitude contour around the vehicle model in the simulated wind tunnel."
main-image-caption: 'Flow visualization from the Physics Internal Assessment; this is a simulation result. [1](#ref-1)'
---

## Context and problem

Opening a vehicle's windows changes the airflow around its body and cabin. I investigated how that change affected aerodynamic drag in a digital wind tunnel, using a model of a 2020 Hyundai Santa Fe. The original question included air-conditioning use, but the simulations compared window configurations; they did not measure an air-conditioning load or fuel consumption. [1](#ref-1)

## My role and contributions

I edited an imported vehicle model in Blender to create open- and closed-window configurations, ran the SimFlow/OpenFOAM simulations, processed the drag-force outputs in Excel and Python, and examined the flow fields in ParaView. The assessment was completed in April 2025. [1](#ref-1), [2](#ref-2)

{% include image-gallery.html images="car-model-open-windows.png, car-model-closed-windows.png" alts="Vehicle geometry with window openings used for the CFD comparison.||Matched vehicle geometry with closed windows used for the CFD comparison." captions="Open-window model edited in Blender. [1](#ref-1)||Closed-window model used for comparison. [1](#ref-1)" %}

## Methods and tools

- **Test matrix:** airflow speeds of 5, 10, 20, 30, and 40 m/s; two window configurations; and 500, 1,000, and 1,500 solver iterations per condition, giving 30 simulation runs. [1](#ref-1), pp. 9–12.
- **Flow model:** incompressible air, a k–ω SST turbulence model, a moving ground boundary, and a no-slip vehicle surface. The report specifies an air density of 1.225 kg/m³. [1](#ref-1), pp. 5–7.
- **Geometry:** Blender 4.2.3 edits to an imported STL model. A frontal bounding rectangle supplied an approximate reference area of 3.86 m²; it was not an exact projected silhouette measurement. [1](#ref-1), pp. 8–10.
- **Analysis:** drag-force comparisons, drag-coefficient calculations, uncertainty propagation, and velocity-contour visualization. The iteration comparisons checked numerical sensitivity; there was no physical wind-tunnel validation. [1](#ref-1), pp. 12–22.

{% include image-gallery.html images="frontal-area-measurement.png" alts="Front orthographic view of the vehicle with width and height dimensions used for the bounding-rectangle area estimate." captions="Approximate frontal reference area measured in Blender. [1](#ref-1), table 3." %}

## Results

The report recorded greater drag for the open-window configuration at each tested airflow speed. At 40 m/s, it reported the following force and power values. [1](#ref-1), pp. 20–21.

<div class="table-scroll" role="region" aria-label="Drag simulation results at 40 metres per second" tabindex="0">
<table>
  <caption>Reported simulation results at 40 m/s [1]</caption>
  <thead><tr><th scope="col">Window configuration</th><th scope="col">Drag force (N)</th><th scope="col">Aerodynamic power (kW)</th></tr></thead>
  <tbody>
    <tr><th scope="row">Closed</th><td>1,056.67</td><td>42.267</td></tr>
    <tr><th scope="row">Open</th><td>1,095.98</td><td>43.839</td></tr>
  </tbody>
</table>
</div>

Using \(P = F_d v\), the report calculated an additional aerodynamic power demand of approximately **1.57 kW** with open windows at 40 m/s. Maintaining that condition for one hour would require approximately **5.66 MJ** of additional aerodynamic work. These are calculated mechanical quantities, not a measured fuel-consumption or air-conditioning comparison. [1](#ref-1), p. 20.

{% include image-gallery.html images="graph-drag-force-vs-velocity.png" alts="Plots of simulated drag force against airflow speed for the closed- and open-window configurations." captions="Drag-force trends from the assessment. The data are numerical simulation outputs. [1](#ref-1), graphs 1–2." %}

## Outcomes, limitations, and next steps

The study connected changes in vehicle geometry to simulated force and power demand. Its limitations included simplified underbody geometry, omitted wheel rotation, idealized flow conditions, and the absence of physical testing. The report proposed mesh refinement, crosswind cases, rotating wheels, and a separate efficiency model as possible extensions. [1](#ref-1), pp. 21–22.

The report's summary drag coefficients do not reconcile with its per-speed table. I have omitted those averages and the percentage derived from them until the original calculation is checked. The study therefore supports a comparison of the two simulated geometries within its stated assumptions, without establishing a general fuel-saving recommendation. [1](#ref-1), table 10 and pp. 16, 19–20.

## References

<ol class="references">
  <li id="ref-1">[1] S. Garcia Salmeron, “Physics IA – Drag Force,” Physics Internal Assessment, pp. 1–23. Source report retained in the project review archive; download not published.</li>
  <li id="ref-2">[2] S. Garcia Salmeron, “Simon Garcia Salmeron Resume,” ver. 6, p. 1, “Aerodynamic Drag Analysis.” Source résumé retained in the project review archive.</li>
</ol>
