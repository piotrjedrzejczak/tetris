from models.board import Board
from models.shapes import OShape, IShape, WrongMove, Point


def main():

    b = Board(20, 20)
    o = OShape(Point(4, 15), Point(5, 15), Point(5, 14), Point(4, 14))
    b.active_shape = o
    # i = IShape(Point(4, 14), Point(4, 13), Point(4, 12), Point(4, 11))
    # b.active_shape = i

    while True:
        try:
            if b.active_shape.has_next_move(b.grid):
                move = input()
                if move == "a":
                    b.active_shape.move(b.grid, "left")
                elif move == "d":
                    b.active_shape.move(b.grid, "right")
                elif move == 'w':
                    b.active_shape.rotate(b.grid)
                # elif move == 's':
                #     b.active_shape.move_right(b.grid)
                else:
                    raise WrongMove
                b.active_shape.move(b.grid, "down")
            else:
                b.assimilate()
                new_shape = OShape(Point(4, 15), Point(5, 15), Point(5, 14), Point(4, 14))
                # new_shape = IShape(Point(4, 14), Point(4, 13), Point(4, 12), Point(4, 11))
                b.active_shape = new_shape
                if not b.active_shape.has_next_move(b.grid):
                    raise ValueError("Game Over")
            b.flush()
        except WrongMove:
            print("Wrong Move, Try Again!")


main()
