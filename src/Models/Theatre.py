# from sqlalchemy import Column, Integer, String
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Theatre(ABaseModel):
#     __tablename__ = "theatres"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True, nullable=False)
#     number_of_seats = Column(Integer, nullable=False)
#
#     def __repr__(self):
#         return f"Theatre(ID={self.id}, Name={self.name}, Seats={self.number_of_seats})"
