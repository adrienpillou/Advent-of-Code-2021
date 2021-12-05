class Segment:
    def __init__(self) -> None:
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def __repr__(self):
        return f"({self.x1},{self.y1}) -> ({self.x2},{self.y2})"
    