from models.exceptions import WrongMove
from models.point import Point


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_figure = None
        self.grid = {y: {x: " " for x in range(x)} for y in range(y)}
        self._initialize()

    def _initialize(self):
        for x in range(self.x):
            self.grid[0][x] = "*"
        for line in range(1, self.y):
            self.grid[line][0] = "*"
            self.grid[line][self.x - 1] = "*"

    def flush(self):
        current_figure_coordinates = [(p.x, p.y) for p in self.current_figure]
        for y in reversed(range(self.y)):
            line_layout = ""
            for x in range(self.x):
                if self.grid[y][x] != "*":
                    if (x, y) in current_figure_coordinates:
                        line_layout = "".join([line_layout, "*"])
                    else:
                        line_layout = "".join([line_layout, " "])
                else:
                    line_layout = "".join([line_layout, "*"])
            print(line_layout)

    def cell_is_free(self, x, y):
        try:
            if self.grid[y][x] == "*":
                raise WrongMove("This cell is a part of the board grid.")
            return Point(x, y)
        except KeyError:
            raise WrongMove("This cell is outside of the board grid.")

    def devour(self):
        for point in self.current_figure:
            self.grid[point.y][point.x] = "*"
