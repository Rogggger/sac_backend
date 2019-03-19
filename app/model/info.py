# coding: utf-8
from sqlalchemy import Column, Integer, String, Sequence, Boolean, Text
from app.libs.db import db


class Info(db.Model):
    id = Column(Integer, Sequence('info_id_seq'), primary_key=True, autoincrement=True)
    student_id = Column(String(50), nullable=False)
    user_id = Column(String(50), nullable=False)
    financial_difficulties = Column(Boolean, nullable=False)  # 是否经济困难
    work = Column(Text)  # 现任职位
    department_id = Column(Integer, nullable=False)  # 申请部门
    position_id = Column(Integer, nullable=False)  # 申请岗位
    experience = Column(Text)  # 勤工助学经历
    skill = Column(Text)  # 有何特长技能
    free_time = Column(Integer, nullable=False)
    school = Column(Integer, nullable=False)  # 学院
    name = Column(String(50), nullable=False)  # 真实姓名
    sex = Column(Integer, nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    on_position = Column(Boolean, nullable=False, default=False)  # 是否被排班
