class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return True if self.x == other.x and self.y == other.y else False
        return NotImplemented
