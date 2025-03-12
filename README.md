# Rough Surface Generation

A Python package for generating and analyzing random rough surfaces using various methods. This package provides both programmatic and interactive interfaces for surface generation, visualization, and export.

## Features

  - **Parametric (Double-Sum) Method**: Uses a double summation of cosine terms with power-law amplitudes and random phases
  - **Spectral (FFT-Based) Method**: Uses inverse Fourier transform with user-defined power spectral density

- **Interactive Visualization Panel**:

  - Real-time surface generation and visualization
  - Parameter adjustment through intuitive sliders
  - Surface statistics display
  - STL file export capability

- **Analysis Tools**:
  - Surface statistics (RMS height, mean, peak-to-valley)
  - Autocorrelation function
  - Power spectral density

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/rough-surface-generation.git
   cd rough-surface-generation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Interface

1. Start the Streamlit app:

   ```bash
   streamlit run src/app.py
   ```

2. Use the sidebar to:
   - Select generation method
   - Adjust surface parameters
   - Generate and visualize surfaces
   - Export surfaces as STL files

### Programmatic Usage

```python
from src.parametric_surface import generate_parametric_surface
from src.spectral_surface import generate_random_gaussian_surface
from src.visualization import plot_surface_3d
from src.stl_export import export_to_stl

# Generate a parametric surface
S1, S2, surface1 = generate_parametric_surface(
    N=10,          # Summation limit
    b=1.8,         # Spectral exponent
    factor=0.01,   # Scale factor
    num_points=101 # Grid resolution
)

# Generate a spectral surface
surface2, x, y = generate_random_gaussian_surface(
    N_x=128,     # Grid points in x
    h=0.001,     # RMS height
    clx=2.0,     # Correlation length
    rL_x=10.0    # Surface length
)

# Visualize surfaces
plot_surface_3d(S1, S2, surface1, title="Parametric Surface")
plot_surface_3d(x, y, surface2, title="Spectral Surface")

# Export to STL
export_to_stl(S1, S2, surface1, "parametric_surface.stl")
```

## Theory

### Parametric (Double-Sum) Method

The surface is generated using a double summation:

\[
h(x,y) = A \sum*{m=-N}^N \sum*{n=-N}^N (m^2 + n^2)^{-\beta/2} \cos(2\pi(mx + ny) + \phi\_{mn})
\]

where:

- \(A\) is the amplitude scaling factor
- \(\beta\) is the spectral exponent
- \(\phi\_{mn}\) are random phases
- \(N\) is the summation limit

### Spectral (FFT-Based) Method

The surface is generated by:

1. Creating a Gaussian random field in frequency space
2. Applying a correlation filter (e.g., Gaussian)
3. Performing inverse FFT to get the surface heights

## Project Structure

```
project/
├── README.md             # This file
├── requirements.txt      # Dependencies
├── src/
│   ├── __init__.py
│   ├── parametric_surface.py   # Parametric generation method
│   ├── spectral_surface.py     # FFT-based generation method
│   ├── visualization.py        # Plotting functions
│   ├── stl_export.py          # STL file export
│   └── app.py                 # Streamlit interface
├── tests/
│   └── test_surface_generation.py  # Unit tests


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original parametric method inspired by COMSOL blog post
- FFT-based method based on standard spectral techniques in surface metrology


---

## Background

Random rough surfaces are widely used in fields like optics, geostatistics, surface metrology, and computer graphics. Different methods exist for generating such surfaces, each with distinct advantages:

- **Parametric (Double-Sum) Method:** A direct summation of a finite number of modes \((m,n)\), each with a power-law amplitude \((m^2 + n^2)^{-\beta/2}\) and a random phase. This method is easy to implement and interpret, but can be more limited in resolution if \(N\) is small.
- **Spectral (FFT-Based) Method:** Uses a continuous (or dense) frequency grid. You define a 2D spectral filter (e.g., Gaussian, Lorentzian) that dictates how amplitudes decay with wavenumber. Random phases are applied, then an inverse FFT yields the surface in real space.

Both approaches can yield surfaces with specified RMS height, correlation length, or spectral exponent. The choice often depends on application requirements (e.g., resolution, ease of parameter tuning, or direct control over frequencies).
```
