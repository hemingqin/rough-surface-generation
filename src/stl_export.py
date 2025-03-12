"""
STL export module for rough surface generation.
"""

import numpy as np
from stl import mesh

def export_to_stl(x, y, z, filename, base_thickness=1.0):
    """
    Export a surface to an STL file.
    
    Parameters:
        x, y: Coordinate meshgrids
        z: Surface heights
        filename: Output STL filename
        base_thickness: Thickness of the base below the surface
        
    Returns:
        None
    """
    rows, cols = z.shape
    vertices = []
    faces = []
    
    # Create vertices for top surface
    for i in range(rows):
        for j in range(cols):
            vertices.append([x[i,j], y[i,j], z[i,j]])
    
    # Create vertices for bottom surface
    for i in range(rows):
        for j in range(cols):
            vertices.append([x[i,j], y[i,j], z[i,j] - base_thickness])
    
    vertices = np.array(vertices)
    
    # Create faces for top surface
    for i in range(rows - 1):
        for j in range(cols - 1):
            # First triangle
            v1 = i * cols + j
            v2 = i * cols + (j + 1)
            v3 = (i + 1) * cols + j
            faces.append([v1, v2, v3])
            
            # Second triangle
            v1 = (i + 1) * cols + j
            v2 = i * cols + (j + 1)
            v3 = (i + 1) * cols + (j + 1)
            faces.append([v1, v2, v3])
    
    # Create faces for bottom surface (inverted orientation)
    offset = rows * cols
    for i in range(rows - 1):
        for j in range(cols - 1):
            # First triangle
            v1 = offset + i * cols + j
            v2 = offset + (i + 1) * cols + j
            v3 = offset + i * cols + (j + 1)
            faces.append([v1, v2, v3])
            
            # Second triangle
            v1 = offset + (i + 1) * cols + j
            v2 = offset + (i + 1) * cols + (j + 1)
            v3 = offset + i * cols + (j + 1)
            faces.append([v1, v2, v3])
    
    # Create side faces
    for i in range(rows - 1):
        # Left side
        v1 = i * cols
        v2 = (i + 1) * cols
        v3 = offset + i * cols
        faces.append([v1, v2, v3])
        
        v1 = (i + 1) * cols
        v2 = offset + (i + 1) * cols
        v3 = offset + i * cols
        faces.append([v1, v2, v3])
        
        # Right side
        v1 = i * cols + (cols - 1)
        v2 = offset + i * cols + (cols - 1)
        v3 = (i + 1) * cols + (cols - 1)
        faces.append([v1, v2, v3])
        
        v1 = (i + 1) * cols + (cols - 1)
        v2 = offset + i * cols + (cols - 1)
        v3 = offset + (i + 1) * cols + (cols - 1)
        faces.append([v1, v2, v3])
    
    # Create front and back faces
    for j in range(cols - 1):
        # Front side
        v1 = j
        v2 = offset + j
        v3 = j + 1
        faces.append([v1, v2, v3])
        
        v1 = j + 1
        v2 = offset + j
        v3 = offset + j + 1
        faces.append([v1, v2, v3])
        
        # Back side
        v1 = (rows - 1) * cols + j
        v2 = (rows - 1) * cols + j + 1
        v3 = offset + (rows - 1) * cols + j
        faces.append([v1, v2, v3])
        
        v1 = (rows - 1) * cols + j + 1
        v2 = offset + (rows - 1) * cols + j + 1
        v3 = offset + (rows - 1) * cols + j
        faces.append([v1, v2, v3])
    
    faces = np.array(faces)
    
    # Create the mesh
    surface = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface.vectors[i][j] = vertices[f[j],:]
    
    # Save the mesh to STL file
    surface.save(filename) 