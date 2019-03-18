# coding: utf-8
import binascii
import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Sequence, Boolean, Text
from app.libs.db import db


class User(db.Model):
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)  # 用户名
    name = Column(String(50), nullable=False)  # 真实姓名
    sex = Column(Integer, nullable=False)
    student_id = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    is_admin = Column(Boolean, nullable=False)  # 是否老师