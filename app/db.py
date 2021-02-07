# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = os.getenv('MYSQL_SERVER')
database_name = os.getenv('MYSQL_DB')
user_name = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
    user_name,
    password,
    host,
    database_name,
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

Base = declarative_base()
