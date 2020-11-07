# -*- coding: utf-8 -*-
# DBへの接続設定
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# 接続したいDBの基本情報を設定
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

# DBとの接続
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()
