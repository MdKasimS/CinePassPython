# from sqlalchemy import Column, Integer, DateTime, ForeignKey
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Show(ABaseModel):
#     __tablename__ = "shows"
#
#     id = Column(Integer, primary_key=True, index=True)
#     movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
#     theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
#     start_date = Column(DateTime, nullable=False)
#     end_date = Column(DateTime, nullable=False)
#     platinum_seat_rate = Column(Integer, nullable=False)
#     gold_seat_rate = Column(Integer, nullable=False)
#     silver_seat_rate = Column(Integer, nullable=False)
#
#     def __repr__(self):
#         return f"Show(ID={self.id}, MovieID={self.movie_id}, TheatreID={self.theatre_id})"
