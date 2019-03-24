# coding: utf-8
from sqlalchemy import Column, Integer, Sequence, Boolean
from app.libs.db import db


class Rest(db.Model):
    id = Column(Integer, Sequence('rest_id_seq'), primary_key=True, autoincrement=True)
    week = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)  # 时间段
    is_approval = Column(Boolean, nullable=False, default=0)
