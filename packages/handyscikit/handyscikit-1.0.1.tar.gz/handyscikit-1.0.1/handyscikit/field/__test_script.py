import gmsh
import handyscikit as hsk
import numpy as np

class BoundaryCondition:
    class Dirichlet:
        @staticmethod
        def function_cos():
            mesh = hsk.mesh.SquareCase(1)
            mesh.generate_structured([3, 3])

            fields = hsk.field.PhysicalFields()

            empty_field = hsk.field.PhysicalField(mesh)
            empty_field.set_boundary_as_dirichlet([mesh.boundary_up, mesh.boundary_down], "cos")
            empty_field.set_boundary_as_dirichlet([mesh.boundary_left, mesh.boundary_right], 9)
            fields.add_field(empty_field)

            fields.generate_info()

            assert empty_field.face_info[0, 0] == 1.0 and (empty_field.face_info[0, 1] - 0.5) < 1e-6
            assert empty_field.face_info[1, 0] == 1.0 and empty_field.face_info[1, 1] == -1.0
            assert empty_field.face_info[2, 0] == 1.0 and (empty_field.face_info[2, 1] - 0.5) < 1e-6
            assert empty_field.face_info[3, 0] == 1.0 and empty_field.face_info[3, 1] == 9.0
            assert empty_field.face_info[4, 0] == 1.0 and empty_field.face_info[4, 1] == 9.0
            assert empty_field.face_info[5, 0] == 1.0 and empty_field.face_info[5, 1] == 9.0
            assert empty_field.face_info[6, 0] == 1.0 and (empty_field.face_info[6, 1] - 0.5) < 1e-6
            assert empty_field.face_info[7, 0] == 1.0 and empty_field.face_info[7, 1] == -1.0
            assert empty_field.face_info[8, 0] == 1.0 and (empty_field.face_info[8, 1] - 0.5) < 1e-6
            assert empty_field.face_info[9, 0] == 1.0 and empty_field.face_info[9, 1] == 9.0
            assert empty_field.face_info[10, 0] == 1.0 and empty_field.face_info[10, 1] == 9.0
            assert empty_field.face_info[11, 0] == 1.0 and empty_field.face_info[11, 1] == 9.0
            assert empty_field.face_info[12, 0] == 0.0 and empty_field.face_info[12, 1] == 0.0
            assert empty_field.face_info[13, 0] == 0.0 and empty_field.face_info[13, 1] == 0.0
            assert empty_field.face_info[14, 0] == 0.0 and empty_field.face_info[14, 1] == 0.0
            assert empty_field.face_info[15, 0] == 0.0 and empty_field.face_info[15, 1] == 0.0
            assert empty_field.face_info[16, 0] == 0.0 and empty_field.face_info[16, 1] == 0.0
            assert empty_field.face_info[17, 0] == 0.0 and empty_field.face_info[17, 1] == 0.0
            assert empty_field.face_info[18, 0] == 0.0 and empty_field.face_info[18, 1] == 0.0
            assert empty_field.face_info[19, 0] == 0.0 and empty_field.face_info[19, 1] == 0.0
            assert empty_field.face_info[20, 0] == 0.0 and empty_field.face_info[20, 1] == 0.0
            assert empty_field.face_info[21, 0] == 0.0 and empty_field.face_info[21, 1] == 0.0
            assert empty_field.face_info[22, 0] == 0.0 and empty_field.face_info[22, 1] == 0.0
            assert empty_field.face_info[23, 0] == 0.0 and empty_field.face_info[23, 1] == 0.0

            hsk.cprint("[BoundaryCondition Test] Dirichlet function cos test passed.", color="green")

        @staticmethod
        def scalar():
            mesh = hsk.mesh.SquareCase(1)
            mesh.generate_structured([2, 2])

            fields = hsk.field.PhysicalFields()

            empty_field = hsk.field.PhysicalField(mesh)
            empty_field.set_boundary_as_dirichlet([mesh.boundary_up], 1)
            empty_field.set_boundary_as_dirichlet([mesh.boundary_down], 2)
            empty_field.set_boundary_as_dirichlet([mesh.boundary_left], 3)
            empty_field.set_boundary_as_dirichlet([mesh.boundary_right], 4)
            fields.add_field(empty_field)

            fields.generate_info()

            assert empty_field.face_info[0, 0] == 1.0 and empty_field.face_info[0, 1] == 2.0
            assert empty_field.face_info[1, 0] == 1.0 and empty_field.face_info[1, 1] == 2.0
            assert empty_field.face_info[2, 0] == 1.0 and empty_field.face_info[2, 1] == 4.0
            assert empty_field.face_info[3, 0] == 1.0 and empty_field.face_info[3, 1] == 4.0
            assert empty_field.face_info[4, 0] == 1.0 and empty_field.face_info[4, 1] == 1.0
            assert empty_field.face_info[5, 0] == 1.0 and empty_field.face_info[5, 1] == 1.0
            assert empty_field.face_info[6, 0] == 1.0 and empty_field.face_info[6, 1] == 3.0
            assert empty_field.face_info[7, 0] == 1.0 and empty_field.face_info[7, 1] == 3.0
            assert empty_field.face_info[8, 0] == 0.0 and empty_field.face_info[8, 1] == 0.0
            assert empty_field.face_info[9, 0] == 0.0 and empty_field.face_info[9, 1] == 0.0
            assert empty_field.face_info[10, 0] == 0.0 and empty_field.face_info[10, 1] == 0.0
            assert empty_field.face_info[11, 0] == 0.0 and empty_field.face_info[11, 1] == 0.0

            hsk.cprint("[BoundaryCondition Test] Dirichlet scalar test passed.", color="green")

    class Open:
        @staticmethod
        def basic():
            mesh = hsk.mesh.SquareCase(1)
            mesh.generate_structured([2, 2])

            fields = hsk.field.PhysicalFields()
            empty_field = hsk.field.PhysicalField(mesh)
            empty_field.set_boundary_as_open([mesh.boundary_up, mesh.boundary_down])
            fields.add_field(empty_field)
            fields.generate_info()

            assert empty_field.face_info[0, 0] == 5
            assert empty_field.face_info[1, 0] == 5
            assert empty_field.face_info[2, 0] == 0
            assert empty_field.face_info[3, 0] == 0
            assert empty_field.face_info[4, 0] == 5
            assert empty_field.face_info[5, 0] == 5
            assert empty_field.face_info[6, 0] == 0
            assert empty_field.face_info[7, 0] == 0
            assert empty_field.face_info[8, 0] == 0
            assert empty_field.face_info[9, 0] == 0
            assert empty_field.face_info[10, 0] == 0
            assert empty_field.face_info[11, 0] == 0

            hsk.cprint("[BoundaryCondition Test] Open test passed.", color="green")

    class Periodic:
        @staticmethod
        def basic():
            mesh = hsk.mesh.SquareCase(1)
            mesh.generate_structured([3, 3])

            fields = hsk.field.PhysicalFields()

            empty = hsk.field.PhysicalField(mesh)
            empty.set_boundary_as_periodic([mesh.boundary_up, mesh.boundary_down])
            empty.set_boundary_as_periodic([mesh.boundary_left, mesh.boundary_right])
            fields.add_field(empty)

            fields.generate_info()

            assert empty.face_info[0, 0] == 4.0 and empty.face_info[0, 1] == 8.0 and empty.face_info[0, 2] == 2.0
            assert empty.face_info[1, 0] == 4.0 and empty.face_info[1, 1] == 7.0 and empty.face_info[1, 2] == 5.0
            assert empty.face_info[2, 0] == 4.0 and empty.face_info[2, 1] == 6.0 and empty.face_info[2, 2] == 8.0
            assert empty.face_info[3, 0] == 4.0 and empty.face_info[3, 1] == 11.0 and empty.face_info[3, 2] == 0.0
            assert empty.face_info[4, 0] == 4.0 and empty.face_info[4, 1] == 10.0 and empty.face_info[4, 2] == 1.0
            assert empty.face_info[5, 0] == 4.0 and empty.face_info[5, 1] == 9.0 and empty.face_info[5, 2] == 2.0
            assert empty.face_info[6, 0] == 4.0 and empty.face_info[6, 1] == 2.0 and empty.face_info[6, 2] == 6.0
            assert empty.face_info[7, 0] == 4.0 and empty.face_info[7, 1] == 1.0 and empty.face_info[7, 2] == 3.0
            assert empty.face_info[8, 0] == 4.0 and empty.face_info[8, 1] == 0.0 and empty.face_info[8, 2] == 0.0
            assert empty.face_info[9, 0] == 4.0 and empty.face_info[9, 1] == 5.0 and empty.face_info[9, 2] == 8.0
            assert empty.face_info[10, 0] == 4.0 and empty.face_info[10, 1] == 4.0 and empty.face_info[10, 2] == 7.0
            assert empty.face_info[11, 0] == 4.0 and empty.face_info[11, 1] == 3.0 and empty.face_info[11, 2] == 6.0
            assert empty.face_info[12, 0] == 0.0 and empty.face_info[12, 1] == 0.0 and empty.face_info[12, 2] == 0.0
            assert empty.face_info[13, 0] == 0.0 and empty.face_info[13, 1] == 0.0 and empty.face_info[13, 2] == 0.0
            assert empty.face_info[14, 0] == 0.0 and empty.face_info[14, 1] == 0.0 and empty.face_info[14, 2] == 0.0
            assert empty.face_info[15, 0] == 0.0 and empty.face_info[15, 1] == 0.0 and empty.face_info[15, 2] == 0.0
            assert empty.face_info[16, 0] == 0.0 and empty.face_info[16, 1] == 0.0 and empty.face_info[16, 2] == 0.0
            assert empty.face_info[17, 0] == 0.0 and empty.face_info[17, 1] == 0.0 and empty.face_info[17, 2] == 0.0
            assert empty.face_info[18, 0] == 0.0 and empty.face_info[18, 1] == 0.0 and empty.face_info[18, 2] == 0.0
            assert empty.face_info[19, 0] == 0.0 and empty.face_info[19, 1] == 0.0 and empty.face_info[19, 2] == 0.0
            assert empty.face_info[20, 0] == 0.0 and empty.face_info[20, 1] == 0.0 and empty.face_info[20, 2] == 0.0
            assert empty.face_info[21, 0] == 0.0 and empty.face_info[21, 1] == 0.0 and empty.face_info[21, 2] == 0.0
            assert empty.face_info[22, 0] == 0.0 and empty.face_info[22, 1] == 0.0 and empty.face_info[22, 2] == 0.0
            assert empty.face_info[23, 0] == 0.0 and empty.face_info[23, 1] == 0.0 and empty.face_info[23, 2] == 0.0

            hsk.cprint("[BoundaryCondition Test] Periodic test passed.", color="green")


class InitialCondition:
    @staticmethod
    def function():
        mesh = hsk.mesh.SquareCase(2, coordinate=[-1, -1])
        mesh.generate_structured([3, 3])

        fields = hsk.field.PhysicalFields()

        empty_field = hsk.field.PhysicalField(mesh)
        gauss = hsk.analytical.GaussianHill(0.05, np.array([[0.001, 0], [0, 0.001]]))
        empty_field.set_initial_condition_by_func(gauss.calc_initial_condition)
        fields.add_field(empty_field)

        fields.generate_info()

        error = 1e-6
        assert empty_field.initial_condition[0] == 0.0
        assert abs(empty_field.initial_condition[1] - 2.489108e-39) < error
        assert empty_field.initial_condition[2] == 0.0
        assert abs(empty_field.initial_condition[3] - 2.489147e-39) < error
        assert empty_field.initial_condition[4] == 1.0
        assert abs(empty_field.initial_condition[5] - 2.489108e-39) < error
        assert empty_field.initial_condition[6] == 0.0
        assert abs(empty_field.initial_condition[7] - 2.489108e-39) < error
        assert empty_field.initial_condition[8] == 0.0

        hsk.cprint("[InitialCondition Test] Function test passed.", color="green")

    @staticmethod
    def scalar():
        mesh = hsk.mesh.SquareCase(1)
        mesh.generate_structured([2, 2])

        fields = hsk.field.PhysicalFields()

        empty_field = hsk.field.PhysicalField(mesh)
        empty_field.set_initial_condition_by_scalar(2.5)
        fields.add_field(empty_field)

        fields.generate_info()

        assert np.all(empty_field.initial_condition==2.5)

        hsk.cprint("[InitialCondition Test] Scalar test passed.", color="green")


class PhysicalProperties:
    @staticmethod
    def basic():
        mesh = hsk.mesh.SquareCase(1)
        mesh.generate_structured([2, 2])

        fields = hsk.field.PhysicalFields()

        field = hsk.field.PhysicalField(mesh)
        field.set_physical_properties_num(10)
        field.set_physical_properties([1], [1e-6, 4e-13, 0, 0, 0, 4e-13, 0, 0, 0, 4e-13])
        fields.add_field(field)

        fields.generate_info()

        error = 1e-6
        assert abs(field.cell_info[0, 1] - 1e-6) < error and abs(field.cell_info[0, 2] - 4e-13) < error
        assert abs(field.cell_info[1, 1] - 1e-6) < error and abs(field.cell_info[1, 2] - 4e-13) < error
        assert abs(field.cell_info[2, 1] - 1e-6) < error and abs(field.cell_info[2, 2] - 4e-13) < error
        assert abs(field.cell_info[3, 1] - 1e-6) < error and abs(field.cell_info[3, 2] - 4e-13) < error

        hsk.cprint("[PhysicalProperties Test] Basic test passed.", color="green")


class Source:
    @staticmethod
    def point():
        mesh = hsk.mesh.SquareCase(1)

        # Particular add four point for test in different os and differen gmsh version.
        point_tags = []
        point_tags.append(gmsh.model.occ.add_point(0.7386115, 0.26138848, 0.0, 0.5))
        point_tags.append(gmsh.model.occ.add_point(0.625, 0.625, 0.0, 0.5))
        point_tags.append(gmsh.model.occ.add_point(0.35747692, 0.35085642, 0.0, 0.5))
        point_tags.append(gmsh.model.occ.add_point(0.28125, 0.71875, 0.0, 0.5))
        gmsh.model.occ.fragment([(0, point_tags[0]), (0, point_tags[1]), (0, point_tags[2]), (0, point_tags[3])],
                                [(2, 1)])
        gmsh.model.occ.synchronize()

        gmsh.model.mesh.set_size([(0, 9)], 0.5)
        gmsh.model.mesh.set_size([(0, 10)], 0.5)
        gmsh.model.mesh.set_size([(0, 11)], 0.5)
        gmsh.model.mesh.set_size([(0, 12)], 0.5)
        # Uniqe deal finished.

        mesh.generate_unstructured([0.5, 0.5, 0.5, 0.5], show_mesh=False)

        fields = hsk.field.PhysicalFields()

        field = hsk.field.PhysicalField(mesh)
        field.set_point_source([6], 6)
        field.set_point_source([5], 5)
        fields.add_field(field)

        fields.generate_info()

        assert field.cell_info[0, 0] == 1.0
        assert field.cell_info[1, 0] == 1.0
        assert field.cell_info[2, 0] == 1.0
        assert field.cell_info[3, 0] == 1.0
        assert field.cell_info[4, 0] == 0.0
        assert field.cell_info[5, 0] == 0.0
        assert field.cell_info[6, 0] == 0.0
        assert field.cell_info[7, 0] == 0.0
        assert field.cell_info[8, 0] == 2.0
        assert field.cell_info[9, 0] == 2.0
        assert field.cell_info[10, 0] == 1.0
        assert field.cell_info[11, 0] == 1.0
        assert field.cell_info[12, 0] == 0.0
        assert field.cell_info[13, 0] == 1.0

        hsk.cprint("[Source Test] Point source basic test passed.", color="green")

    @staticmethod
    def set_by_coordinate():
        mesh = hsk.mesh.SquareCase(2, coordinate=[-1, -1])
        mesh.generate_structured([3, 3], show_mesh=False)


        fields = hsk.field.PhysicalFields()
        field = hsk.field.PhysicalField(mesh)
        field.set_point_source_by_coordinate(np.array([0.0, 0.0, 0.0], dtype=np.float32), 1)
        fields.add_field(field)
        fields.generate_info()

        assert field.cell_info[0, 0] == 0.0
        assert field.cell_info[1, 0] == 0.0
        assert field.cell_info[2, 0] == 0.0
        assert field.cell_info[3, 0] == 0.0
        assert field.cell_info[4, 0] == 1.0
        assert field.cell_info[5, 0] == 0.0
        assert field.cell_info[6, 0] == 0.0
        assert field.cell_info[7, 0] == 0.0
        assert field.cell_info[8, 0] == 0.0

        hsk.cprint("[Source Test] Point source by coordinate test passed.", color="green")


class MultiField:
    @staticmethod
    def basic():
        mesh = hsk.mesh.SquareCase(1)
        mesh.generate_structured([2, 2])

        fields = hsk.field.PhysicalFields()

        field_1 = hsk.field.PhysicalField(mesh)
        field_1.set_physical_properties_num(1)
        field_1.set_physical_properties([mesh.square_area], [1])
        field_1.set_boundary_as_dirichlet([1, 2, 3, 4], 1)
        field_1.set_point_source_by_coordinate(np.array([0.25, 0.25, 0.0]), 1)
        fields.add_field(field_1)

        field_2 = hsk.field.PhysicalField(mesh)
        field_2.set_physical_properties_num(1)
        field_2.set_physical_properties([mesh.square_area], [2])
        field_2.set_boundary_as_periodic([mesh.boundary_left, mesh.boundary_right])
        field_2.set_boundary_as_periodic([mesh.boundary_up, mesh.boundary_down])
        field_2.set_point_source_by_coordinate(np.array([0.75, 0.75, 0.0]), 2)
        fields.add_field(field_2)

        fields.generate_info()

        assert field_1.face_info[0, 0] == 1 and field_1.face_info[0, 1] == 1
        assert field_1.face_info[1, 0] == 1 and field_1.face_info[1, 1] == 1
        assert field_1.face_info[2, 0] == 1 and field_1.face_info[2, 1] == 1
        assert field_1.face_info[3, 0] == 1 and field_1.face_info[3, 1] == 1
        assert field_1.face_info[4, 0] == 1 and field_1.face_info[4, 1] == 1
        assert field_1.face_info[5, 0] == 1 and field_1.face_info[5, 1] == 1
        assert field_1.face_info[6, 0] == 1 and field_1.face_info[6, 1] == 1
        assert field_1.face_info[7, 0] == 1 and field_1.face_info[7, 1] == 1
        assert field_1.face_info[8, 0] == 0 and field_1.face_info[8, 1] == 0
        assert field_1.face_info[9, 0] == 0 and field_1.face_info[9, 1] == 0
        assert field_1.face_info[10, 0] == 0 and field_1.face_info[10, 1] == 0
        assert field_1.face_info[11, 0] == 0 and field_1.face_info[11, 1] == 0

        assert field_2.face_info[0, 0] == 4 and field_2.face_info[0, 1] == 5 and field_2.face_info[0, 2] == 1
        assert field_2.face_info[1, 0] == 4 and field_2.face_info[1, 1] == 4 and field_2.face_info[1, 2] == 3
        assert field_2.face_info[2, 0] == 4 and field_2.face_info[2, 1] == 7 and field_2.face_info[2, 2] == 0
        assert field_2.face_info[3, 0] == 4 and field_2.face_info[3, 1] == 6 and field_2.face_info[3, 2] == 1
        assert field_2.face_info[4, 0] == 4 and field_2.face_info[4, 1] == 1 and field_2.face_info[4, 2] == 2
        assert field_2.face_info[5, 0] == 4 and field_2.face_info[5, 1] == 0 and field_2.face_info[5, 2] == 0
        assert field_2.face_info[6, 0] == 4 and field_2.face_info[6, 1] == 3 and field_2.face_info[6, 2] == 3
        assert field_2.face_info[7, 0] == 4 and field_2.face_info[7, 1] == 2 and field_2.face_info[7, 2] == 2
        assert field_2.face_info[8, 0] == 0 and field_2.face_info[8, 1] == 0 and field_2.face_info[8, 2] == 0
        assert field_2.face_info[9, 0] == 0 and field_2.face_info[9, 1] == 0 and field_2.face_info[9, 2] == 0
        assert field_2.face_info[10, 0] == 0 and field_2.face_info[10, 1] == 0 and field_2.face_info[10, 2] == 0
        assert field_2.face_info[11, 0] == 0 and field_2.face_info[11, 1] == 0 and field_2.face_info[11, 2] == 0

        assert field_1.cell_info[0, 0] == 1.0 and field_1.cell_info[0, 1] == 1.0
        assert field_1.cell_info[1, 0] == 0.0 and field_1.cell_info[1, 1] == 1.0
        assert field_1.cell_info[2, 0] == 0.0 and field_1.cell_info[2, 1] == 1.0
        assert field_1.cell_info[3, 0] == 0.0 and field_1.cell_info[3, 1] == 1.0

        assert field_2.cell_info[0, 0] == 0.0 and field_2.cell_info[0, 1] == 2.0
        assert field_2.cell_info[1, 0] == 0.0 and field_2.cell_info[1, 1] == 2.0
        assert field_2.cell_info[2, 0] == 0.0 and field_2.cell_info[2, 1] == 2.0
        assert field_2.cell_info[3, 0] == 2.0 and field_2.cell_info[3, 1] == 2.0

        hsk.cprint("[MultiField Test] Basic test passed.", color="green")


if __name__ == "__main__":
    BoundaryCondition.Dirichlet.scalar()
    BoundaryCondition.Dirichlet.function_cos()
    BoundaryCondition.Open.basic()
    BoundaryCondition.Periodic.basic()

    InitialCondition.function()
    InitialCondition.scalar()

    PhysicalProperties.basic()

    Source.point()
    Source.set_by_coordinate()

    MultiField.basic()
