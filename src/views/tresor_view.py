import pygame
from views.tile_view import TileView
from tiles.colors import BLACK

class TresorView:
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        pygame.draw.rect(screen, BLACK, rect)