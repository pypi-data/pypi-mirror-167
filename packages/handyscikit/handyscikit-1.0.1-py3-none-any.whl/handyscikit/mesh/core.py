from ..common.print_related import cprint
import gmsh
import math
import numpy as np
import time


class MeshBase:
    def __init__(self):
        if not gmsh.is_initialized(): gmsh.initialize()
        gmsh.option.set_number("General.Terminal", 0)

        self._cell_num = None
        self._dim = None
        self._face_num = None
        self._face_per_cell = None
        self._node_num = None
        self._node_per_cell = None
        self._node_per_face = None

        self._cell_cell = None
        self._cell_volume = None
        self._cell_face = None
        self._cell_center = None
        self._cells = None
        self._face_area = None
        self._face_cell = None
        self._face_center = None
        self._face_norm = None
        self._face_vector = None
        self._faces = None
        self._nodes = None

        self._gmsh_element_type = None

    def clear_gmsh(self):
        gmsh.clear()

    def _calc_face_area(self):
        assert False

    def _calc_face_center(self):
        assert False

    def _calc_face_norm(self):
        assert False

    def _calc_face_vector(self):
        assert False

    def _generate_topology(self):
        self.__make_nodes()
        self.__make_cells()
        self._make_faces_and_cell_face()
        self.__calc_face_cell()
        self.__calc_cell_cell()

        self.__calc_cell_center()
        self.__calc_cell_volume()
        self._calc_face_area()
        self._calc_face_center()
        self._calc_face_norm()
        self._calc_face_vector()

    def _make_faces_and_cell_face(self):
        assert False

    def __calc_cell_center(self):
        bary_centers = gmsh.model.mesh.get_barycenters(self.gmsh_element_type, -1, 0, 0)
        self._cell_center = bary_centers.reshape([self._cell_num, 3])
        self._cell_center = self._cell_center.astype(np.float32)

    def __calc_cell_cell(self):
        self._cell_cell = np.full([self._cell_num, self._face_per_cell], fill_value=-1, dtype=np.int32)
        for i in range(self._face_num):
            if self._face_cell[i, 0] != -1 and self._face_cell[i, 1] != -1:
                for j in range(self._face_per_cell):
                    if self._cell_cell[self._face_cell[i, 0], j] == -1:
                        self._cell_cell[self._face_cell[i, 0], j] = self._face_cell[i, 1]
                        break
                for j in range(self._face_per_cell):
                    if self._cell_cell[self._face_cell[i, 1], j] == -1:
                        self._cell_cell[self._face_cell[i, 1], j] = self._face_cell[i, 0]
                        break

    def __calc_cell_volume(self):
        self._cell_volume = np.zeros([self._cell_num], dtype=np.float32)

        if self._gmsh_element_type == 3:
            for i in range(self._cell_num):
                vector_0 = self._nodes[self._cells[i, 0]] - self._nodes[self._cells[i, 1]]
                vector_1 = self._nodes[self._cells[i, 0]] - self._nodes[self._cells[i, 3]]
                self._cell_volume[i] = abs(np.cross(vector_0, vector_1)[2])  # 3D vector cross makes a new vector.
        elif self._gmsh_element_type == 2:
            for i in range(self.cell_num):
                node_0 = self._nodes[self._cells[i, 0]]
                node_1 = self._nodes[self._cells[i, 1]]
                node_2 = self._nodes[self._cells[i, 2]]
                self._cell_volume[i] = ((node_1[0] - node_0[0])*(node_2[1] - node_0[1]) -
                                        (node_1[1] - node_0[1])*(node_2[0] - node_0[0]))/2
        else:
            self._cell_volume = None

    def __calc_face_cell(self):
        self._face_cell = np.full([self._face_num, 2], fill_value=-1, dtype=np.int32)
        for i in range(self._cell_num):
            for j in range(self._face_per_cell):
                if self._face_cell[self._cell_face[i, j], 0] == -1:
                    self._face_cell[self._cell_face[i, j], 0] = i
                else:
                    self._face_cell[self._cell_face[i, j], 1] = i

    def __make_cells(self):
        (cell_tags, node_tags) = gmsh.model.mesh.get_elements_by_type(self._gmsh_element_type)  # 3 means quadrilateral.
        self._cells = node_tags.reshape([-1, self._node_per_cell])
        self._cells = self._cells.astype(np.int32)
        self._cells -= 1  # Gmsh cells index starts from 1, but index start from zero, transfer it.
        self._cell_num = self._cells.shape[0]

    def __make_nodes(self):
        (node_tags, node_coordinates, unuse) = gmsh.model.mesh.get_nodes()
        self._node_num = node_tags.size
        self._nodes = node_coordinates.reshape([-1, 3])
        self._nodes = self._nodes.astype(np.float32)

    @property
    def cell_cell(self):
        return self._cell_cell

    @property
    def cell_center(self):
        return self._cell_center

    @property
    def cell_face(self):
        return self._cell_face

    @property
    def cell_num(self):
        return self._cell_num

    @property
    def cell_volume(self):
        return self._cell_volume

    @property
    def cells(self):
        return self._cells

    @property
    def dim(self):
        return self._dim

    @property
    def face_cell(self):
        return self._face_cell

    @property
    def face_center(self):
        return self._face_center

    @property
    def face_area(self):
        return self._face_area

    @property
    def face_norm(self):
        return self._face_norm

    @property
    def face_num(self):
        return self._face_num

    @property
    def face_per_cell(self):
        return self._face_per_cell

    @property
    def face_vector(self):
        return self._face_vector

    @property
    def faces(self):
        return self._faces

    @property
    def gmsh_element_type(self):
        return self._gmsh_element_type

    @property
    def node_num(self):
        return self._node_num

    @property
    def node_per_cell(self):
        return self._node_per_cell

    @property
    def node_per_face(self):
        return self._node_per_face

    @property
    def nodes(self):
        return self._nodes


class Mesh2D(MeshBase):
    def __init__(self):
        MeshBase.__init__(self)

    def _calc_face_area(self):
        self._face_area = np.zeros([self._face_num], dtype=np.float32)

        for i in range(self.face_num):
            self._face_area[i] = np.linalg.norm(self._nodes[self._faces[i,0]] - self._nodes[self._faces[i, 1]])

    def _calc_face_center(self):
        self._face_center = np.zeros([self._face_num, 3], dtype=np.float32)

        for i in range(self._face_num):
            self._face_center[i] = (self._nodes[self._faces[i,0]] + self._nodes[self._faces[i,1]])/2

    def _calc_face_norm(self):
        self._face_norm = np.zeros([self._face_num, 3], dtype=np.float32)

        for i in range(self._face_num):
            node0 = self._nodes[self._faces[i, 0]]
            node1 = self._nodes[self._faces[i, 1]]
            if node0[1] - node1[1] == 0:
                self._face_norm[i, 1] = 1
            else:
                tmp = (node0[0] - node1[0])/(node1[1] - node0[1])
                self._face_norm[i, 0] = 1/(1 + tmp**2)**0.5
                self._face_norm[i, 1] = tmp/(1 + tmp**2)**0.5
            if np.dot(self._face_norm[i], self._cell_center[self._face_cell[i, 0]] - self._face_center[i]) > 0:
                self._face_norm[i] *= -1

    def _calc_face_vector(self):
        self._face_vector = np.zeros([self._face_num, 3], dtype=np.float32)

        for i in range(self._face_num):
            self._face_vector[i] = self._face_norm[i]*self._face_area[i]

    def _make_faces_and_cell_face(self):
        gmsh.model.mesh.create_edges()

        element_node_tags = gmsh.model.mesh.get_element_edge_nodes(self._gmsh_element_type)
        element_node_num = element_node_tags.size

        (face_tags, unuse) = gmsh.model.mesh.get_edges(element_node_tags)  # Inner face repeated in face tags.
        element_face_num = face_tags.size

        # Calculate face number.
        self._face_num = 0
        tmp = np.full(element_face_num, fill_value=-1)
        for i in range(element_face_num):
            if tmp[face_tags[i]] == -1:
                tmp[face_tags[i]] = 0
                self._face_num += 1

        self._faces = np.zeros([self._face_num, self._node_per_face], dtype=np.int32)
        for i in range(element_node_num):
            self._faces[int(face_tags[i//2])-1, i%2] = element_node_tags[i]-1

        self._cell_face = face_tags.reshape([self._cell_num, self._face_per_cell])
        self._cell_face = self._cell_face.astype(np.int32)
        self._cell_face -= 1


def meshing_timer(func):
    def wrapper_func(*args, **kwargs):
        cprint("[handyscikit | Mesh] Meshing start.", color="purple")
        start_time = time.time()

        func(*args, **kwargs)

        spend_time = time.time() - start_time
        cprint("[handyscikit | Mesh] Meshing finished and takes %f seconds." % (spend_time), color="purple")

    return wrapper_func