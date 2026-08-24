#!/usr/bin/env python3
"""Generate a main image for the DIW Lab Suite project page."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = r"C:\Users\simon\Documents\simongarcia.engineer\_projects\diw-lab-suite"

# Create a clean, professional main image showing the three apps
fig, axes = plt.subplots(1, 3, figsize=(12, 4), facecolor='#1a1c20')

# Color scheme matching the apps
colors = ['#4a76ee', '#00bcd4', '#4caf50']
titles = ['G-Code\nConverter', 'Line Width\nAnalysis', 'Surface\nRoughness']
subtitles = [
    'Toolpath Visualization\n2D/3D Preview',
    'Edge Detection\nCV% Statistics',
    'Flat-Field Correction\nQuantitative CV%'
]

for i, (ax, color, title, subtitle) in enumerate(zip(axes, colors, titles, subtitles)):
    ax.set_facecolor('#2d2d2d')
    
    # Create a stylized icon area
    if i == 0:
        # G-Code: a simple toolpath-like line
        x = np.linspace(0, 1, 50)
        y = 0.5 + 0.3 * np.sin(3 * np.pi * x) * np.exp(-x)
        ax.plot(x, y, color=color, linewidth=2.5)
        # Add a few points
        ax.scatter([0, 0.25, 0.5, 0.75, 1.0], 
                   [0.5, 0.67, 0.3, 0.7, 0.5], 
                   color=color, s=15, zorder=5)
    elif i == 1:
        # Line Width: a line profile with detected edges
        x = np.linspace(0, 1, 100)
        profile = np.exp(-((x - 0.5) ** 2) / (2 * 0.02))
        ax.plot(x, profile, color=color, linewidth=2)
        # Mark edges
        ax.axvline(0.35, color='red', linestyle='--', alpha=0.6, linewidth=1)
        ax.axvline(0.65, color='red', linestyle='--', alpha=0.6, linewidth=1)
        ax.fill_between(x, 0, profile, alpha=0.2, color=color)
    else:
        # Surface Roughness: a histogram
        data = np.random.normal(0.5, 0.1, 1000)
        ax.hist(data, bins=20, color=color, alpha=0.7, edgecolor='white', linewidth=0.5)
    
    ax.set_title(title, color='white', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_visible(False)
    
    # Add subtitle
    ax.text(0.5, -0.15, subtitle, transform=ax.transAxes, 
            ha='center', va='top', color='#aaaaaa', fontsize=8)

plt.suptitle('DIW Lab Suite v4.0', color='white', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2)
output_path = os.path.join(output_dir, 'diw-suite-showcase.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#1a1c20')
plt.close()
print(f"Generated: {output_path}")

# Create launcher-menu.png (simple version)
fig, ax = plt.subplots(figsize=(5, 4), facecolor='#1a1c20')
ax.set_facecolor('#2d2d2d')
ax.set_xlim(0, 5)
ax.set_ylim(0, 4)
ax.set_xticks([])
ax.set_yticks([])
ax.spines[:].set_visible(False)

# Title
ax.text(2.5, 3.5, 'Lee Research Group — Tool Suite', 
        ha='center', va='center', color='white', fontsize=12, fontweight='bold')
ax.text(2.5, 3.15, 'University of St. Thomas  v4.0.0', 
        ha='center', va='center', color='#888888', fontsize=8)

# Three buttons
buttons = [
    (2.5, 2.5, 'G-Code Converter\n& Visualizer', '#4a76ee'),
    (2.5, 1.6, 'Line Width\nImage Analysis', '#00bcd4'),
    (2.5, 0.7, 'Surface\nRoughness Analysis', '#4caf50'),
]

for x, y, label, color in buttons:
    rect = plt.Rectangle((x-1.5, y-0.35), 3, 0.7, 
                         facecolor=color, edgecolor='white', 
                         linewidth=0.5, alpha=0.8,  # reduced alpha
                         linestyle='-')
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', color='white', fontsize=8, fontweight='bold')

# Footer
ax.text(2.5, 0.15, 'Lee Research Group — University of St. Thomas', 
        ha='center', va='center', color='#555555', fontsize=7)

output_path = os.path.join(output_dir, 'launcher-menu.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#1a1c20')
plt.close()
print(f"Generated: {output_path}")