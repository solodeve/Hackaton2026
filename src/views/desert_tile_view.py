import pygame
from views.tile_view import TileView
from tiles.colors import YELLOW

class DesertTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles de désert dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        if pygame.image.get_extended():
            image = pygame.image.load("assets/tiles/tile_0_18.png")
            image = pygame.transform.scale(image, (50, 50)) 
            screen.blit(image, rect)
