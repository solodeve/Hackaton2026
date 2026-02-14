from eventmanager import *
import pygame


class Menu:
    def __init__(self, ev_manager):
        """
        ev_manager: l'instance de EventManager pour s'abonner aux événements du jeu
        """
        self.ev_manager = ev_manager
        ev_manager.register(self)
        self.game_on = False
    
    def notify(self, event):
        if isinstance(event, MouseEvent):
            if not self.game_on:
                click_pos = event.click_pos
                if 210 <= click_pos[0] <= 410 and 150 <= click_pos[1] <= 250:
                    self.game_on = True
                elif 210 <= click_pos[0] <= 410 and 350 <= click_pos[1] <= 450:
                    self.ev_manager.post(QuitEvent())
    def get_game_on(self):
        return self.game_on
    def afficher_menu(self, screen):
        font = pygame.font.Font(None, 74)
        text_play = font.render("Jouer", True, (255, 255, 255))
        text_quit = font.render("Quitter", True, (255, 255, 255))
        
        play_rect = pygame.Rect(210, 150, 200, 100)
        quit_rect = pygame.Rect(210, 350, 200, 100)
        

    
        screen.fill((0, 0, 0))
        screen.blit(text_play, (play_rect.x + 30, play_rect.y + 25))
        screen.blit(text_quit, (quit_rect.x + 10, quit_rect.y + 25))
    
        pygame.draw.rect(screen, (0, 128, 255), play_rect, 5)
        pygame.draw.rect(screen, (0, 128, 255), quit_rect, 5)
    
        pygame.display.flip()
    