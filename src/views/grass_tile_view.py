import pygame
from views.tile_view import TileView

class GrassTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles d'herbe dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        pygame.draw.rect(screen, (0, 255, 0), rect)
