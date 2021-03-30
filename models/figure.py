from models.board import WrongMove
from models.point import Point


class Figure:
    def __init__(self, origin_point=None, **kwargs):
        self.coordinates = kwargs
        self.origin_point = origin_point

    def __iter__(self):
        for item in self.coordinates.values():
            yield item

    @property
    def origin(self):
        if self.origin_point:
            return self.coordinates[self.origin_point]
        return None

    def has_next_move(self, board):
        for point in self.coordinates.values():
            try:
                board.cell_is_free(point.x, point.y - 1)
            except WrongMove:
                return False
        return True

    def move(self, board, direction, _rotation_direction="cw"):
        new_coordinates = {}
        for name, point in self.coordinates.items():
            if direction == "down":
                new_coordinates[name] = board.cell_is_free(point.x, point.y - 1)
            if direction == "left":
                new_coordinates[name] = board.cell_is_free(point.x - 1, point.y)
            if direction == "right":
                new_coordinates[name] = board.cell_is_free(point.x + 1, point.y)
            if direction == "rotate":
                if self.origin is None or point == self.origin:
                    new_coordinates[name] = point
                else:
                    x, y = point.x - self.origin.x, point.y - self.origin.y
                    if _rotation_direction == "cw":
                        x, y = y, -x
                    else:  # Counter Clockwise
                        x, y = -y, x
                    new_coordinates[name] = board.cell_is_free(
                        x + self.origin.x, y + self.origin.y
                    )
        self.coordinates = new_coordinates

    @classmethod
    def from_point(cls, x, y, shape="o"):
        if shape == "o":
            return cls(
                p1=Point(x, y),
                p2=Point(x + 1, y),
                p3=Point(x, y - 1),
                p4=Point(x + 1, y - 1),
            )
        elif shape == "i":
            return cls(
                origin_point="p2",
                p1=Point(x, y),
                p2=Point(x + 1, y),
                p3=Point(x + 2, y),
                p4=Point(x + 3, y),
            )
        elif shape == "z":
            return cls(
                origin_point="p2",
                p1=Point(x, y),
                p2=Point(x + 1, y),
                p3=Point(x + 1, y - 1),
                p4=Point(x + 2, y - 1),
            )
        elif shape == "l":
            return cls(
                origin_point="p2",
                p1=Point(x, y),
                p2=Point(x, y - 1),
                p3=Point(x, y - 2),
                p4=Point(x + 1, y - 2),
            )
        elif shape == "j":
            return cls(
                origin_point="p2",
                p1=Point(x, y),
                p2=Point(x, y - 1),
                p3=Point(x, y - 2),
                p4=Point(x - 1, y - 2),
            )
