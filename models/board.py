

class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = {y: {x: " " for x in range(x)} for y in range(y)}
        self.active_shape = None
        self._initial_layout()

    def _initial_layout(self):
        for x in range(self.x):
            self.grid[0][x] = '*'
        for line in range(1, self.y):
            self.grid[line][0] = "*"
            self.grid[line][self.x - 1] = "*"

    def flush(self):
        for y in reversed(range(self.y)):
            line_layout = ""
            for x in range(self.x):
                if self.grid[y][x] != "*":
                    if [x, y] in self.active_shape.list_of_points():
                        line_layout = "".join([line_layout, "*"])
                    else:
                        line_layout = "".join([line_layout, " "])
                else:
                    line_layout = "".join([line_layout, "*"])
            print(line_layout)

    def assimilate(self):
        for point in self.active_shape:
            self.grid[point.y][point.x] = "*"
