from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.user)
