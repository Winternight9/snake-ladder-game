class ladder():
    def __init__(self, start: int, end: int) -> None:
        self.validate(start, end)
        self.start = start
        self.end = end

    def validate(self, start: int, end: int) -> None:
        self.is_ladder_ascending(start, end)
        self.is_minimum_ladder_valid(start, end)
        self.is_ladder_start_equal_end(start, end)

    """return True when start < end"""

    def is_ladder_ascending(self, start: int, end: int) -> None:
        if start > end:
            raise "ladder not ascending"

    """return True when min_ladder_square > 1"""

    def is_minimum_ladder_valid(self, start: int, end: int) -> None:
        if min(start, end) < 1:
            raise "ladder lower than minimum"

    """return True when start != end"""

    def is_ladder_start_equal_end(self, start: int, end: int) -> None:
        if start == end:
            raise "ladder start equal to end"

    def get_start(self) -> int:
        return self.head

    def set_start(self, newstart: int) -> None:
        self.start = newstart

    def get_end(self) -> int:
        return self.end

    def set_end(self, newend: int) -> None:
        self.end = newend
