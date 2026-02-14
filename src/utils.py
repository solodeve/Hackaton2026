from dataclasses import dataclass
from enum import Enum

# --- CONFIGURATION ---
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 15
CELL_SIZE = WIDTH // GRID_SIZE

class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


@dataclass
class Position:
    x: int
    y: int

    def move(self, direction: Move):
        match direction:
            case Move.UP:
                self.y -= 1
            case Move.DOWN:
                self.y += 1
            case Move.LEFT:
                self.x -= 1
            case Move.RIGHT:
                self.x += 1
            case _:
                raise ValueError(f"Direction non reconnue : {direction}")