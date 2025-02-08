from src.Classes.Base.ABaseSingleton import SingletonMeta


class ABaseView(metaclass=SingletonMeta):
    """Base class for Views ensuring singleton behavior."""
    pass