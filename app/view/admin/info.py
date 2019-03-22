# coding: utf-8

from flask import request
from flask_login import login_required
from app.model.info import Info
from app.decorator.auth import admin_required
from app.libs.http import jsonify, error_jsonify
from sqlalchemy import and_
from app.const.errors import NoStudentInfo
from app.view.admin import bp_admin


@bp_admin.route('/info', methods=['GET'])
@login_required
@admin_required
def info():
    # 管理员查看排版系统

    department_id = request.args.get('department_id')
    position_id = request.args.get('position_id')
    time = request.args.get('time')
    # TODO: 这里应该对上面得到的三个变量做校验，包括类型和数值

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
            'name': i.name,
            'sex': i.sex,
            'student_id': i.student_id
        }  # 学生简略信息
        students.append(student)

    return jsonify(info)
