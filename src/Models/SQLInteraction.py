from src.Classes.Base.ABaseSingleton import Singleton
from src.Classes.SQL.CinePassDb import CinePassDb


class SQLInteraction(Singleton):
    """Singleton class to provide a single session instance for database interactions."""

    def __init__(self):
        self.Db = CinePassDb().get_session()