import pygame
from utils import WIDTH, HEIGHT
from tiles.colors import BLACK, LAVA, WHITE

class TimerView:
    """Cette classe est responsable du compte à rebours de la partie du joueur."""
    def draw(self, screen, compte_rebours):
        font = pygame.font.SysFont("Arial", 40)
        rect_x, rect_y = 10, 10
        rect_width, rect_height = 100, 50
        timer_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, BLACK, timer_rect, border_radius=10)

        text_surf = font.render(str(int(compte_rebours)), True, WHITE)

        text_rect = text_surf.get_rect(center=timer_rect.center)
        screen.blit(text_surf, text_rect) # Dessiner surface sur une autre
        
        
