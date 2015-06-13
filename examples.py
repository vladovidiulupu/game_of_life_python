import conway

def pentomino_cell_count():
    universe = conway.Universe(1000, 1000)
    universe.addCell(503, 501)
    universe.addCell(503, 502)
    universe.addCell(502, 502)
    universe.addCell(501, 502)
    universe.addCell(502, 503)

    counter = 0
    #universe.visualize()
    while (universe.getNumberOfCells() != 0):
        universe.evolve()
        counter += 1
        print "generation: ", counter, "; Alive cells: ", universe.getNumberOfCells()

    wait = raw_input()

def visualize_glider():
    universe = conway.Universe(30, 30)
    universe.addCell(0, 1)
    universe.addCell(1, 2)
    universe.addCell(2, 0)
    universe.addCell(2, 1)
    universe.addCell(2, 2)
    universe.visualize()

    while (universe.getNumberOfCells() != 0):
        universe.evolve()
        universe.visualize()

if __name__ == '__main__':
    visualize_glider()
