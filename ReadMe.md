# Xiangi - Chinese Chess

A game of Xiangqi- a battle between two armies with the goal of capturing the enemy's
general. This game is also known as Chinese Chess. A detailed description of rules and pieces can be found [here](https://en.wikipedia.org/wiki/Xiangqi).

![Board](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/board.png) | ![Helper Mode](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/helper.png)

## Playing:
* This game is played via the command line, and requires Python3
* Run Xiangqi_CLI.py to play
* Helper mode will display a list of positions that a designated piece can move to


* Players take turns moving one piece of their army at a time using algebraic notation (ex: a1)
* Red player goes first

## The Board:
* The board is separated into two camps- Black and Red.

* A main feature of the game is the **river**, which separates the two armies and affects Piece movement.
For example, if a soldier crosses the River, it can move horizontally as well.

* Generals and Advisors are limited to their respective **palaces**- the 3x3 middle space on the ends of the board that have diagonal lines.

## Special Rules:
* Moves cannot be made that leave the two Generals directly facing one another (no pieces in between)
* In general, pieces capture pieces of the opposing army by moving to their position.
* Winning involves checkmating the opposing camp (similar to western Chess)
* This version uses 'ranks' to refer to rows, and 'files' to refer to columns.

## Notes:
* This version does not implement perpetual check or chasing.