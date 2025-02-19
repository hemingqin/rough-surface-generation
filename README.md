# rough-surface-generation

This project demonstrates two different approaches to generating 2D random rough surfaces:

1. **Parametric (Double-Sum) Method** – Inspired by the COMSOL blog post on using a double summation of cosine terms with power-law amplitudes and random phases.  
2. **Spectral (FFT-Based) Method** – Uses an inverse Fourier transform with a user-defined power spectral density (PSD) or correlation function (e.g., Gaussian, exponential).

#Right now, I have finished the two generation methods, the rest will be finished this month
#02/18/2025
#Heming


project/
├── README.md             
├── requirements.txt      # List of dependencies (e.g., numpy, matplotlib, etc.).
├── docs/
│   └── usage.md          # Documentation and user guides.
├── src/
│   ├── __init__.py       # Make the directory a Python package.
│   ├── parametric_surface.py   # Contains the function for generating the parametric surface (double-sum method). (Finished)
│   ├── spectral_surface.py     # Contains the function for generating the FFT-based Gaussian random surface. Finished
│   ├── analysis.py       # Functions for computing statistical properties (RMS, autocorrelation, PSD, etc.).
│   ├── visualization.py  # Functions for plotting 2D/3D visualizations of surfaces and curves.
│   └── main.py           
├── notebooks/
│   └── interactive_analysis.ipynb  # A Jupyter Notebook for interactive exploration and analysis.
└── tests/

---

## Background
Random rough surfaces are widely used in fields like optics, geostatistics, surface metrology, and computer graphics. Different methods exist for generating such surfaces, each with distinct advantages:
- **Parametric (Double-Sum) Method:** A direct summation of a finite number of modes \((m,n)\), each with a power-law amplitude \((m^2 + n^2)^{-\beta/2}\) and a random phase. This method is easy to implement and interpret, but can be more limited in resolution if \(N\) is small.
- **Spectral (FFT-Based) Method:** Uses a continuous (or dense) frequency grid. You define a 2D spectral filter (e.g., Gaussian, Lorentzian) that dictates how amplitudes decay with wavenumber. Random phases are applied, then an inverse FFT yields the surface in real space.

Both approaches can yield surfaces with specified RMS height, correlation length, or spectral exponent. The choice often depends on application requirements (e.g., resolution, ease of parameter tuning, or direct control over frequencies).

## Installation
1. **Clone or download** this repository.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

