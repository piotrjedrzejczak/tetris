from models.board import Board
from models.shapes import OShape
from models.shapes import Point
from xceptions import WrongMove


def main():

    b = Board(20, 20)
    o = OShape(Point(4, 15), Point(5, 15), Point(4, 14), Point(5, 14))
    b.active_shape = o

    while True:
        try:
            if b.active_shape.has_next_move(b.grid):
                move = input()
                if move == "a":
                    b.active_shape.move(b.grid, "left")
                elif move == "d":
                    b.active_shape.move(b.grid, "right")
                # elif move == 'w':
                #     b.active_shape.move_right(b.grid)
                # elif move == 's':
                #     b.active_shape.move_right(b.grid)
                else:
                    raise WrongMove
                b.active_shape.move(b.grid, "down")
            else:
                b.assimilate()
                new_shape = OShape(Point(4, 15), Point(5, 15), Point(4, 14), Point(5, 14))
                b.active_shape = new_shape
                if not b.active_shape.has_next_move(b.grid):
                    raise ValueError("Game Over")
            b.flush()
        except WrongMove:
            print("Wrong Move, Try Again!")


main()
