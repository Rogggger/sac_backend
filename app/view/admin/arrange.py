# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.schedule import Schedule
from app.model.info import Info
from app.libs.http import error_jsonify
from app.decorator.auth import admin_required
from app.serializer.arrange import ArrangeParaSchema
from app.libs.db import session

bp_account = Blueprint('arrange', __name__, url_prefix='/arrange')


@bp_account.route('/', methods=['POST'])
@login_required
@admin_required
def arrange():
    # 管理员排班审批
    json = request.get_json()
    data, errors = ArrangeParaSchema().load(json)

    if errors:
        return error_jsonify(1001, errors)

    user_id = data['user_id']
    time = bin(data['time']).replace('0b', '')  # 将time转化为二进制数字符串
    time_list = [i for i in range(len(time)) if time[i] == '1']  # 提取所有有空的时间段

    info = Info.query.filter_by(Info.user_id == user_id).first()

    if info is None:
        return error_jsonify(1003, errors)

    for schedule_time in time_list:
        for wk in range(20):
            schedule = Schedule(
                user_id=user_id,
                year=time.strftime('%Y'),
                term=not 1 < int(time.strftime('%m')) < 7,  # 判断学期
                week=wk + 1,
                time=schedule_time,
                department=info.department_id,
                position=info.position_id
            )
            session.add(schedule)
            session.commit()
