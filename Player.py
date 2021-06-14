class player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.location = 1

    def get_location(self) -> int:
        return self.location

    def get_player_name(self) -> str:
        return self.name

    def set_player_name(self, newname: str) -> None:
        self.name = newname

    def set_location(self, newlocation: int) -> None:
        self.location = newlocation
