import pygame
import game
import eventmanager as evmgr
from tiles.colors import BLACK
from utils import CELL_SIZE, GRID_SIZE, HEIGHT, WIDTH
from listener import Listener
from views.player_view import PlayerView
from views.world_view import WorldView
from menu import Menu   
from views.timer_view import TimerView
from views.score_view import ScoreView


class GraphicalView(Listener):
    """
    Cette classe est responsable de l'affichage graphique du jeu en utilisant Pygame. 
    Elle écoute les événements du jeu et met à jour l'affichage en conséquence. 
    Elle utilise des sous-vues pour dessiner le monde et le joueur.
    """

    def __init__(self, ev_manager, model):
        """
        ev_manager: l'instance de EventManager pour s'abonner aux événements du jeu
        model: l'instance du modèle de jeu pour accéder aux données du jeu à afficher       

        La fonction d'initialisation configure les attributs de la classe,
        s'abonne aux événements du jeu et initialise les sous-vues pour le joueur et le monde.
        """

        self.ev_manager = ev_manager
        ev_manager.register(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
        
        # Sub-views
        self.player_view = PlayerView()
        self.world_view = WorldView()
        self.timer_view = TimerView()
        self.score_view = ScoreView()

    def notify(self, event):
        """
        Reçoit les événements du jeu et met à jour l'affichage en conséquence.
         - InitializeEvent: initialise l'affichage graphique
         - QuitEvent: ferme l'affichage graphique et quitte le jeu
         - TickEvent: met à jour l'affichage du jeu en cours
        """

        if isinstance(event, evmgr.InitializeEvent):
            self.initialize()
        elif isinstance(event, evmgr.QuitEvent):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, evmgr.TickEvent):
            if not self.isinitialized:
                return
            self.renderplay(self.model.player,self.model.grid)
            self.clock.tick(30)

    def renderplay(self,player,grid):
        """
        Fonction de rendu qui met à jour l'affichage du jeu en cours.
         - player: l'instance du joueur pour accéder à sa position et son état
         - grid: l'instance de la grille du jeu pour accéder à l'état du monde
         - timer: l'instance du compe à rebours de la partie
        """
        self.draw(player,grid)
    
    def draw(self,player,grid):
        self.screen.fill((255, 255, 255))

        
        
        # Delegate drawing to sub-views

        # self.model.menu
        if not self.model.menu.get_game_on():
            self.model.menu.afficher_menu(self.screen)
        else:
            if self.model.win: 
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render('GAME WIN',False,(0,0,0))
                GRID_SIZE//2
                self.screen.blit(textsurface,(0,0))
            else:
                self.world_view.draw(self.screen, grid, player.pos)
                self.player_view.draw(self.screen)
        

                self.timer_view.draw(self.screen, self.model.timer)
                self.score_view.draw(self.screen, self.model.score)

        pygame.display.flip()

    def initialize(self):
        """
        Initialise l'affichage graphique du jeu en configurant Pygame et les sous-vues.
        """

        _ = pygame.init()
        # pygame.font.init() # Disabled for Python 3.14 compatibility
        pygame.display.set_caption('Extraction Game')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        # self.smallfont = pygame.font.Font(None, 40) # Disabled for Python 3.14 compatibility
        self.smallfont = None
        self.isinitialized = True