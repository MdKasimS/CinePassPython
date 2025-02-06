from abc import ABC, abstractmethod

class IUtility(ABC):
    """Interface representing utility services."""
    
    @abstractmethod
    def perform_utility_task(self):
        """Perform a general utility task."""
        pass
