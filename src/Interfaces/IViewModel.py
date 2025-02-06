from abc import ABC, abstractmethod

class IViewModel(ABC):
    """Base interface for all view models in the application."""

    @abstractmethod
    def initialize(self):
        """Initialize the view model."""
        pass
