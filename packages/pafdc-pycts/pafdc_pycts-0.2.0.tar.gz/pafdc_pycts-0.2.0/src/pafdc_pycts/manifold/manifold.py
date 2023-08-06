import numpy as np
from .cell import Cell


class Manifold:
    """

    """

    def __init__(self, gain, touch):
        """

        """

        # Check that gain is of type list or type numpy.ndarray
        if not isinstance(gain, (list, np.ndarray)):
            raise TypeError(f"Gain ({type(gain)}) must be of type list or type numpy.ndarray")

        # Check that touch is of type list or type numpy.ndarray
        if not isinstance(touch, (list, np.ndarray)):
            raise TypeError(f"Touch ({type(touch)}) must be of type list or type numpy.ndarray")

        # Convert a gain list to a numpy.ndarray
        if isinstance(gain, list):
            gain = np.array(gain)

        # Convert a touch list to a numpy.ndarray
        if isinstance(touch, list):
            touch = np.array(touch)

        # Assert that gain and touch have an equal number of dimensions except for the last dimension
        assert gain.shape[:-1] == touch.shape[
                                  :-1], f"Gain and touch must have the same dimensions up to last: {gain.shape[:-1]}," \
                                        f" {touch.shape[:-1]} "

        # Check that touch is of type numpy.ndarray
        assert gain.shape[-1] >= len(gain.shape[:-1]), f"Last gain dimension must have equal or more elements than " \
                                                       f"previous dimensions: "

        # Check that touch is of type numpy.ndarray
        assert touch.shape[-1] >= len(touch.shape[:-1]), f"Touch must have "

        self.__gain = gain  # Set the gain
        self.__touch = touch  # Set the touch

        self.__create_manifold_cells()  # Create the cell matrix

        self.__checked = np.zeros(self.cells.shape, dtype=bool)  # Create a NumPy array of booleans to keep track of
        # cells that have been evaluated

    @property
    def gain(self):
        return self.__gain

    @property
    def touch(self):
        return self.__touch

    @property
    def cells(self):
        return self.__cells

    def __create_manifold_cells(self):
        """
        Creates a matrix of cell objects.


        """
        cells_shape = tuple(i - 1 for i in self.gain.shape[:-1])  # Construct a tuple based on the shape of the data
        self.__cells = np.empty(cells_shape, dtype=object)  # Create an empty numpy array of objects

        for cell_idx in range(self.cells.size):
            cell_idx_tuple = np.unravel_index(cell_idx, self.cells.shape)  #
            gain_idx_str = ", ".join([f"{i}:{i + 2}" for i in np.unravel_index(cell_idx, self.__cells.shape)])  #
            self.__cells[cell_idx_tuple] = eval(f"Cell(self.gain[{gain_idx_str}], self.touch[{gain_idx_str}])")  #

    def offset_cell(self, cell_idx_tuple, offset_tuple):
        out = []
        for s, i, t in zip(self.cells.shape, cell_idx_tuple, offset_tuple):
            tmp_s = i + t
            out.append(s - 1 if (tmp_s >= s) else 0 if (tmp_s < 0) else tmp_s)

        return tuple(out)

    def map_vec(self, vec, P, Q):

        # Check that vec is array-like
        if not isinstance(vec, (list, np.ndarray)):
            raise TypeError(f"Vector ({type(vec)}) must be of type list or type numpy.ndarray")

        # Convert a gain list to a numpy.ndarray
        if isinstance(vec, list):
            vec = np.array(vec)

        # Reshape vec if it is 1-dimensional
        if len(vec.shape) == 1:
            vec = vec[np.newaxis, :]

        #
        assert len(vec.shape) == 2, f"Vec must be 2-dimensional: {vec.shape}."

        # Check that vec dimension 1 is the same length as the last gain dimension
        assert vec.shape[-1] == getattr(self, P).shape[
            -1], f"Vec must have the same last dimension length as {P}: {vec.shape[-1]} : {getattr(self, P).shape[-1]}."

        self.__checked = self.__checked * False  # Clear the checked array

        #
        res = []

        #
        for pos, v in enumerate(vec):
            self.__checked = self.__checked * False  # Clear the checked array

            dist = np.zeros((self.cells.size, getattr(self, P).shape[
                -1]))  # Create a NumPy array to store the distance between the particle and the centroid of each cell

            for cell_idx in range(self.cells.size):
                cell_idx_tuple = np.unravel_index(cell_idx, self.cells.shape)  # Get the
                dist[cell_idx, :] = getattr(self.cells[cell_idx_tuple], f"{P}_centroid")  #

            min_cell_dist_idx = np.argmin(
                np.sqrt(((dist - v) ** 2).sum(axis=-1)))  # Get the index of the minimum distance
            min_cell_dist_idx_tuple = np.unravel_index(min_cell_dist_idx, self.cells.shape)  #

            nmo = Cell.newtons_method(
                self.cells[min_cell_dist_idx_tuple],
                getattr(self.cells[min_cell_dist_idx_tuple], f"{P}"),
                v
            )

            res.append(
                Cell.regress(
                    getattr(nmo.cell, f"{Q}"),
                    nmo.constrained_history[-1, :]
                )
            )

            """
            while True: # Returns eventually
                nmo = Cell.newtons_method(
                    self.cells[min_cell_dist_idx_tuple],
                    getattr(self.cells[min_cell_dist_idx_tuple], f"{P}"),
                    v
                )

                self.__checked[min_cell_dist_idx_tuple] = True
                min_cell_dist_idx_tuple = self.offset_cell(min_cell_dist_idx_tuple, nmo.offset)

                if self.__checked[min_cell_dist_idx_tuple] or any(nmo.offset):
                    res.append(
                        Cell.regress(
                            getattr(nmo.cell, f"{Q}"),
                            nmo.constrained_history[-1, :]
                        )
                    )
                    print(f"vector: {pos}")
                    print(res[-1])
                    break
            """

        return res

        # Assert that the

        # 1. For each point:
        # 2. Return the closest cell to the input vector via the cells' centroid
        # 3. Return the local mapping, constrained local mapping, and offset vector of the closest cell
        # 4. Mark the cell as having been evaluated
        # 4. If the offset vector is all zero, return the transformed constrained local mapping
        # 5. If the offset vector is not all zero, apply the offset
        # 6. If the offset is beyond the manifold boundary,

        # self.cells[cell_idx_tuple].

        # if self.cells[].is_evaluated
