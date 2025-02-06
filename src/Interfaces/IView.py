from abc import ABC, abstractmethod
from typing import List

class IView(ABC):
    """Interface for views in the CinePass system."""
    
    @property
    @abstractmethod
    def choice(self) -> int:
        """Property for the user's choice."""
        pass
    
    @choice.setter
    @abstractmethod
    def choice(self, value: int):
        """Set the user's choice."""
        pass

    @property
    @abstractmethod
    def menu_list(self) -> List[str]:
        """Property for the list of menu options."""
        pass
