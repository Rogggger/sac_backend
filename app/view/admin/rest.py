# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.info import Info
from app.model.rest import Rest
from app.model.schedule import Schedule
from app.decorator.auth import admin_required
from app.libs.http import jsonify, error_jsonify
from app.const.errors import NoStudentInfo
from app.const.errors import InvalidParameters
from app.serializer.rest_approval import RestApprovalParaSchema
from app.libs.db import session
from sqlalchemy import and_

bp_admin_rest = Blueprint('admin_rest', __name__, url_prefix='/admin/rest')


@bp_admin_rest.route('/', methods=['GET'])
@login_required
@admin_required
def get_rest():
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


@bp_admin_rest.route('/<int:rest_id>/', methods=['POST'])
@login_required
@admin_required
def approve_rest(rest_id):
    json = request.get_json()
    data, errors = RestApprovalParaSchema().load(json)

    if errors:
        return error_jsonify(InvalidParameters)

    rest = Rest.query.filter_by(Rest.id == rest_id).first()
    rest.is_approval = 1
    schedule = Schedule.query.filter(and_(
        Schedule.user_id == rest.user_id,
        Schedule.week == rest.week,
        Schedule.time == rest.time
    ))
    schedule.is_rest = 1
    session.commit()
