# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required, current_user
from app.model.info import Info
from app.model.user import User
from app.libs.http import jsonify, error_jsonify
from app.libs.db import session
from app.const.errors import NoStudentInfo
from app.serializer.info import InfoModifyParaSchema
from app.const.errors import InvalidParameters

bp_info = Blueprint('info', __name__, url_prefix='/info')

@bp_info.route('/', methods=['GET'])
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
        'free_time': info.free_time,
        'on_position': info.on_position
    }

    return jsonify(ret)


@bp_info.route('/<int:user_id>/', methods=['POST'])
@login_required
def info_modify(user_id):
    json = request.get_json()
    data, errors = InfoModifyParaSchema().load(json)

    if errors:
        return error_jsonify(InvalidParameters)

    user = User.query.filter_by(User.user_id == user_id).first()

    if user is None:
        user = User(user_id=user_id,
                    username=data['username'],
                    is_admin=0)
        session.add(user)
        session.commit()
    else:
        session.commit()

    info = Info.query.filter_by(user_id=user.id).first()

    exist = 0
    if info is not None:
        exist = 1

    info = Info(student_id=data['student_id'],
                user_id=user_id,
                financial_difficulties=data['financial_difficulties'],
                work=data['work'],
                department_id=data['department_id'],
                position_id=data['position_id'],
                experience=data['experience'],
                skill=data['skill'],
                free_time=data['free_time'],
                school=data['school'],
                name=data['name'],
                sex=data['sex'],
                phone=data['phone'],
                email=data['email'],
                on_position=0)

    if exist == 0:
        session.add(info)

    session.commit()
