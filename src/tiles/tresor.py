from utils import Position,Move
from entities.entity import Entity
from tiles.tile import Tile

class TresorTile(Tile):
    def __init__(self, position: Position):
        super().__init__(position)

    def on(self, entity: Entity):
        return None
    

 