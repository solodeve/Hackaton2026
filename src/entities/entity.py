from abc import ABC, abstractmethod

from actions.action import Action
from utils import Position, Move
from random import randint


class Entity(ABC):
    """Classe de base pour les entités dans le monde de jeu."""
    def __init__(self, position: Position):
        self.pos = position
        self.color = None

    @abstractmethod
    def move(self, direction: Move):
        raise NotImplementedError(' ')

    @abstractmethod
    def effect_on(self, effect: Action):
        raise NotImplementedError(' ')
