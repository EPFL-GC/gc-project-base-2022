import pyvista as pv
import numpy as np
from scipy import spatial


def define_pyvista_mesh(V, elems):
    """
    Return a mesh in pyvista format.

    Input:
    - V : np.array (|V|, 3)
        The array of vertices positions.
        Contains the coordinates of the i-th vertex in i-th row.
    - elems : np.array (|elems|, <3, 4>)
        The array of trianglar faces or tetrahedral elements.
    Output:
    - mesh : pyvista.core.pointset.UnstructuredGrid
        The mesh in a format that can be plotted by pyvista.

    For more information see: https://docs.pyvista.org/examples/00-load/create-unstructured-surface.html#create-unstructured-example
    """
    if elems.shape[1] == 3:  # triangles
        n_tri = elems.shape[0]
        F_pyvista = np.column_stack((3*np.ones(n_tri), elems)).astype(int)
        celltypes = np.full(n_tri, fill_value=pv.CellType.TRIANGLE, dtype=np.uint8)
        mesh = pv.UnstructuredGrid(F_pyvista, celltypes, V)
    elif elems.shape[1] == 4:  # tets
        n_tets = elems.shape[0]
        T_pyvista = np.column_stack((4*np.ones(n_tets), elems)).astype(int)
        celltypes = np.full(n_tets, fill_value=pv.CellType.TETRA, dtype=np.uint8)
        mesh = pv.UnstructuredGrid(T_pyvista, celltypes, V)
    return mesh


def compute_convex_hull_indices(P):
    """
    Given a set of points, return the indices of the points that define the convex hull.
    Note: when computing a 2D convex hull, the input points should be 2-dimensional.

    Input:
    - P : np.array (|points|, d)
        An array of d-dimensional points.
    Output:
    - indices : np.array (|boundary_points|, d)
        An array containing the indices of the points that define the boundary of the convex hull.

    For more information see: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
    """
    indices = spatial.ConvexHull(P).vertices
    return indices