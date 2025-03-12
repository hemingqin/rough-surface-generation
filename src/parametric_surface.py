"""
Parametric surface generation using double-sum method
Implements the core of the Bjorn Sjodin 's COMSOL blog's parametric surface formula:
    
      0.01 * sum_{m=-N..N} sum_{n=-N..N}(
          if(m=0 || n=0, 0, (m^2 + n^2)^(-b/2) * cos(2*pi*(m*s1 + n*s2) + random_phase))
      ),
    
    with default parameters matching the blog snippet.
    
    Returns
    -------
    S1 : ndarray, shape (num_points, num_points)
        Mesh of s1 values in [0, 1].
    S2 : ndarray, shape (num_points, num_points)
        Mesh of s2 values in [0, 1].
    f  : ndarray, shape (num_points, num_points)
        Resulting surface values.

    Created by: Heming Qin (2024-12-31)
"""

import numpy as np

def generate_parametric_surface(
    N=10,          # Summation limit for m,n: -N..N
    b=1.8,         # Spectral exponent
    factor=0.01,   # Leading multiplier
    num_points=101 # Number of sample points
):
    """
    Generate a rough surface using double summation method.
    """
    s1 = np.linspace(0, 1, num_points)
    s2 = np.linspace(0, 1, num_points)
    S1, S2 = np.meshgrid(s1, s2)
    
    f = np.zeros_like(S1)
    
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 or n == 0:
                continue
            r = (m**2 + n**2)**(-b / 2.0)
            phase = 2.0 * np.pi * np.random.rand()
            f += r * np.cos(2.0 * np.pi * (m * S1 + n * S2) + phase)
    
    f *= factor
    return S1, S2, f 