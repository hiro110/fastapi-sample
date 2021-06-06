from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP, Boolean, text
from sqlalchemy.sql.functions import current_timestamp
from pydantic import BaseModel

from db import Base, ENGINE
from .mixins import TimestampMixin

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255), unique=True, nullable=False)
    email = Column('email', String(255), unique=True, nullable=False)
    password = Column('password', String(255), nullable=False)
    token = Column('token', TEXT, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

#     def __init__(self, name, email, password, token):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.token = token
#         now = datetime.now()
#         self.created_at = now
#         self.updated_at = now

def main():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()
