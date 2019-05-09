# coding: utf-8

from flask import request, Blueprint
from flask_login import login_required
from app.model.schedule import Schedule
from app.model.info import Info
from app.libs.http import jsonify, error_jsonify
from app.const.errors import InvalidParameters
from sqlalchemy import and_
from app.serializer.schedule import ScheduleParaSchema

bp_schedule = Blueprint('schedule', __name__, url_prefix='/schedule')


@bp_schedule.route('/', methods=['GET'])
@login_required
def schedule():
    # 学生用户查看排班表
    json = request.get_json()
    data, errors = ScheduleParaSchema().load(json)

    week = data['week']
    department = data['department']
    position = data['position']

    if week is None or department is None or position is None:
        return error_jsonify(InvalidParameters)

    students = Schedule.query.filter(and_(
        Schedule.week == week,
        Schedule.department == department,
        Schedule.position == position
    )).all()

    names = []

    for student in students:
        name = Info.query.filter_by(student.user_id == Info.user_id).first().name
        if name is None:
            names.append('无')
        else:
            names.append(name)

    return jsonify(names)
