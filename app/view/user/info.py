# coding: utf-8

from flask import Blueprint
from flask_login import login_required, current_user
from app.model.info import Info
from app.libs.http import jsonify, error_jsonify
from app.const.errors import NoStudentInfo

bp_account = Blueprint('info', __name__, url_prefix='/info')

@bp_account.route('/', methods=['GET'])
@login_required
def info():
    # 学生用户获取个人信息

    info = Info.query.filter_by(user_id=current_user.id).first()

    if info is None:
        return error_jsonify(NoStudentInfo)

    ret = {
        'username': current_user.username,
        'sex': info.sex,
        'student_id': info.student_id,
        'financial_difficulties': info.financial_difficulties,
        'phone': info.phone,
        'email': info.email,
        'name': info.name,
        'school': info.school,
        'work': info.work,
        'department_id': info.department_id,
        'position_id': info.position_id,
        'experience': info.experience,
        'skill': info.skill,
        'free_time': info.free_time
    }

    return jsonify(ret)