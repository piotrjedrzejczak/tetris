# Tetris - Recruitment Task

There are 5 pieces In this version of Tetris:

```shell
****
 
*
*
**

*
*
**

*
**
*

**
**
```

...and they fall down a 20x20 tetris board:

```shell
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*******************
```

The game starts with a random piece appearing at the top of the board. The user is then prompted to make a move:

• a (return): move piece left
• d (return): move piece right
• w (return): rotate piece counter clockwise
• s (return): rotate piece clockwise

If the move user selects is valid, then it is executed and the screen redrawn (you can use printf()/ cout / System.out.println(), etc to redraw the entire board). If it is not valid then they are again prompted to enter a valid move. Note that the game only updates after the user has entered a valid action.

A valid move is defined thus: The piece is altered as per the user’s input, and then displaced by 1 row downwards. If the piece, drawn at it’s new location, is not outside the bounds of the board, and does not overlap any pieces that previously fell, then it is a valid move.

If the piece’s new position is such that it allows no valid move, then a new piece appears along the top of the board, randomly positioned along the x-axis. If this new piece happens offer no valid move, then the game is over and the program exits.
