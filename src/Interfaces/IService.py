from abc import ABC, abstractmethod

class IService(ABC):
    """Base interface for all services in the application."""
    
    @abstractmethod
    def execute(self):
        """Execute a generic service action."""
        pass
