from src.Classes.Base.ABaseSingleton import SingletonMeta
from src.Classes.SQL.CinePassDb import CinePassDb

class SQLInteraction(metaclass=SingletonMeta):
    """Singleton class to provide a single session instance for database interactions."""

    def __init__(self):
        super().__init__()
        self.Db = CinePassDb().get_session()