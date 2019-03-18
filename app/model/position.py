# coding: utf-8
from sqlalchemy import Column, Integer, String, Sequence
from app.libs.db import db


class Position(db.Model):
    id = Column(Integer, Sequence('position_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # 岗位名称
    department_id = Column(Integer, nullable=False)  # 所属部门
