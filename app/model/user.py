# coding: utf-8
from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.libs.db import db


class User(db.Model):
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)  # 用户名
    is_admin = Column(Boolean, nullable=False)  # 是否老师
