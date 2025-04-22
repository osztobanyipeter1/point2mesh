import open3d as o3d
import os

# ABSZOLÚT ÚTVONAL megadása
obj_path = "/home/buvr_tp4/point2mesh/data/output_mesh.obj"
#obj_path = "/home/buvr_tp4/point2mesh/checkpoints/boat/iter_0392.obj"

# Load the OBJ file
mesh = o3d.io.read_triangle_mesh(obj_path)  # Replace with your file path

# Check if the mesh is valid
if not mesh.has_vertices():
    print("Error: No vertices found in the mesh!")
else:
    # Compute normals for better visualization (optional)
    mesh.compute_vertex_normals()

    # Visualize
    o3d.visualization.draw_geometries([mesh], window_name="3D Model")