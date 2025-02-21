import pytest
import numpy as np
from rough-surface-generation import generate_parametric_surface  

def test_default_params():
    """
    Test the function with default parameters.
    """
    S1, S2, f = generate_parametric_surface()

    # Check shape
    assert S1.shape == (101, 101), "S1 should be a 101x101 array."
    assert S2.shape == (101, 101), "S2 should be a 101x101 array."
    assert f.shape == (101, 101),  "f should be a 101x101 array."

    # Check for finite values
    assert np.all(np.isfinite(S1)), "S1 contains non-finite values."
    assert np.all(np.isfinite(S2)), "S2 contains non-finite values."
    assert np.all(np.isfinite(f)),  "f contains non-finite values."

    # Check that the surface isn't entirely zero
    assert not np.allclose(f, 0.0), "Surface f is unexpectedly all zeros."

def test_custom_params():
    """
    Test the function with a custom set of parameters.
    """
    N_custom = 5
    b_custom = 2.0
    factor_custom = 0.02
    num_points_custom = 50

    S1, S2, f = generate_parametric_surface(
        N=N_custom,
        b=b_custom,
        factor=factor_custom,
        num_points=num_points_custom
    )

    # Check shape
    assert S1.shape == (num_points_custom, num_points_custom), "S1 shape mismatch."
    assert S2.shape == (num_points_custom, num_points_custom), "S2 shape mismatch."
    assert f.shape == (num_points_custom, num_points_custom),  "f shape mismatch."

    # Check for finite values
    assert np.all(np.isfinite(S1)), "S1 contains non-finite values."
    assert np.all(np.isfinite(S2)), "S2 contains non-finite values."
    assert np.all(np.isfinite(f)),  "f contains non-finite values."

    # Check that the surface isn't entirely zero
    assert not np.allclose(f, 0.0), "Surface f is unexpectedly all zeros."
