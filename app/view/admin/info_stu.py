# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.info import Info
from app.model.schedule import Schedule
from app.decorator.auth import admin_required
from app.libs.http import jsonify, error_jsonify
from app.const.errors import NoStudentInfo

bp_info_stu = Blueprint('info', __name__, url_prefix='info')


@bp_info_stu.route('info/<int:user_id>', methods=['GET'])
@login_required
@admin_required
def info_stu():
    # 管理员查看学生信息

    user_id = request.args.get('user_id')
    info = Info.query.filter_by(Info.user_id == user_id).first()
    schedules = Schedule.query.filter_by(Schedule.user_id == user_id).all()

    if info is None:
        return error_jsonify(NoStudentInfo)

    if schedules is None:
        work_time = '无'  # 若学生未被安排工作，则返回无
    else:
        work_time = 0
        for schedule in schedules:
            work_time += schedule.time  # 若学生已被安排工作，则加和计算该学生的所有工作时段

    stu = {
        "name": info.name,
        "sex": info.sex,  # 0 代表女性，1代表男性
        "student_id": info.student_id,
        "phone": info.phone,
        "email": info.email,
        "financial_difficulties": info.financial_difficulties,  # Bool
        "work": info.work,  # 现任工作
        "school": info.school,  # 学院编号
        "experience": info.experience,  # 勤工助学经历
        "skill": info.skill,  # 特长
        "department_id": info.department_id,  # 申请部门编号
        "position_id": info.position_id,  # 申请岗位编号
        "free_time": info.free_time,  # 25位的一个二进制数，表示哪个时间段有空闲
        "work_time": work_time  # 表示哪个时间段已经排好了班
    }

    return jsonify(stu)
