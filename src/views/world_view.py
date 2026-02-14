import pygame
from tiles.PortailTile import PortailTile
from utils import CELL_SIZE, GRID_SIZE
from tiles.desert_tile import DesertTile
from tiles.water_tile import WaterTile
from tiles.grass_tile import GrassTile
from views.desert_tile_view import DesertTileView
from views.portail_view import PortailTileView
from views.water_tile_view import WaterTileView
from views.grass_tile_view import GrassTileView

class WorldView:
    """ 
    Cette classe est responsable de l'affichage du monde de jeu, y compris les tiles et la caméra centrée sur le joueur.
    Elle utilise des vues dédiées pour dessiner les différents types de tiles."""
    def __init__(self):
        self.tile_views = {
            DesertTile: DesertTileView(),
            WaterTile: WaterTileView(),
            PortailTile: PortailTileView()
            WaterTile: WaterTileView(),
            GrassTile: GrassTileView()
        }

    def draw(self, screen, grid, player_pos):
        # CALCUL DE LA CAMÉRA
        # On calcule le décalage pour que le joueur soit au centre de l'écran
        offset_x = player_pos.x - (GRID_SIZE // 2)
        offset_y = player_pos.y - (GRID_SIZE // 2)

        # Rendu de la fenêtre visible
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                world_x = x + offset_x
                world_y = y + offset_y
                
                tile = grid.get_tile(world_x, world_y)
                
                # Dessin du tile via sa vue dédiée
                view = self.tile_views.get(type(tile))
                if view:
                    rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    view.draw(screen, rect)
