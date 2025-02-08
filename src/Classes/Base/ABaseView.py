from abc import abstractmethod

from src.Classes.Base.ABaseSingleton import SingletonMeta


class ABaseView(SingletonMeta):
    """Base class for Views ensuring singleton behavior."""
    def __init__(self):
        self.Choice = 0
        self.MenuList = []
        self.Menu = {}

    @abstractmethod
    def View(self):
        pass

    def LoadMenuList(self):
        pass