# Xiangi - Chinese Chess

A game of Xiangqi- a battle between two armies with the goal of capturing the enemy's
general. This game is also known as Chinese Chess. A detailed description of rules and pieces can be found [here](https://en.wikipedia.org/wiki/Xiangqi).

![Game Start](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/main.png)
![Board](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/board.png) ![Board](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/board2.png)
![Helper Mode](https://raw.githubusercontent.com/mcastillo22/Xiangqi/master/Screenshots/helper.png)

## Prerequisites:
* This game can be played using the command line or using GUI
* Requires Python3
* Python3 installation instructions can be found [here](https://realpython.com/installing-python/)

## Playing:
* On the CLI:
  * Download  Xiangqi.py, XiangqiPieces.py, and main.py
* Run Xiangqi_CLI.py to play
  * For example: open a new command line and navigate to the directory where files have been downloaded
  * Type `python3 Xiangqi_CLI.py` and hit `Enter`
* Helper mode will display a list of positions that a designated piece can move to


* Players take turns moving one piece of their army at a time using algebraic notation (ex: a1)
* Red player goes first
* Enter `0`, `quit`, or `q` at any prompt to quit

### The Board:
* The board is separated into two camps- Black and Red.

* A main feature of the game is the **river**, which separates the two armies and affects Piece movement.
For example, if a soldier crosses the River, it can move horizontally as well.

* Generals and Advisors are limited to their respective **palaces**- the 3x3 middle space on the ends of the board that have diagonal lines.

### Pieces:
#### General
* The desired piece to capture. Similar to the King in western Chess
* Limited to the palace
* Can move one spot orthogonally
* Cannot jump over other pieces

#### Advisors
* 2x Advisors located next to the General
* Limited to the palace
* Can move one spot diagonally
* Cannot jump over other pieces

#### Elephants
* 2x Elephants located next to Advisors
* Can move exactly two spots diagonally
* Cannot cross the river
* Cannot jump over other pieces

#### Horses
* 2x Horses located next to the Elephants
* Move one spot orthogonally, then one spot diagonally
* Cannot jump over other pieces (unlike the Horse in western Chess)

#### Rooks
* 2x Rooks located next to Horses
* Can move any distance orthogonally
* Cannot jump over other pieces

#### Cannons
* 2x Cannons, behind the line of Soldiers
* Can move any distance orthogonally
* To capture a piece, the Cannon *must* first jump over another piece

#### Soldiers
* 5x Soldiers located two lines behind the River 
* Can only move one spot forward
* When a Soldier crosses the River, it may move one spot horizontally as well
* Cannot retreat (move backward)

## Special Rules:
* Moves cannot be made that leave the two Generals directly facing one another (no pieces in between)
* In general, pieces capture pieces of the opposing army by moving to their position.
* Winning involves checkmating the opposing camp (similar to western Chess)
* This version uses 'ranks' to refer to rows, and 'files' to refer to columns.

## Notes:
* This version does not implement perpetual check or chasing.
* This version does not implement trading pieces in the beginning of the game