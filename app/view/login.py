from flask import Blueprint, request
from flask_login import login_user

from app.libs.db import session
from app.libs.http import error_jsonify, jsonify
from app.model.user import User
from app.serializer.account import AccountParaSchema
from app.const.errors import InvalidParameters

bp_login = Blueprint('login', __name__, url_prefix='/login')


@bp_login.route('/', methods=['POST'])
def login():
    """
    最基本的登录视图，只能通过post发送登录信息
    如果发送的参数不对返回400
    :return: HTTP状态码和json信息
    """
    json = request.get_json()
    data, errors = AccountParaSchema().load(json)
    if errors:
        return error_jsonify(InvalidParameters, errors, 400)

    username = data['username']
    attempt_user = User.query.filter_by(username=username).first()
    if attempt_user is None:
        is_admin = True if 'admin' in username else False
        new_user = User(username=username, is_admin=is_admin)
        session.add(new_user)
        session.commit()
        login_user(new_user)
        return jsonify({})
    else:
        login_user(attempt_user)
        return jsonify({})
