from xceptions import WrongMove


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BaseShape:

    def __init__(self):
        self.coordinates = {}

    def __iter__(self):
        for item in self.coordinates.values():
            yield item

    def __repr__(self):
        return str(self.coordinates)

    def list_of_points(self):
        return [[point.x, point.y] for point in self.coordinates.values()]

    def has_next_move(self, grid):
        for point in self.coordinates.values():
            if grid[point.x][point.y - 1] == "*":
                return False
        return True

    def move(self, grid, direction):
        new_coordinates = {}
        for name, point in self.coordinates.items():
            if direction == 'down':
                if grid[point.x][point.y - 1] == "*":
                    raise WrongMove
                new_coordinates[name] = Point(point.x, point.y - 1)
            if direction == 'left':
                if grid[point.x - 1][point.y] == "*":
                    raise WrongMove
                new_coordinates[name] = Point(point.x - 1, point.y)
            if direction == 'right':
                if grid[point.x + 1][point.y] == "*":
                    raise WrongMove
                new_coordinates[name] = Point(point.x + 1, point.y)
        self.coordinates = new_coordinates


class OShape(BaseShape):

    def __init__(self, p1, p2, p3, p4):
        self.coordinates = {
            "p1": p1,
            "p2": p2,
            "p3": p3,
            "p4": p4,
        }

    def rotate(self):
        pass


class ZShape:
    pass


class IShape:
    pass


class JShape:
    pass


class LShape:
    pass
