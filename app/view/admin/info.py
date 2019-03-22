# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.info import Info
from app.decorator.auth import admin_required
from app.libs.http import jsonify, error_jsonify
from sqlalchemy import and_
from app.const.errors import NoStudentInfo

bp_account = Blueprint('info', __name__, url_prefix='/info')


@bp_account.route('/', methods=['GET'])
@login_required
@admin_required
def info():
    # 管理员排班审批

    department_id = request.args.get('department_id')
    position_id = request.args.get('position_id')
    time = request.args.get('time')

    time_list = [i for i in range(len(time)) if time[i] == '1']  # 提取所有有空的时间段

    info = Info.query.filter(and_(
        Info.department_id == department_id,
        Info.position_id == position_id,
        Info.free_time & time != 0
    )).all()

    if info is None:
        return error_jsonify(NoStudentInfo)

    students = []
    for i in info:
        student = {
            'name':i.name,
            'sex':i.sex,
            'student_id':i.student_id
        }
        students.append(student)

    return jsonify(info)