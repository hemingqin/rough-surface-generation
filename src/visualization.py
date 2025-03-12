"""
Visualization module for rough surface generation.
"""

import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_surface_3d(x, y, z, title="3D Surface Plot", colormap='viridis', interactive=True):
    """
    Create a 3D surface plot using either plotly (interactive) or matplotlib.
    
    Parameters:
        x, y: Coordinate meshgrids
        z: Surface heights
        title: Plot title
        colormap: Color scheme for the surface
        interactive: If True, use plotly for interactive plot, else use matplotlib
    
    Returns:
        fig: Figure object (plotly.graph_objects.Figure or matplotlib.figure.Figure)
    """
    if interactive:
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale=colormap)])
        fig.update_layout(
            title=title,
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Height'
            )
        )
    else:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(x, y, z, cmap=colormap)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Height')
        ax.set_title(title)
        fig.colorbar(surf)
    
    return fig

def plot_surface_2d(x, y, z, title="Surface Height Map", colormap='viridis'):
    """
    Create a 2D height map of the surface.
    
    Parameters:
        x, y: Coordinate meshgrids
        z: Surface heights
        title: Plot title
        colormap: Color scheme for the height map
    
    Returns:
        fig: matplotlib.figure.Figure object
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.pcolormesh(x, y, z, cmap=colormap, shading='auto')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label='Height')
    
    return fig

def plot_height_distribution(z, bins=50, title="Height Distribution"):
    """
    Plot the height distribution histogram.
    
    Parameters:
        z: Surface heights
        bins: Number of histogram bins
        title: Plot title
    
    Returns:
        fig: matplotlib.figure.Figure object
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(z.flatten(), bins=bins, density=True)
    ax.set_xlabel('Height')
    ax.set_ylabel('Density')
    ax.set_title(title)
    
    return fig 