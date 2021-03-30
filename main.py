from models.board import Board
from models.exceptions import WrongMove
from models.figure import Figure
from random import choice, randint


def main():

    xlen = 20
    ylen = 20
    board = Board(xlen, ylen)
    x, y = randint(1, xlen - 5), 19
    board.current_figure = Figure.from_point(x, y, shape=choice("oizlj"))
    board.flush()

    while True:
        try:
            if board.current_figure.has_next_move(board):
                move = input()
                if move == "a":
                    board.current_figure.move(board, "left")
                elif move == "d":
                    board.current_figure.move(board, "right")
                elif move == "s":
                    board.current_figure.move(board, "rotate")
                elif move == "w":
                    board.current_figure.move(board, "rotate", _rotation_direction="ccw")
                else:
                    raise WrongMove
                board.current_figure.move(board, "down")
            else:
                board.devour()
                x, y = randint(1, xlen - 5), 19
                board.current_figure = Figure.from_point(x, y, shape=choice("oizlj"))
                if not board.current_figure.has_next_move(board):
                    raise ValueError("Game Over")
            board.flush()
        except WrongMove as e:
            print(f"Wrong Move, Try Again! {str(e)}")


main()
