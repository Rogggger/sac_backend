# coding: utf-8
from sqlalchemy import Column, Integer, Sequence, Boolean
from app.libs.db import db


class Schedule(db.Model):
    id = Column(Integer, Sequence('schedule_id_seq'), primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)  # 用户名
    term = Column(Boolean, nullable=False)  # 是否第二学期
    week = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)  # 时间段
    department = Column(Integer, nullable=False)  # 部门
    position = Column(Integer, nullable=False)  # 岗位
    is_rest = Column(Boolean, nullable=False, default=0)