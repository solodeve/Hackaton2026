import random
from tiles.colors import *
from tiles.desert_tile import DesertTile
from tiles.tile import Tile
from tiles.water_tile import WaterTile
from tiles.grass_tile import GrassTile
from utils import Position
from tiles.PortailTile import PortailTile




class LazyGrid:
    """Génération procédurale infinie et déterministe."""
    def __init__(self, seed: int):
        self.seed = seed
        self._cache = {}

    def get_tile(self, x: int, y: int) -> Tile:
        # 1. Vérifier le cache (modifications joueur)
        if (x, y) in self._cache:
            return self._cache[(x, y)]
        
        # 2. Sécurité pour le point de départ
        if x == 1000 and y == 1000:
            return DesertTile(Position(x, y)) 

        # 3. Génération basée sur la seed et les coordonnées
        rng = random.Random(f"{self.seed}_{x}_{y}")
        rand = rng.random()
        
        if rand < 0.7:   return  DesertTile(Position(x, y))  # Majorité de tuiles désertiques
        elif rand < 0.701 :   return PortailTile(Position(x,y)) # Egzlité donne un portail
        if rand < 0.5:   return  DesertTile(Position(x, y))  # Majorité de tuiles désertiques
        elif rand >= 0.5 and rand <= 0.8: return GrassTile(Position(x,y)) # grasse 
        else:             return WaterTile(Position(x, y))   # Quelques tuiles d'eau

    def set_tile(self, x: int, y: int, tile: Tile):
        self._cache[(x, y)] = tile