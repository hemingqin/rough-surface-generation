"""
Example usage of surface generation and visualization.
"""

from parametric_surface import generate_parametric_surface
from spectral_surface import generate_random_gaussian_surface
from visualization import plot_surface_3d, plot_surface_2d, plot_height_distribution

# Generate surfaces using both methods
print("Generating parametric surface...")
S1, S2, param_surface = generate_parametric_surface(N=10, b=1.8, factor=0.01)

print("Generating spectral surface...")
spec_surface, x, y = generate_random_gaussian_surface(N_x=128, h=0.001, clx=2.0)

# Create visualizations
print("Creating visualizations...")

# 3D plots
param_fig = plot_surface_3d(S1, S2, param_surface, title="Parametric Surface")
param_fig.show()

spec_fig = plot_surface_3d(x, y, spec_surface, title="Spectral Surface")
spec_fig.show()

# 2D height maps
plot_surface_2d(S1, S2, param_surface, title="Parametric Surface Height Map")
plot_surface_2d(x, y, spec_surface, title="Spectral Surface Height Map")

# Height distributions
plot_height_distribution(param_surface, title="Parametric Surface Heights")
plot_height_distribution(spec_surface, title="Spectral Surface Heights")

print("Done! Close the plot windows to exit.") 