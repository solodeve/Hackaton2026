import pygame
from tiles.colors import BLACK


class EnemyView:
    """Cette classe est responsable de l'affichage de l'énnemi dans le monde de jeu."""
    def draw(self, screen, rect):
        pygame.draw.rect(screen, BLACK, rect)