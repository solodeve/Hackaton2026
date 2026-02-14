import pygame
from utils import CELL_SIZE, GRID_SIZE
from tiles.colors import BLACK

class PlayerView:
    """Cette classe est responsable de l'affichage du joueur dans le monde de jeu."""
    def draw(self, screen):
        # DESSIN DU JOUEUR (Toujours au centre de l'écran)
        screen_center = (
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2 - 10,
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2 - 10
        )
        # pygame.draw.circle(screen, BLACK, screen_center, CELL_SIZE // 3)
        if pygame.image.get_extended():
            image = pygame.image.load("assets/characters/basic/char_idle_down_anim.gif")
            image = pygame.transform.scale(image, (20, 20)) 
            screen.blit(image, screen_center)

        # char_idle_down_anim
