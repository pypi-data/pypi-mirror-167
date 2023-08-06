import numpy as np
from .manifoldutils import NewtonsMethodObject


class Cell:
    """

    """

    def __init__(self, gain, touch):
        """
        Cell object constructor.

        :param gain:
        :type gain: numpy.ndarray
        :param touch:
        :type touch: numpy.ndarray
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
        assert gain.shape[:-1] == touch.shape[:-1], f"Gain and touch must have the same dimensions up to last: " \
                                                    f"{gain.shape[:-1]}, {touch.shape[:-1]}"

        # Check that touch is of type numpy.ndarray
        assert gain.shape[-1] >= len(gain.shape[:-1]), f"Last gain dimension must have equal or more elements than " \
                                                       f"previous dimensions: "

        # Check that touch is of type numpy.ndarray
        assert touch.shape[-1] >= len(touch.shape[:-1]), f"Touch must have "

        #
        assert all([i == 2 for i in gain.shape[:-1]]), f"Unsupported cell shape: {gain.shape[:-1]}."  # Assert that
        # the first gain dimensions are equal to 2
        assert all([i == 2 for i in touch.shape[
                                    :-1]]), f"Unsupported cell shape: {touch.shape[:-1]}."  # Assert that the first
        # touch dimensions are equal to 2

        self.__gain = gain
        self.__touch = touch

    @property
    def gain(self):
        """

        """
        return self.__gain

    @property
    def touch(self):
        """

        """
        return self.__touch

    @property
    def gain_centroid(self):
        """
        Return the gain centroid computed at the midpoint of each cell axis.

        """

        return self.regress(self.gain, 0.5 * np.ones((len(self.gain.shape[:-1])), ))

    @property
    def touch_centroid(self):
        """
        Return the touch centroid computed at the midpoint of each cell axis.

        """

        return self.regress(self.touch, 0.5 * np.ones((len(self.touch.shape[:-1])), ))

    @classmethod
    def regress(cls, vertices, coords):
        """
        Regress a coordinate vector based on the given vertices.

        :param vec:
        :type vec: numpy.ndarray
        """

        # Convert singular inputs to lists
        if isinstance(coords, (int, float)):
            coords = [coords]

        # Convert regular lists to numpy arrays
        if isinstance(coords, list):
            coords = np.array(coords)

        # If the numpy array is a single dimension,
        if len(coords.shape) == 1:
            coords = coords[np.newaxis, :]

        result = np.zeros((coords.shape[0], vertices.shape[-1]))

        assert coords.shape[-1] == len(vertices.shape[
                                       :-1]), f"Coordinate vector length must match gain shape : {coords.shape[-1]}" \
                                              f" : {len(vertices.shape[:-1])}."

        for i, coord in enumerate(coords):
            tmp_vertices = vertices
            for j in reversed(range(len(coord))):  # Compute the regression for each axis
                tmp_vertices = eval(
                    f"coord[{j}]*(tmp_vertices[{':, ' * j}1, :] - tmp_vertices[{':, ' * j}0, :]) + "
                    f"tmp_vertices[{':, ' * j}0, :]")

            result[i, :] = tmp_vertices

        return result.ravel() if result.shape[0] == 1 else result

    @classmethod
    def jacobian(cls, vertices, coords):
        """
        Compute the linear Jacobian at the given vector coordinate location using the given vertices.

        """

        # This function typically shouldn't be used for multidimensional vector inputs

        # Convert singular values to lists
        if isinstance(coords, (int, float)):
            coords = [coords]

        # Assert that vec is array-like
        if not isinstance(coords, (list, np.ndarray)):
            raise TypeError(f"Vector ({type(coords)}) must be of type list or type numpy.ndarray")

        # Make sure that a NumPy array is single-dimensional
        # if isinstance(vec, np.ndarray):
        #    pass

        # Reshape vec if it is 1-dimensional
        # if len(vec.shape) == 1:
        #    vec = vec[np.newaxis, :]

        # Assert that the number of vertices dimensions to n-1 are equal to the vector length
        # assert len(vertices.shape[:-1]) == vec.shape[-1], f"Vector length must match vertices shape."

        J = np.zeros((vertices.shape[-1], 0))  # Construct the jacobian matrix
        dims = np.arange(0, len(coords), dtype=int)

        for i in range(len(coords)):
            tmp_coords = np.roll(coords, -i)  # Roll the input vector
            tmp_dims = np.roll(dims, -i)  # Roll the dimension vector
            tmp_vertices = vertices.transpose(tuple(tmp_dims) + (len(coords),))

            for i in reversed(range(1, len(coords))):
                tmp_vertices = eval(
                    f"tmp_coords[{i}]*(tmp_vertices[{':, ' * i}1, :] - tmp_vertices[{':, ' * i}0, :]) + "
                    f"tmp_vertices[{':, ' * i}0, :]")

            J = np.concatenate(
                (
                    J,
                    (tmp_vertices[1, :] - tmp_vertices[0, :])[:, np.newaxis]
                ),
                axis=1
            )

        return J

    @classmethod
    def newtons_method(cls, cell, vertices, goal, guess_vec=None, tol=1e-6, max_iter=20):
        """
        Newton's Method

        """

        # assert that the goal length must match the last vertices dimension
        assert len(goal) == vertices.shape[-1], "Goal length must match last vertices dimension."

        if guess_vec is None:
            guess_vec = 0.5 * np.ones((len(vertices.shape[:-1]),))

        I = np.identity(len(guess_vec))  # Construct an identity matrix of the length of the guess vector
        guess_vec_history = np.zeros((max_iter + 1, len(guess_vec)))
        guess_vec_history[0, :] = guess_vec

        for i in range(max_iter):
            J = cls.jacobian(vertices, guess_vec_history[i, :])
            Jinv = np.linalg.solve(J.T @ J, I)  # J.T @ J to account for non-square Jacobian matrices
            inc = (Jinv @ (J.T @ (cls.regress(vertices, guess_vec_history[i, :]) - goal)[:,
                                 np.newaxis])).ravel()  # Solve the incremental change in the guess vector

            # print(inc)
            # print(guess_vec_history[i, :])

            guess_vec_history[i + 1, :] = guess_vec_history[i, :] - inc
            # if np.all(inc < tol):
            #    break

        return NewtonsMethodObject(cell, guess_vec_history[:i + 1, :], vertices, goal, guess_vec, tol, max_iter)
        # return guess_vec_states[i+1, :], guess_vec_history[:i+1, :]
