#! python3
import random


class Grid:
    def __init__(self, w, h, grid=None):
        self.width, self.height = w, h
        self.loop_paths = dict()
        self._points = [(ir, ic) for ir in range(self.height) for ic in range(self.width)]
        self._cell_movements = {
            '^': lambda x: self._move_point(x, [-1, 0]),
            'v': lambda x: self._move_point(x, [1, 0]),
            '<': lambda x: self._move_point(x, [0, -1]),
            '>': lambda x: self._move_point(x, [0, 1])
        }

        try:
            self.grid = [[c for c in r] for r in grid.splitlines()]
        except TypeError:
            self.grid = self._generate_grid()

        if (len(self.grid) != self.height) + sum([len(r) != self.width for r in self.grid]) > 0:
            print('Grid does not match given dimensions.')
            self.grid = None

        self.get_loops()

    def _generate_grid(self):
        return [[random.choice([ch for ch in '<>^v']) for c in range(self.width)] for r in range(self.height)]

    def _move_point(self, point, point_mod):
        return (point[0] + point_mod[0]) % self.height, (point[1] + point_mod[1]) % self.width

    def get_loops(self):
        while self._points:
            path = list()
            cell = self._points.pop(0)

            while True:
                path.append(cell)
                cell = self._cell_movements[self.grid[cell[0]][cell[1]]](cell)

                try:
                    self._points.remove(cell)
                except ValueError:
                    if cell in path:
                        path = path[path.index(cell):]
                        self.loop_paths.setdefault(len(path), list())
                        self.loop_paths[len(path)].append(path)
                    break

    def max_loop(self):
        loop = random.choice(self.loop_paths[max(self.loop_paths.keys())])
        g ='\n'.join([''.join([self.grid[ir][ic] if (ir, ic) in loop else '_' for ic in range(self.width)])
                      for ir in range(self.height)])
        return g


if __name__ == '__main__':
    test, ans = ((5, 5, ">>>>v\n^v<<v\n^vv^v\n^>>v<\n^<<<^"), 16)
    g = Grid(*test[:2])
    print(max(g.loop_paths) == ans)
    # while True:
    #     g = Grid(10, 10)
    #     if max(g.loop_paths.keys()) > 25:
    #         print(max(g.loop_paths.keys()))
    #         print(g.max_loop())
    #         print()
    #         break
