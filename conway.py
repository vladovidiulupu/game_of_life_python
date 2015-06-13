# To make sure you have numpy and scipy that work properly install the
# Anaconda Python distribution from http://continuum.io/downloads

import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

class Universe():

    cv_filter = np.array([[1, 1, 1],
                          [1, 100, 1],
                          [1, 1, 1]])
    live_cell_with_2_neighbours = 102
    live_cell_with_3_neighbours = 103
    dead_cell_with_3_neighrbours = 3

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros([rows, cols])

    def addCell(self, x, y):
        self.board[x, y] = 1.0

    def getNumberOfCells(self):
        return int(self.board.sum())

    def get_next_state(self):
        new_board = np.zeros([self.rows, self.cols])
        new_board[self.board == Universe.live_cell_with_2_neighbours] = 1
        new_board[self.board == Universe.live_cell_with_3_neighbours] = 1
        new_board[self.board == Universe.dead_cell_with_3_neighrbours] = 1
        return new_board

    def solve_boundaries(self):
        self.board = self.board[range(1, self.rows + 1), :]
        self.board = self.board[:, range(1, self.cols + 1)]

    def evolve(self):
        self.board = convolve2d(self.board, Universe.cv_filter)
        self.solve_boundaries()
        self.board = self.get_next_state()

    def visualize(self):
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(self.board, cmap=plt.cm.gray_r)

        # put the major ticks at the middle of each cell
        ax.set_xticks(np.arange(self.board.shape[0]), minor=False)
        ax.set_yticks(np.arange(self.board.shape[1]), minor=False)

        plt.grid(b=True, which='both', color='0.65',linestyle='-')

        # want a more natural, table-like display
        ax.invert_yaxis()
        ax.xaxis.tick_top()

        ax.set_xticklabels(range(0, self.cols + 1), minor=False)
        ax.set_yticklabels(range(0, self.rows + 1), minor=False)
        plt.show()
