from typing import List
from Snake import snake
from Ladder import ladder
from Board import board
from Player import player
from Dice import dice


class game():
    def __init__(self, board: board, players: player, dice: dice) -> None:
        self.gamestatus = False
        self.players = players
        self.board = board
        self.dice = dice

    def is_player_hit_snake(self, player: player, snake: snake) -> bool:
        return player.location == snake.head

    def is_player_hit_ladder(self, player: player, ladder: ladder) -> bool:
        return player.location == ladder.start

    def player_hit_snake(self, player: player) -> None:
        for snake in self.board.snakes:
            if self.is_player_hit_snake(player, snake):
                player.set_location(snake.tail)
                print(
                    f"You Hit head of the snake now you are on square: {player.location}")

    def player_hit_ladder(self, player: player) -> None:
        for ladder in self.board.ladders:
            if self.is_player_hit_ladder(player, ladder):
                player.set_location(ladder.end)
                print(
                    f"You Hit the ladder now you are on square: {player.location}")

    def move(self, player: player) -> None:
        self.player_move(player, self.dice.roll_dice())
        self.player_hit_snake(player)
        self.player_hit_ladder(player)

    def player_move(self, player: player, diceface: int) -> None:
        player.location += diceface
        print(f"Now you are on square: {player.location}")

    def player_reach_last_square(self, player: player) -> bool:
        return player.location >= self.board.finalsquare

    def play(self) -> None:
        self.gamestatus = True
        while self.gamestatus:
            for player in self.players:
                print(f"{player.get_player_name()} Turn")
                command = input("Press (r) to roll or press (e) to exit: ")
                if command == "r":
                    self.move(player)
                    if self.player_reach_last_square(player):
                        self.exit()
                        print(f"{player.name} Win!")
                        break
                elif command == "e":
                    self.exit()

    def exit(self) -> None:
        self.gamestatus = False
