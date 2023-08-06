from .core import Mesh2D
from .core import meshing_timer
import gmsh


class GmshEncapsulation:
    class geom:
        @staticmethod
        def add_point(x, y, z, mesh_size=0, tag=-1):
            return gmsh.model.occ.add_point(x, y, z, meshSize=mesh_size, tag=tag)

        @staticmethod
        def add_rectangle(x, y, z, dx, dy, tag=-1, round_radius=0):
            return gmsh.model.occ.add_rectangle(x, y, z, dx, dy, tag=tag, roundedRadius=round_radius)

        @staticmethod
        def fragment(object_dim_tags, tool_dim_tags):
            gmsh.model.occ.fragment(object_dim_tags, tool_dim_tags, removeObject=True, removeTool=True)

        @staticmethod
        def synchronize(show_geom=False):
            gmsh.model.occ.synchronize()
            if show_geom: gmsh.fltk.run()

    class mesh:
        @staticmethod
        def recombine():
            gmsh.model.mesh.recombine()

        @staticmethod
        def set_size(dim_tags, size):
            gmsh.model.mesh.set_size(dim_tags, size)


class General2DCase(Mesh2D, GmshEncapsulation):
    def __init__(self):
        Mesh2D.__init__(self)

        self._dim = 2
        self._node_per_face = 2

        self._gmsh_element_type = 2  # 2 means triangle.
        self._face_per_cell = 3
        self._node_per_cell = 3

    @meshing_timer
    def generate_unstructured(self, show_mesh=False):

        gmsh.model.mesh.generate(2)
        if self._gmsh_element_type == 3: gmsh.model.mesh.recombine()
        if show_mesh: gmsh.fltk.run()

        self._generate_topology()