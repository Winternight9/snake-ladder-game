from Board import board
from Player import player
from Dice import dice
from SnakeAndLadderGame import game
from Snake import snake
from Ladder import ladder


ladderA = ladder(30, 40)
ladderB = ladder(7, 19)
ladderC = ladder(19, 27)
ladderD = ladder(6, 23)
ladderE = ladder(82, 100)
listladders = [ladderA, ladderB, ladderC, ladderD, ladderE]

snakeA = snake(70, 50)
snakeB = snake(31, 4)
snakeC = snake(25, 13)
snakeD = snake(15, 4)
snakeE = snake(43, 35)
listsnakes = [snakeA, snakeB, snakeC, snakeD, snakeE]

playerA = player('Poom')
playerB = player('Korn')
playerC = player('Oon')
listplayers = [playerA, playerB, playerC]

boardA = board(size=100, snakes=listsnakes, ladders=listladders)
diceA = dice()

game = game(boardA, listplayers, diceA)
game.play()
