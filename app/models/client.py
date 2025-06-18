from sqlalchemy.orm import relationship, foreign
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String)
    status = Column(String)
    comment = Column(Text, nullable=True)
    date_created = Column(DateTime)
    user_id = Column(Integer, index=True)  # Без ForeignKey

    user = relationship(
        "User",
        back_populates="clients",
        primaryjoin="foreign(Client.user_id) == User.id"
    )

    visit_logs = relationship("VisitLog", back_populates="client", cascade="all, delete")
