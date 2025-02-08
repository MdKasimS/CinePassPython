from abc import abstractmethod, ABC
from typing import List

from src.Classes.Base.ABaseSingleton import SingletonMeta


class ABaseView(metaclass=SingletonMeta):
    """Base class for Views ensuring singleton behavior and enforcing menu structure."""

    MenuList: List[str]  # Explicitly declare the type for IDE support
    Menu: dict  # Explicitly declare the type for IDE support
    Choice: int

    def __init__(self):
        super().__init__()
        self.MenuList: List[str] = []  # List of menu options
        self.Menu: dict = {}  # Dictionary mapping menu options to functions
        self.Choice = 0

    @abstractmethod
    def View(self):
        """This method must be implemented by derived classes to define view behavior."""
        pass