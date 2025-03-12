"""
Rough Surface Generation Package

This package provides tools for generating and analyzing random rough surfaces
using various methods including parametric (double-sum) and spectral (FFT-based) approaches.
"""

from .parametric_surface import generate_parametric_surface
from .spectral_surface import generate_random_gaussian_surface
from .visualization import plot_surface_3d, plot_surface_2d
from .stl_export import export_to_stl

__version__ = '0.1.0'
__author__ = 'Heming Qin' 