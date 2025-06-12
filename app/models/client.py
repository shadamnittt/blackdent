from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String)
    status = Column(String)  # "надежный" или "проблемный"
    comment = Column(Text, nullable=True)
    date_created = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    # user = relationship("User")  # если есть модель User
