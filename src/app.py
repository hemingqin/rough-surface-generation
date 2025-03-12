"""
Streamlit app for interactive rough surface generation and visualization.
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from parametric_surface import generate_parametric_surface
from spectral_surface import generate_random_gaussian_surface
from stl_export import export_to_stl
import tempfile
import os

st.set_page_config(page_title="Rough Surface Generator", layout="wide")

st.title("Rough Surface Generator")

# Sidebar for parameters
st.sidebar.header("Generation Parameters")

# Method selection
method = st.sidebar.radio(
    "Surface Generation Method",
    ["Parametric (Double-Sum)", "Spectral (FFT-Based)"]
)

if method == "Parametric (Double-Sum)":
    # Parameters for parametric method
    N = st.sidebar.slider("Summation Limit (N)", 5, 50, 10)
    b = st.sidebar.slider("Spectral Exponent (β)", 1.0, 3.0, 1.8)
    factor = st.sidebar.slider("Scale Factor", 0.001, 0.1, 0.01)
    num_points = st.sidebar.slider("Grid Points", 50, 200, 101)
    
    if st.sidebar.button("Generate Surface"):
        with st.spinner("Generating surface..."):
            S1, S2, surface = generate_parametric_surface(
                N=N,
                b=b,
                factor=factor,
                num_points=num_points
            )
            
            # Create 3D surface plot
            fig = go.Figure(data=[go.Surface(x=S1, y=S2, z=surface)])
            fig.update_layout(
                title="Generated Rough Surface (Parametric Method)",
                scene=dict(
                    xaxis_title="X",
                    yaxis_title="Y",
                    zaxis_title="Height"
                )
            )
            
            # Display the plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Statistics
            st.subheader("Surface Statistics")
            col1, col2, col3 = st.columns(3)
            col1.metric("RMS Height", f"{np.std(surface):.6f}")
            col2.metric("Mean Height", f"{np.mean(surface):.6f}")
            col3.metric("Peak-to-Valley", f"{np.max(surface) - np.min(surface):.6f}")
            
            # Export options
            st.subheader("Export Options")
            if st.button("Export to STL"):
                with tempfile.NamedTemporaryFile(delete=False, suffix='.stl') as tmp:
                    export_to_stl(S1, S2, surface, tmp.name)
                    with open(tmp.name, 'rb') as f:
                        st.download_button(
                            label="Download STL file",
                            data=f,
                            file_name="rough_surface.stl",
                            mime="application/octet-stream"
                        )
                    os.unlink(tmp.name)

else:  # Spectral (FFT-Based) method
    # Parameters for spectral method
    N_x = st.sidebar.slider("Grid Points (X)", 50, 200, 128)
    rL_x = st.sidebar.slider("Surface Length (X)", 1.0, 20.0, 10.0)
    h = st.sidebar.slider("RMS Height", 0.0001, 0.01, 0.001)
    clx = st.sidebar.slider("Correlation Length", 0.1, 5.0, 2.0)
    
    # Option for isotropic/anisotropic
    isotropic = st.sidebar.checkbox("Isotropic Surface", value=True)
    
    if not isotropic:
        N_y = st.sidebar.slider("Grid Points (Y)", 50, 200, 128)
        rL_y = st.sidebar.slider("Surface Length (Y)", 1.0, 20.0, 10.0)
        cly = st.sidebar.slider("Correlation Length (Y)", 0.1, 5.0, 2.0)
    else:
        N_y = None
        rL_y = None
        cly = None
    
    if st.sidebar.button("Generate Surface"):
        with st.spinner("Generating surface..."):
            surface, x, y = generate_random_gaussian_surface(
                N_x=N_x,
                N_y=N_y,
                rL_x=rL_x,
                rL_y=rL_y,
                h=h,
                clx=clx,
                cly=cly
            )
            
            # Create meshgrid for plotting
            X, Y = np.meshgrid(x, y)
            
            # Create 3D surface plot
            fig = go.Figure(data=[go.Surface(x=X, y=Y, z=surface)])
            fig.update_layout(
                title="Generated Rough Surface (Spectral Method)",
                scene=dict(
                    xaxis_title="X",
                    yaxis_title="Y",
                    zaxis_title="Height"
                )
            )
            
            # Display the plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Statistics
            st.subheader("Surface Statistics")
            col1, col2, col3 = st.columns(3)
            col1.metric("RMS Height", f"{np.std(surface):.6f}")
            col2.metric("Mean Height", f"{np.mean(surface):.6f}")
            col3.metric("Peak-to-Valley", f"{np.max(surface) - np.min(surface):.6f}")
            
            # Export options
            st.subheader("Export Options")
            if st.button("Export to STL"):
                with tempfile.NamedTemporaryFile(delete=False, suffix='.stl') as tmp:
                    export_to_stl(X, Y, surface, tmp.name)
                    with open(tmp.name, 'rb') as f:
                        st.download_button(
                            label="Download STL file",
                            data=f,
                            file_name="rough_surface.stl",
                            mime="application/octet-stream"
                        )
                    os.unlink(tmp.name)

# Add documentation in the sidebar
with st.sidebar.expander("Documentation"):
    st.markdown("""
    ### Parametric (Double-Sum) Method
    Uses a double summation of cosine terms with power-law amplitudes and random phases.
    - **N**: Summation limit for modes
    - **β**: Spectral exponent controlling roughness
    - **Scale Factor**: Overall amplitude scaling
    
    ### Spectral (FFT-Based) Method
    Uses inverse Fourier transform with Gaussian correlation function.
    - **RMS Height**: Root mean square height of the surface
    - **Correlation Length**: Distance over which heights become uncorrelated
    - **Surface Length**: Physical size of the surface
    - **Grid Points**: Resolution of the surface
    """) 