import sys
import igl, tetgen, pyvista as pv, numpy as np
from utilities import *

# Read a triangulated mesh
n = len(sys.argv)
if n < 4:
    raise ValueError('Please provide: \n - an input triangulated mesh (.obj), \n - a path to save the unoptimized tet mesh (.mesh), \n - a path to save the optimized standing tet mesh (.mesh).')
else:
    input_mesh_file = sys.argv[1]
    unopt_mesh_file = sys.argv[2]
    opt_mesh_file = sys.argv[3]
    M = igl.read_obj(input_mesh_file)
    V_tri, F_tri = M[0], M[3]

# Tetrahedralize the mesh
# Note: the triangulated mesh needs to be *closed*
tet = tetgen.TetGen(V_tri, F_tri)
V, T = tet.tetrahedralize(order=1, mindihedral=20, minratio=1.5)  # docs (if needed): https://tetgen.pyvista.org/api.html
unopt_mesh = define_pyvista_mesh(V, T)

# --------------------
# TODO: Make it stand!
# --------------------
opt_mesh = unopt_mesh  # <---- your code goes here 

# Visulization
pv.global_theme.background = 'white'
p = pv.Plotter()
p.add_mesh_clip_plane(opt_mesh, normal=(0, 0, -1))
p.add_mesh(opt_mesh, 'r', 'wireframe')
p.add_axes()
p.add_floor(offset=0.001)
p.show()

# Save output meshes to file
pv.save_meshio(unopt_mesh_file, unopt_mesh)
pv.save_meshio(opt_mesh_file, opt_mesh)
