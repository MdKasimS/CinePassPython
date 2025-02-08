from src.Classes.Base.ABaseSingleton import SingletonMeta
from src.Classes.SQL.CinePassDb import CinePassDb


class SQLInteraction(SingletonMeta):
    """Singleton class to provide a single session instance for database interactions."""

    def __init__(self):
        self.Db = CinePassDb().get_session()