"""
Unit tests for surface generation functions.
"""

import pytest
import numpy as np
from src.parametric_surface import generate_parametric_surface
from src.spectral_surface import generate_random_gaussian_surface

def test_parametric_surface_shape():
    """Test if parametric surface has correct shape."""
    num_points = 101
    S1, S2, surface = generate_parametric_surface(num_points=num_points)
    assert surface.shape == (num_points, num_points)
    assert S1.shape == (num_points, num_points)
    assert S2.shape == (num_points, num_points)

def test_parametric_surface_parameters():
    """Test if parametric surface respects input parameters."""
    N = 5
    b = 2.0
    factor = 0.1
    S1, S2, surface = generate_parametric_surface(N=N, b=b, factor=factor)
    
    # Check if surface values are within expected range
    assert np.abs(surface).max() < factor * N  # Rough upper bound

def test_spectral_surface_shape():
    """Test if spectral surface has correct shape."""
    N_x = 128
    N_y = 64
    surface, x, y = generate_random_gaussian_surface(N_x=N_x, N_y=N_y)
    assert surface.shape == (N_y, N_x)
    assert len(x) == N_x
    assert len(y) == N_y

def test_spectral_surface_rms():
    """Test if spectral surface has correct RMS height."""
    h = 0.001
    surface, _, _ = generate_random_gaussian_surface(h=h)
    assert np.abs(np.std(surface) - h) < 0.1 * h  # Within 10% of target

def test_spectral_surface_isotropy():
    """Test if isotropic surface has same correlation length in both directions."""
    clx = 2.0
    surface, x, y = generate_random_gaussian_surface(clx=clx)
    
    # Compute autocorrelation in x and y directions
    acf_x = np.correlate(surface[surface.shape[0]//2, :], 
                        surface[surface.shape[0]//2, :], mode='full')
    acf_y = np.correlate(surface[:, surface.shape[1]//2], 
                        surface[:, surface.shape[1]//2], mode='full')
    
    # Normalize
    acf_x = acf_x / acf_x.max()
    acf_y = acf_y / acf_y.max()
    
    # Check if correlation lengths are similar
    # (find where ACF drops to 1/e)
    e_val = 1/np.e
    x_corr = np.where(acf_x[len(acf_x)//2:] < e_val)[0][0]
    y_corr = np.where(acf_y[len(acf_y)//2:] < e_val)[0][0]
    
    assert np.abs(x_corr - y_corr) < 0.2 * x_corr  # Within 20%

def test_surface_generation_errors():
    """Test if functions handle invalid inputs correctly."""
    # Test negative N
    with pytest.raises(ValueError):
        generate_parametric_surface(N=-1)
    
    # Test negative RMS height
    with pytest.raises(ValueError):
        generate_random_gaussian_surface(h=-0.001)
    
    # Test negative correlation length
    with pytest.raises(ValueError):
        generate_random_gaussian_surface(clx=-1.0)

def test_surface_reproducibility():
    """Test if surfaces are different with different random seeds."""
    np.random.seed(42)
    surface1, _, _ = generate_random_gaussian_surface()
    
    np.random.seed(43)
    surface2, _, _ = generate_random_gaussian_surface()
    
    assert not np.allclose(surface1, surface2) 