import numpy as np


class NewtonsMethodObject:
    def __init__(self, cell, history, vertices, goal, guess_vec, tol, max_iter):
        self.__cell = cell
        self.__history = history
        self.__vertices = vertices
        self.__goal = goal
        self.__guess_vec = guess_vec
        self.__tol = tol
        self.__max_iter = max_iter

        self.__constrained_history = np.copy(self.__history)
        self.__constrained_history[self.__constrained_history > 1.0] = 1.0
        self.__constrained_history[self.__constrained_history < 0.0] = 0.0

    @property
    def cell(self):
        return self.__cell

    @property
    def history(self):
        return self.__history

    @property
    def constrained_history(self):
        return self.__constrained_history

    @property
    def offset(self):
        result = self.__history[-1, :]
        return [1 if (i > 1.0) else -1 if (i < 0.0) else 0 for i in result]

    @property
    def vertices(self):
        return self.__vertices

    @property
    def goal(self):
        return self.__goal

    @property
    def guess_vec(self):
        return self.__guess_vec

    @property
    def tol(self):
        return self.__tol

    @property
    def max_iter(self):
        return self.__max_iter
