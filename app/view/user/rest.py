# coding: utf-8

from flask import request, Blueprint
from flask_login import login_required, current_user
from app.model.schedule import Schedule
from sqlalchemy import and_
from app.model.rest import Rest
from app.libs.http import error_jsonify
from app.libs.db import session
from app.serializer.rest import RestParaSchema
from app.const.errors import InvalidParameters

bp_rest = Blueprint('rest', __name__, url_prefix='/rest')


@bp_rest.route('/', methods=['POST'])
@login_required
def rest():
    # 学生用户请假
    json = request.get_json()
    data, errors = RestParaSchema().load(json)

    if errors:
        return error_jsonify(InvalidParameters)

    week = data['week']
    time = data['free_time']

    schedule = Schedule.query.filter(and_(Schedule.user_id == current_user.id,
                                          Schedule.week == week,
                                          Schedule.time == time)).first()
    if schedule is None:
        return error_jsonify(1002, errors)

    rest = Rest(user_id=current_user.id,
                week=week,
                time=time)
    session.add(rest)
    session.commit()
