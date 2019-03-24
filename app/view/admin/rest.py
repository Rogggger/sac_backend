# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.rest import Rest
from app.model.info import Info
from app.decorator.auth import admin_required
from app.libs.http import jsonify, error_jsonify
from app.const.errors import NoStudentInfo

bp_rest = Blueprint('rest', __name__, url_prefix='/rest')


@bp_rest.route('/', methods=['GET'])
@login_required
@admin_required
def rest():
    # 管理员查看请假信息
    rest = Rest.query.filter_by().all

    if rest is None:
        return error_jsonify(NoStudentInfo)

    students = []

    for i in rest:
        info = Info.query.filter_by(info.user_id == i.user_id)

        student = {
            'user_id': i.user_id,
            'name': info.name,
            'rest_id': i.id,
            'week': i.week,
            'free_time': i.time
        }
        students.append(student)

    return jsonify(students)