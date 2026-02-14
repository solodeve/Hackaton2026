from abc import ABC, abstractmethod

from actions.action import Action
from utils import Position, Move
from random import randint
from entities.entity import Entity 


class Ennemy(Entity):
    """Classe de base pour les entités dans le monde de jeu."""
    def __init__(self):
        self._cache = [200, 200]    
    
    def move(self):
        speed = [randint(-1, 1), randint(-1, 1)]
        
        self.pos.x += speed[0]
        self.pos.y += speed[1]
    
    def getPos(self): 
        return self.pos

    def effect_on(self, effect: Action):
        pass
