import pygame

from tiles.colors import BLACK, WHITE, LAVA

class ScoreView:
    def draw(self, screen, score):
        font = pygame.font.SysFont("Arial", 20)
        rect_x, rect_y = 500, 10
        rect_width, rect_height = 100, 40
        timer_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, LAVA, timer_rect, border_radius=10)

        text_surf = font.render(f"score: {str(int(score))}", True, WHITE)

        text_rect = text_surf.get_rect(center=timer_rect.center)
        screen.blit(text_surf, text_rect) # Dessiner surface sur une autre