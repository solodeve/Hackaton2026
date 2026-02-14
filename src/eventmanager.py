from dataclasses import dataclass
from typing import Any, Optional
from weakref import WeakKeyDictionary
from abc import ABC, abstractmethod
from utils import Move
from listener import Listener



@dataclass(frozen=True)
class Event(ABC):
    """Classe de base utilisant les dataclasses pour la gestion automatique du __repr__."""

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass(frozen=True)
class QuitEvent(Event):
    """Événement pour signaler que le jeu doit se terminer."""
    def __str__(self) -> str:
        return "Quit Event"


@dataclass(frozen=True)
class TickEvent(Event):
    """Événement pour signaler une mise à jour du jeu (tick)."""
    def __str__(self) -> str:
        return "Tick Event"


@dataclass(frozen=True)
class InitializeEvent(Event):
    """Événement pour signaler l'initialisation du jeu."""
    def __str__(self):
        return "Initialize Event"


@dataclass(frozen=True)
class InputEvent(Event):
    """Événement pour signaler une entrée utilisateur."""
    input_type: Move
    click_pos: Optional[tuple[int, int]]

    def __str__(self) -> str:
        return f"{super().__str__()}: type={self.input_type}, pos={self.click_pos}"

class MouseEvent(Event):
    """Événement pour signaler une entrée utilisateur."""
    def __init__(self, click_pos: tuple[int, int]):
            self.click_pos = click_pos

    def __str__(self) -> str:
        return f"{super().__str__()}: pos={self.click_pos}"






class EventManager:
    """Coordonne la communication entre le Model, la View et le Controller."""

    def __init__(self):
        # On utilise un set pour les weak refs si on n'a pas besoin de valeurs (v2.0+).
        self._listeners: WeakKeyDictionary[Listener, None] = WeakKeyDictionary()

    def register(self, listener: Listener):
        self._listeners[listener] = True

    def unregister(self, listener: Listener):
        self._listeners.pop(listener, None)

    def post(self, event: Event):
        if not isinstance(event, TickEvent):
            print(event)

        for listener in list(self._listeners.keys()):
            listener.notify(event)