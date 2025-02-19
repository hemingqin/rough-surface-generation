import numpy as np

def generate_random_gaussian_surface(N_x, N_y=None, rL_x=None, rL_y=None, h=0.0001, clx=None, cly=None):
    """
    Generates a 2-dimensional random gaussian rough surface f(x,y).
    
    If N_y, rL_y, and cly are omitted, the function assumes an isotropic surface 
    where N_x, rL_x, h, and clx are used.
    
    Parameters:
        N_x  : int
               Number of surface points along the x-axis (or for both axes if isotropic).
        N_y  : int, optional
               Number of surface points along the y-axis.
        rL_x : float, optional
               Length of the surface along the x-axis (or for both axes if isotropic).
        rL_y : float, optional
               Length of the surface along the y-axis.
        h    : float, RMS height (unit is meter).
        clx  : float, optional
               Correlation length in the x-direction.
        cly  : float, optional
               Correlation length in the y-direction.
    
    Returns:
        f : ndarray
            Surface heights.
        x : ndarray
            x coordinates.
        y : ndarray
            y coordinates.

    Created by: David Bergström (2010-07-26)
    Last modified by: Heming Qin (2024-12-01)
    """
    # Determine if isotropic: if N_y, rL_y, and cly are not provided, use N_x, rL_x, clx for both axes.
    if N_y is None or rL_y is None or cly is None:
        N_y = N_x
        rL_y = rL_x
        cly = clx

    # Generate coordinates
    x = np.linspace(-rL_x / 2, rL_x / 2, N_x)
    y = np.linspace(-rL_y / 2, rL_y / 2, N_y)
    X, Y = np.meshgrid(x, y)

    # Generate an uncorrelated Gaussian random surface with RMS height h
    Z = h * np.random.randn(N_y, N_x)

    # Create the exponential filter matrix for a non-isotropic surface
    F = np.exp(- (np.abs(X) / (clx / 2.0) + np.abs(Y) / (cly / 2.0)))

    # Convolution via FFTs
    fft_Z = np.fft.fft2(Z)
    fft_F = np.fft.fft2(F)
    conv = np.fft.ifft2(fft_Z * fft_F)

    # Normalization factor depends on whether the surface is isotropic or not.
    if N_y == N_x and rL_y == rL_x and clx == cly:
        # Isotropic normalization: similar to rsgene2D_version original
        factor = 2.0 * rL_x / (N_x * clx)
    else:
        # Non-isotropic normalization: using separate lengths for x and y.
        factor = (rL_x / N_x + rL_y / N_y) / np.sqrt(clx * cly)

    f = factor * conv
    f = np.real(f)  # Take the real part

    return f, x, y

# Example usage:
if __name__ == '__main__':
    # Isotropic example: only provide one set of parameters
    f_iso, x_iso, y_iso = rsgene2D(128, rL_x=10.0, h=1.0, clx=2.0)
    print("Isotropic f[0,0] =", f_iso[0, 0])

    # Non-isotropic example: provide different parameters for x and y
    f_aniso, x_aniso, y_aniso = rsgene2D(128, 128, 10.0, 10.0, 1.0, 2.0, 3.0)
    print("Non-isotropic f[0,0] =", f_aniso[0, 0])
