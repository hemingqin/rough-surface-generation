"""
Spectral (FFT-based) surface generation.
"""

import numpy as np

def generate_random_gaussian_surface(N_x=128, N_y=None, rL_x=10.0, rL_y=None, h=0.001, clx=2.0, cly=None):
    """
    Generate a random Gaussian surface using FFT method.
    """
    if N_y is None:
        N_y = N_x
    if rL_y is None:
        rL_y = rL_x
    if cly is None:
        cly = clx

    x = np.linspace(-rL_x/2, rL_x/2, N_x)
    y = np.linspace(-rL_y/2, rL_y/2, N_y)
    
    Z = h * np.random.randn(N_y, N_x)
    X, Y = np.meshgrid(x, y)
    
    F = np.exp(-(np.abs(X)/(clx/2.0) + np.abs(Y)/(cly/2.0)))
    
    fft_Z = np.fft.fft2(Z)
    fft_F = np.fft.fft2(F)
    conv = np.fft.ifft2(fft_Z * fft_F)
    
    factor = np.sqrt(rL_x * rL_y) / (N_x * N_y * clx * cly)
    surface = factor * np.real(conv)
    
    return surface, x, y 