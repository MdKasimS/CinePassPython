# from sqlalchemy import Column, Integer, String, Float
# from src.Classes.Base.ABaseModel import ABaseModel
#
# class Movie(ABaseModel):
#     __tablename__ = "movies"
#
#     id = Column(Integer, primary_key=True, index=True)
#     movie_name = Column(String, nullable=False)
#     director_name = Column(String, nullable=False)
#     producer_name = Column(String, nullable=False)
#     genre = Column(String, nullable=False)
#     language = Column(String, nullable=False)
#     duration = Column(Float, nullable=False)
#     story = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f"Movie(ID={self.id}, Name={self.movie_name}, Director={self.director_name})"