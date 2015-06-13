import unittest
from conway import *

class TestConway(unittest.TestCase):

  # adding one cell to an empty universe results in a universe with one cell
  def test_one_cell(self):
      universe = Universe(3, 3)
      universe.addCell(1, 1)
      self.assertEqual(1, universe.getNumberOfCells())

  def test_two_neighbour_cells(self):
      universe = Universe(3, 3)
      universe.addCell(1, 1)
      universe.addCell(2, 1)

      self.assertEqual(2, universe.getNumberOfCells())

  def test_one_cell_next_generation_zero(self):
      universe = Universe(6, 6)
      universe.addCell(1, 1)
      universe.evolve()

      self.assertEqual(0, universe.getNumberOfCells())

  def test_two_cell_next_generation_zero(self):
      universe = Universe(6, 6)
      universe.addCell(1, 1)
      universe.addCell(2, 1)

      universe.evolve()

      self.assertEqual(0, universe.getNumberOfCells())

  def test_one_cell_two_neigh_next_generation_lives(self):
      universe = Universe(6, 6)
      universe.addCell(1, 1)
      universe.addCell(2, 1)
      universe.addCell(3, 1)

      universe.evolve()

      self.assertEqual(3, universe.getNumberOfCells())

  def test_one_cell_two_not_neigh_next_generation_zero(self):
      universe = Universe(6, 6)
      universe.addCell(1, 1)
      universe.addCell(5, 1)
      universe.addCell(2, 2)

      universe.evolve()

      self.assertEqual(0, universe.getNumberOfCells())

  def test_one_cell_three_neigh_next_generation_lives(self):
      universe = Universe(6, 6)
      universe.addCell(2, 2)
      universe.addCell(2, 3)
      universe.addCell(3, 2)
      universe.addCell(3, 3)

      universe.evolve()

      self.assertEqual(4, universe.getNumberOfCells())

  def test_one_cell_three_not_neigh_next_generation_dies(self):
      universe = Universe(6, 6)
      universe.addCell(2, 2)
      universe.addCell(2, 3)
      universe.addCell(4, 2)
      universe.addCell(4, 5)

      universe.evolve()

      self.assertEqual(2, universe.getNumberOfCells())

  def test_one_cell_three_neigh_next_generation_reproduction(self):
      universe = Universe(6, 6)
      universe.addCell(2, 2)
      universe.addCell(2, 4)
      universe.addCell(4, 2)

      universe.evolve()

      self.assertEqual(1, universe.getNumberOfCells())

if __name__ == '__main__':
    unittest.main()
