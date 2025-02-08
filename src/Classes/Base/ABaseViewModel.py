from src.Classes.Base.ABaseSingleton import SingletonMeta


class ABaseViewModel(metaclass=SingletonMeta):
    """Base class for ViewModels ensuring singleton behavior."""

    def __init__(self):
        super().__init__()