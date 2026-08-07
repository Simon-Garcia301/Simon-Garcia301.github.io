# Architecture Documentation

## Overview

The DIW Lab Suite follows a modular **Engine-GUI-Separation** architecture, where computational logic is cleanly isolated from user interface code. This design enables:

- **Testability:** Engines can be unit-tested without a Tkinter event loop.
- **Reusability:** The same engine can serve multiple front-ends (desktop GUI, CLI, web API).
- **Maintainability:** GUI changes (theming, layout, new controls) do not affect analysis logic.
- **Parallel development:** Researchers can iterate on analysis algorithms while designers work on the UI.

---

## Package Structure

```
apps/gcode-converter/          ← Primary application package
├── main.py                    ← Launcher menu (entry point)
├── gui/                       ← GUI layer
│   ├── __init__.py
│   ├── gcode_converter_gui.py
│   ├── image_analysis_gui.py
│   └── surface_roughness_gui.py
├── engines/                   ← Engine/computation layer
│   ├── __init__.py
│   ├── gcode_engine.py
│   ├── line_width_engine.py
│   └── surface_roughness_engine.py
├── shared/                    ← Shared components
│   ├── __init__.py
│   └── ui_common.py
├── assets/                    ← Application assets
│   └── app_icon.ico
├── lee_tool_suite.spec        ← PyInstaller spec
├── hook-tkinterdnd2.py        ← PyInstaller hook for tkinterdnd2
├── hook-ttkbootstrap.py       ← PyInstaller hook for ttkbootstrap
└── version_info.txt           ← Windows version metadata
```

### Standalone App Directories

```
apps/line-width-analysis/      ← Contains README.md + src/ junction → gcode-converter
apps/surface-roughness/        ← Contains README.md + src/ junction → gcode-converter
```

These directories provide standalone entry points for users who want to launch a specific tool without the launcher menu. The `src/` directory is a junction (NTFS symlink equivalent) pointing to the shared `gcode-converter` package, ensuring no code duplication.

---

## Architecture Pattern: Engine-GUI Separation

### Engine Layer (`engines/`)

Each engine is a pure-Python module (or class) that:

- Accepts input data via constructor parameters or method arguments.
- Performs computation using only NumPy, OpenCV, and SciPy — no Tkinter dependencies.
- Returns a dictionary of results with typed, well-documented keys.
- Is importable from any context (GUI, CLI, Jupyter notebook, automated test).

```python
# Pattern example (LineWidthAnalyzer):
results = analyzer.analyze()
# Returns: {
#   "width_profile": np.ndarray,
#   "stats": {"mean": float, "cv_pct": float, "robust_cv_pct": float, ...},
#   "qa_image": np.ndarray,
#   "fig_plot": matplotlib.figure.Figure,
#   "qa_images_all": dict,
#   "row_logs": dict,
#   "thresholds_used": dict,
#   "stitch_quality": float,
# }
```

### GUI Layer (`gui/`)

Each GUI module is a Tkinter/ttkbootstrap window that:

- Builds the widget tree using shared components from `ui_common.py`.
- Wires user interactions (button clicks, file dialogs, checkbox toggles) to engine methods.
- Runs analysis in a **background thread** (`threading.Thread`, daemon=True) to keep the UI responsive.
- Uses `root.after(0, callback)` to marshal results back to the GUI thread safely.
- Is importable as a `build_gui(master=None)` function returning a `ttk.Window` or `ttk.Toplevel`.

### Shared Components (`shared/`)

The `ui_common.py` module provides:

- **Calibration constants:** `LENS_CALIBRATION_UM_PER_PX` — single source of truth for pixel-to-micron scale factors across all three apps.
- **Theme palette:** `COLOR_BG_DARK`, `COLOR_PANEL_DARK`, `COLOR_TEXT`, etc. — all apps share the same dark scientific color scheme.
- **Widget factories:** `make_app_header()`, `make_app_footer()`, `make_titled_panel()`, `make_action_button()`, `make_scrollable_left_panel()` — consistent look and feel.
- **Status utilities:** `set_status()` with four severity levels (info, success, warning, error) mapped to palette colors.
- **Asset resolution:** `load_app_icon()`, `get_asset_path()` — PyInstaller-safe file path resolution for bundled assets.

---

## Data Flow

```
User Action
    │
    ▼
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  GUI Layer       │────▶│  Background      │────▶│  Engine Layer    │
│  (tkinter/ttk)   │     │  Thread          │     │  (pure Python)   │
│                  │     │                  │     │                  │
│  • File dialogs  │     │  • Prevents UI   │     │  • G-Code parse  │
│  • Button clicks │     │    freeze        │     │  • Edge detect   │
│  • Status bar    │     │  • Isolates      │     │  • Flat-field    │
│  • Matplotlib    │     │    exceptions    │     │  • Statistics    │
│    canvas render │     │                  │     │                  │
└─────────────────┘     └──────────────────┘     └──────────────────┘
        │                       │                        │
        │                       ▼                        │
        │              ┌──────────────────┐              │
        │              │  root.after(0,   │              │
        └──────────────│  callback)       │◀─────────────┘
                       │  → GUI thread    │
                       └──────────────────┘
```

---

## Threading Model

All analysis operations are executed in background daemon threads to prevent UI freezing:

```python
# Pattern from gcode_converter_gui.py:
threading.Thread(
    target=_png_worker,
    args=(...),
    daemon=True,
).start()

# Worker function runs engine, then schedules GUI update:
def _png_worker(...):
    result = convert_gcode_to_png(...)
    root.after(0, _png_done, result, ...)
```

Key rules:
1. **Engine calls are always thread-safe** — they use only NumPy/OpenCV operations (GIL-releasing for I/O).
2. **GUI updates always happen on the main thread** via `root.after(0, ...)`.
3. **Daemon threads** are used so they do not block application exit.
4. **Progress bars** are indeterminate (`mode="indeterminate"`) during analysis.

---

## Modularity Boundaries

### G-Code Engine

| Module | Responsibility | Dependencies |
|--------|---------------|-------------|
| `gcode_engine.py` | G-Code/AeroScript parsing, arc interpolation, matplotlib rendering, PNG export | `re`, `math`, `os`, `matplotlib`, `numpy` |
| `gcode_engine.MachineState` | Tracks position, unit mode, feedrate, variables | None |
| `gcode_engine.PrintLayer` | Container for travel/print segments at a Z-height | None |
| `gcode_engine.convert_gcode_to_png()` | Public API: file → PNG pipeline | All above |

### Line Width Engine

| Module | Responsibility | Dependencies |
|--------|---------------|-------------|
| `line_width_engine.py` | Image loading, edge detection, width computation, QA overlays, results export | `opencv`, `numpy`, `matplotlib`, `scipy`, `skimage` |
| `LineWidthAnalyzer` | Full analysis pipeline as a class with configurable parameters | All above |
| `LineWidthAnalyzer.analyze()` | Public API: runs full pipeline | All above |
| `LineWidthAnalyzer.save_results()` | Persists CSV, QA images to disk | `os`, `csv`, `opencv` |

### Surface Roughness Engine

| Module | Responsibility | Dependencies |
|--------|---------------|-------------|
| `surface_roughness_engine.py` | Flat-field correction, intensity statistics, ROI/polygon masking, CSV export | `opencv`, `numpy`, `csv` |
| `SurfaceRoughnessAnalyzer` | Full analysis pipeline as a class | All above |
| `SurfaceRoughnessAnalyzer.analyze()` | Public API: processes all images | All above |
| `SurfaceRoughnessAnalyzer._flat_field_correct()` | Self-calibrating vignetting correction via inpainting + Gaussian blur | `opencv` |

### Shared UI Components

| Module | Responsibility | Dependencies |
|--------|---------------|-------------|
| `ui_common.py` | Theme constants, widget factories, about dialog, asset handling | `tkinter`, `ttkbootstrap`, `PIL` (optional) |
| `ui_common.LENS_CALIBRATION_UM_PER_PX` | `dict[str, float]` — single calibration source | None |
| `ui_common.make_app_header()` | Creates consistent header with Return/About buttons | `ttkbootstrap` |
| `ui_common.show_about_dialog()` | Modal dialog with lab info and tool descriptions | `ttkbootstrap`, `PIL` |

---

## Configuration & Calibration

All calibration constants are centralized in `ui_common.py`:

```python
LENS_CALIBRATION_UM_PER_PX = {
    "4x": 0.8075,  # Reference only — unsupported for reflectance surface roughness
    "5x": 0.6408,  # Primary coaxial reflectance objective
}
```

Both analysis engines import this dictionary from `ui_common`, ensuring consistent calibration across the suite. The Surface Roughness module enforces 5x-only usage, blocking the 4x lens selection with a warning dialog.

---

## PyInstaller Packaging

The suite can be packaged as a standalone Windows executable using PyInstaller:

```
pyinstaller lee_tool_suite.spec --additional-hooks-dir=.
```

### Custom Hooks

| Hook | Purpose |
|------|---------|
| `hook-tkinterdnd2.py` | Collects the compiled `tkdnd` binaries (`.dll`, `.tcl`) required for drag-and-drop support |
| `hook-ttkbootstrap.py` | Collects theme files, icons, and fonts; ensures all submodules are imported |

### Executable Build

The spec file (`lee_tool_suite.spec`) configures:
- Icon: `assets/app_icon.ico`
- Data files: `st thomas logo.png`, `assets/*`
- Console: `False` (windowed GUI application)
- UPX compression: enabled

---

## Import Philosophy

The source files in this repository are preserved byte-for-byte from the original flat layout. The imports use the original flat module names (e.g., `from gcode_engine import ...`, `from ui_common import ...`) rather than the package-qualified names (`from engines.gcode_engine import ...`). This is intentional: the codebase is packaged here for documentation and showcase purposes, and the flat imports reflect the original project structure.

To run the code from the packaged layout, add `apps/gcode-converter` to `sys.path`:

```python
import sys
sys.path.insert(0, "apps/gcode-converter")
sys.path.insert(0, "apps/gcode-converter/gui")
sys.path.insert(0, "apps/gcode-converter/engines")
sys.path.insert(0, "apps/gcode-converter/shared")
```

---

## Future Architecture Considerations

### Migration to Package-Qualified Imports
If the suite is refactored for pip-installable distribution, the flat imports should be updated to use the package structure. The `__init__.py` files are already in place to support this transition.

### CLI Mode
Each engine's public API is already importable without a GUI. A CLI wrapper (e.g., using `argparse` or `click`) could be added for headless batch processing on servers or CI pipelines.

### Plugin System
For future extensibility, the engine could be refactored to support a plugin architecture where new analysis modules (e.g., contact angle measurement, film thickness profilometry) can be added without modifying the core framework.

### Web API
The engine-GUI separation makes it straightforward to expose the analysis pipeline as a REST API using Flask or FastAPI, enabling remote analysis or integration with laboratory information management systems (LIMS).

---

*Documentation generated for DIW Lab Suite v4.0.0 — Lee Research Group, University of St. Thomas.*