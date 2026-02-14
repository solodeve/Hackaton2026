import pygame
from views.tile_view import TileView

class GrassTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles d'herbe dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        # assets/tiles/grass/tile_0_16.png
        # pygame.draw.rect(screen, (0, 255, 0), rect)
        if pygame.image.get_extended():
            image = pygame.image.load("assets/tiles/grass/tile_0_16.png")
            image = pygame.transform.scale(image, (40, 40)) 
            screen.blit(image, rect)
