from collections import deque


class WrongMove(Exception):
    pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def move_point(cls, grid, x, y):
        if grid[y][x] == "*":
            raise WrongMove
        return cls(x, y)


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
            if grid[point.y - 1][point.x] == "*":
                return False
        return True

    def move(self, grid, direction):
        new_coordinates = {}
        for name, point in self.coordinates.items():
            if direction == 'down':
                new_coordinates[name] = point.move_point(grid, point.x, point.y - 1)
            if direction == 'left':
                new_coordinates[name] = point.move_point(grid, point.x - 1, point.y)
            if direction == 'right':
                new_coordinates[name] = point.move_point(grid, point.x + 1, point.y)
        self.coordinates = new_coordinates

    def rotate(self):
        raise NotImplementedError


class OShape(BaseShape):

    def __init__(self, p1, p2, p3, p4):
        self.coordinates = {
            "p1": p1,
            "p2": p2,
            "p3": p3,
            "p4": p4,
        }

    def rotate(self, direction):
        """Set direction to 1 to rotate clockwise, -1 to rotate counter clockwise."""
        dq = deque(self.coordinates.values())
        dq.rotate(direction)
        self.coordinates = dict(zip(self.coordinates.keys(), dq))


class IShape(BaseShape):

    def __init__(self, p1, p2, p3, p4):
        self.coordinates = {
            "p1": p1,
            "p2": p2,
            "p3": p3,
            "p4": p4,
        }

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, dictionary):
        self._coordinates = dictionary
        self.is_vertical = True if len(set([p.x for p in dictionary.values()])) == 1 else False

    def rotate(self, grid):
        new_coordinates = {}
        for name, point in self.coordinates.items():
            if name == 'p1':
                if self.is_vertical:
                    new_coordinates['p1'] = point.move_point(grid, point.x - 1, point.y)
                else:
                    new_coordinates['p1'] = point.move_point(grid, point.x + 1, point.y)
            if name == 'p2':
                if self.is_vertical:
                    new_coordinates['p2'] = point.move_point(grid, point.x, point.y + 1)
                else:
                    new_coordinates['p2'] = point.move_point(grid, point.x, point.y - 1)
            if name == 'p3':
                if self.is_vertical:
                    new_coordinates['p3'] = point.move_point(grid, point.x + 1, point.y + 2)
                else:
                    new_coordinates['p3'] = point.move_point(grid, point.x - 1, point.y - 2)
            if name == 'p4':
                if self.is_vertical:
                    new_coordinates['p4'] = point.move_point(grid, point.x + 2, point.y + 3)
                else:
                    new_coordinates['p4'] = point.move_point(grid, point.x - 2, point.y - 3)
        self.coordinates = new_coordinates


class ZShape:
    pass


class JShape:
    pass


class LShape:
    pass
