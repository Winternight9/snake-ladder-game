from typing import List
from Snake import snake
from Ladder import ladder


class board():
    def __init__(self, size: int, snakes: List[snake], ladders: List[ladder]) -> None:
        self.finalsquare = size
        self.snakes: List[snake] = []
        self.ladders: List[ladder] = []
        self.assign_ladders(ladders)
        self.assign_snakes(snakes)

    """TODO: change function from check all snakes to single snake instead"""

    def assign_snakes(self, snakes: List[snake]) -> None:
        for snake in snakes:
            self.add_snake(snake)

    def assign_ladders(self, ladders: List[ladder]) -> None:
        for ladder in ladders:
            self.add_ladder(ladder)

    def add_snake(self, snake: snake) -> None:
        if self.is_snake_valid(snake):
            self.snakes.append(snake)
        else:
            print(f"Fail to assign snakes({snake.head},{snake.tail})")

    def add_ladder(self, ladder: ladder) -> None:
        if self.is_ladder_valid(ladder):
            self.ladders.append(ladder)
        else:
            print(f"Fail to assign ladders({ladder.start},{ladder.end})")

    def is_snake_valid(self, snake: snake) -> bool:
        return self.is_max_value_snake_less_than_finalsquare(snake) \
            and self.is_snake_head_not_chain_ladders(snake) \
            and self.is_snake_head_not_chain_snakes_head(snake) \
            and self.is_snake_head_not_chain_snakes_tail(snake) \
            and self.is_snake_tail_not_chain_snakes_head(snake) \
            and self.is_snake_tail_end_not_chain_ladders_start(snake)

    def is_ladder_valid(self, ladder: ladder) -> bool:
        return self.is_max_value_ladder_less_than_finalsquare(ladder) \
            and self.is_ladder_start_not_chain_snakes(ladder) \
            and self.is_ladder_start_not_chain_ladders_start(ladder) \
            and self.is_ladder_start_not_chain_ladders_end(ladder) \
            and self.is_ladder_end_not_chain_ladders_start(ladder) \
            and self.is_ladder_end_not_chain_snakes_head(ladder)

    """return True when max_snake_square <= finalsquare"""

    def is_max_value_snake_less_than_finalsquare(self, snake: snake) -> bool:
        return max(snake.head, snake.tail) <= self.finalsquare

    """return True when max_ladder_square <= finalsquare"""

    def is_max_value_ladder_less_than_finalsquare(self, ladder: ladder) -> bool:
        return max(ladder.start, ladder.end) <= self.finalsquare

    def is_snake_head_not_chain_ladders(self, snake: snake) -> bool:
        return all(map(lambda ladder: snake.head != ladder.start, self.ladders))

    def is_ladder_start_not_chain_snakes(self, ladder: ladder) -> bool:
        return all(map(lambda snake: ladder.start != snake.head, self.snakes))

    def is_snake_head_not_chain_snakes_head(self, snake: snake) -> bool:
        return all(map(lambda oldsnake: snake.head != oldsnake.head, self.snakes))

    def is_snake_head_not_chain_snakes_tail(self, snake: snake) -> bool:
        return all(map(lambda oldsnake: snake.head != oldsnake.tail, self.snakes))

    def is_snake_tail_not_chain_snakes_head(self, snake: snake) -> bool:
        return all(map(lambda oldsnake: snake.tail != oldsnake.head, self.snakes))

    def is_ladder_start_not_chain_ladders_start(self, ladder: ladder) -> bool:
        return all(map(lambda oldladder: ladder.start != oldladder.start, self.ladders))

    def is_ladder_start_not_chain_ladders_end(self, ladder: ladder) -> bool:
        return all(map(lambda oldladder: ladder.start != oldladder.end, self.ladders))

    def is_ladder_end_not_chain_ladders_start(self, ladder: ladder) -> bool:
        return all(map(lambda oldladder: ladder.end != oldladder.start, self.ladders))

    def is_snake_tail_end_not_chain_ladders_start(self, snake: snake) -> bool:
        return all(map(lambda ladder: snake.tail != ladder.start, self.ladders))

    def is_ladder_end_not_chain_snakes_head(self, ladder: ladder) -> bool:
        return all(map(lambda snake: ladder.end != snake.head, self.snakes))

    """TODO: logic snake chain"""

    def get_snakes(self) -> List[snake]:
        return self.snakes

    def get_ladders(self) -> List[ladder]:
        return self.ladders

    def get_finalsquare(self) -> int:
        return self.finalsquare

    def get_gamestatus(self) -> bool:
        return self.gamestatus

    def set_gamestatus(self, newgamestatus: bool) -> None:
        self.gamestatus = newgamestatus

    def set_finalsquare(self, newfinalsquare: int) -> None:
        self.finalsquare = newfinalsquare
