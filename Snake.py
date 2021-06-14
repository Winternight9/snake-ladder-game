class snake():
    def __init__(self, head: int, tail: int) -> None:
        self.validate(head, tail)
        self.head = head
        self.tail = tail

    def validate(self, head: int, tail: int) -> None:
        self.is_snake_descending(head, tail)
        self.is_minimum_snake_valid(head, tail)
        self.is_snake_head_equal_tail(head, tail)

    """return True when head > tail"""

    def is_snake_descending(self, head: int, tail: int) -> None:
        if head < tail:
            raise "snake not descending"

    """return True when min_snake_square > 1"""

    def is_minimum_snake_valid(self, head: int, tail: int) -> None:
        if min(head, tail) < 1:
            raise "snake lower than minimum"

    """return True when head != tail"""

    def is_snake_head_equal_tail(self, head: int, tail: int) -> None:
        if head == tail:
            raise "snake head equal to tail"

    def get_head(self) -> int:
        return self.head

    def set_head(self, newhead: int) -> None:
        self.head = newhead

    def get_tail(self) -> int:
        return self.tail

    def set_tail(self, newtail: int) -> None:
        self.tail = newtail
