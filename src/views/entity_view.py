import pygame
from utils import CELL_SIZE, GRID_SIZE
from tiles.colors import BLACK


class EntityView:
    """Cette classe est responsable de l'affichage du joueur dans le monde de jeu."""
    def draw(self, screen, entity):
        entity_pos = entity.getPos()
        pygame.draw.circle(screen, BLACK, (entity_pos.x, entity_pos.y), CELL_SIZE // 3)
