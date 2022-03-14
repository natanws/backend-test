from dataclasses import dataclass
import re
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from app.configs.database import db
from app.exceptions import EmailError, PhoneError

@dataclass
class UserModel(db.Model):
    name: str
    email: str
    phone: str
    points: int

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String, nullable=False)
    points = Column(Integer, nullable=False, default=1)

    @validates('email')
    def check_email(self, key, value):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w{2,3}){1,2}$'

        email = re.fullmatch(regex, value)

        if not email:
            raise EmailError

        return value

    @validates('phone')
    def check_phone(self, key, value):
        regex = r'\(?\d{2}\)?\d{4,5}\-?\d{4}'

        phone = re.fullmatch(regex, value)

        if not phone:
            raise PhoneError

        return value