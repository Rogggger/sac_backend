# coding: utf-8
from datetime import datetime

from flask import request, Blueprint
from flask_login import login_required

from app.model.schedule import Schedule
from app.model.info import Info
from app.libs.http import error_jsonify, jsonify
from app.decorator.auth import admin_required
from app.serializer.arrange import ArrangeParaSchema
from app.libs.db import session
from app.const.errors import InvalidParameters, NoStudentInfo

bp_admin_arrange = Blueprint('admin_arrange', __name__, url_prefix='/admin/arrange')


@bp_admin_arrange.route('/', methods=['POST'])
@login_required
@admin_required
def arrange():
    # 管理员排班审批
    json = request.get_json()
    data, errors = ArrangeParaSchema().load(json)

    if errors:
        return error_jsonify(InvalidParameters, errors)

    user_id = data['user_id']
    time = bin(data['time']).replace('0b', '')  # 将time转化为二进制数字符串
    time_list = [i for i in range(len(time)) if time[i] == '1']  # 提取所有有空的时间段

    info = Info.query.filter_by(Info.user_id == user_id).first()

    if info is None:
        return error_jsonify(NoStudentInfo, errors)

    now = datetime.now()
    year = now.strftime('%Y')
    month = int(now.strftime('%m'))

    for schedule_time in time_list:
        for wk in range(1, 21):
            schedule = Schedule(
                user_id=user_id,
                year=year,
                term=False if 2 <= month <= 7 else True,  # 判断学期
                week=wk + 1,
                time=schedule_time,
                department=info.department_id,
                position=info.position_id
            )
            session.add(schedule)
    session.commit()
    return jsonify({})
