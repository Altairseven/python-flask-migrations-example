from sqlalchemy import Column, DateTime, String, Integer, func
from app_base import db
##Fijate que importamos la db inicializada desde app_base, no desde app

class Student(db.Model):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    createdAt = Column(DateTime, default= func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"