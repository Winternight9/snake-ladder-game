from Snake import snake
from Player import player
from Ladder import ladder

snakeA = snake(7, 3)
snakeB = snake(10, 7)
listsnakes = [snakeA, snakeB]
playerA = player("Poom")
playerA.set_location(10)
ladderA = ladder(30, 40)
ladderB = ladder(5, 20)
listladders = [ladderA, ladderB]


def is_snake_chain_ladders(snake: snake):
    print(all(map(lambda ladder: snake.head != ladder.start, listladders)))


is_snake_chain_ladders(snakeA)
