# coding: utf-8
import binascii
import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Sequence, Boolean, Text
from app.libs.db import db


class Department(db.Model):
    id = Column(Integer, Sequence('department_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # 部门名称
