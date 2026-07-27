---
layout: post
title: "Mapping the Illumination of a Desk"
description: "A mathematical exploration deriving an illumination function from the inverse square law and 3D distance geometry, then testing it against 180 real lux measurements taken across a study desk to find where light is concentrated and where it's lost."
skills:
  - Multivariable calculus (partial derivatives)
  - Mathematical modeling
  - Photometry / inverse square law
  - Python (NumPy, Matplotlib, Seaborn)
  - Data visualization (heatmaps)
  - Experimental measurement & uncertainty
main-image: /illumination-heatmap.png
---

## Overview

Studying at a desk under a single lamp is common practice, especially during long study sessions — but how good is that lighting actually across the whole work surface? This exploration builds a mathematical model of how light spreads from a point source, derives a closed-form illumination function using the inverse square law, then tests that model against 180 real lux measurements taken across a student desk to map where light is strong and where it drops off.

## Deriving the Illumination Function

Modeling the light source as spreading uniformly over a sphere of radius $$r$$, the surface area at any distance is $$A = 4\pi r^2$$. Dividing luminous flux ($$\Phi$$) by that area gives illuminance:

$$E = \frac{\Phi}{4\pi r^2}$$

{% include image-gallery.html images="sphere-diagram.png, inverse-square-law.png" height="350" %}

Substituting the definition of luminous intensity ($$I = \Phi/\omega$$) and assuming a fully "direct" light source (all flux directed downward, $$\omega = 4\pi$$ steradians) simplifies this to:

$$E = \frac{I}{r^2}$$

This is the working formula used throughout: illuminance at a point equals the source's luminous intensity divided by the square of the distance to that point.

## Mapping the Desk in 3D

To apply the formula to a real desk, each measurement point was treated as a coordinate $$(x, y, 0)$$ on the desk plane, with the light source fixed above it at $$(x_{light}, y_{light}, z_{light})$$. Using the Euclidean distance formula, the illumination function becomes:

$$E(x,y) = \frac{I}{(x-x_{light})^2 + (y-y_{light})^2 + z_{light}^2}$$

{% include image-gallery.html images="desk-render.png, light-position-map.png" height="350" %}

## Results

180 lux readings were taken across the desk at 5cm intervals and plotted as a heatmap:

{% include image-gallery.html images="illumination-heatmap.png" height="450" %}

Setting the partial derivatives $$\partial E/\partial x$$ and $$\partial E/\partial y$$ to zero shows the function's critical point occurs exactly at $$(x_{light}, y_{light})$$ — the point directly beneath the light. This matched the heatmap: the brightest region sat directly under the lamp, falling off sharply toward the desk's edges, consistent with the inverse-square relationship.

## Limitations

The model only accounts for direct light from the source — it ignores reflection off walls, absorption by objects, and light spreading beyond the desk surface. The lux meter used was also limited to two significant figures, and the 180-point grid, while dense, doesn't capture the theoretically continuous illumination surface.

## Takeaway

A desk lit by a single overhead point source loses illumination quickly with distance — and since a desk's most-used areas often aren't centered directly under the light, a meaningful fraction of usable light is wasted. The exercise turned an everyday annoyance (uneven desk lighting) into a closed-form, testable multivariable function, and confirmed the inverse square law's prediction with real measurements.

**Python used to generate the heatmap:**
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.array([
    [15, 17, 19, 22, 25, 28, 31, 34, 36, 36, 37, 37, 37, 35, 33, 30, 28, 25],
    [15, 18, 20, 23, 26, 30, 33, 35, 37, 37, 38, 38, 38, 37, 35, 32, 29, 26],
    # ...remaining rows omitted for brevity...
])

plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5)
plt.title("Heatmap with Data Values (lux)")
plt.show()