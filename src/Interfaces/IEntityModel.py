from abc import ABC, abstractmethod
import pandas as pd
from typing import Type

class IEntityModel(ABC):
    
    @abstractmethod
    def new_from_sql_row(self, row: pd.Series):
        """Initialize the object from a SQL row (as a pandas Series)."""
        pass
    
    @abstractmethod
    def save_as_a_new_version(self, model_object: Type["IEntityModel"]):
        """Save the current object as a new version."""
        pass
    
    @abstractmethod
    def create_new(self) -> "IEntityModel":
        """Create and return a new instance of the model."""
        pass
