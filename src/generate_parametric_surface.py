import numpy as np

def generate_parametric_surface(
    N=10,          # Summation limit for m,n: -N..N
    b=1.8,         # Spectral exponent
    factor=0.01,   # Leading multiplier (e.g., 0.01)
    num_points=101 # Number of sample points in s1 and s2
):
    """
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
    # Create s1, s2 grids in [0,1].
    s1 = np.linspace(0, 1, num_points)
    s2 = np.linspace(0, 1, num_points)
    S1, S2 = np.meshgrid(s1, s2)

    # Initialize the surface array.
    f = np.zeros_like(S1)

    # Double sum over m, n, skipping the (m=0 or n=0) term.
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 or n == 0:
                continue

            # Amplitude ~ (m^2 + n^2)^(-b/2).
            r = (m**2 + n**2)**(-b / 2.0)

            # Random phase in [0, 2π).
            phase = 2.0 * np.pi * np.random.rand()

            # Add the term: r * cos(2π(m*s1 + n*s2) + phase).
            f += r * np.cos(2.0 * np.pi * (m * S1 + n * S2) + phase)

    # Multiply by the leading factor (0.01).
    f *= factor

    return S1, S2, f

# Example usage:
if __name__ == "__main__":
    S1, S2, surface = generate_parametric_surface()
    print("Surface shape:", surface.shape)
    print("Surface min, max:", surface.min(), surface.max())
