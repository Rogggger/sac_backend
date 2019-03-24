# coding: utf-8

from flask import Blueprint, request
from flask_login import login_required
from app.model.rest import Rest
from app.model.schedule import Schedule
from app.decorator.auth import admin_required
from app.libs.http import error_jsonify
from sqlalchemy import and_
from app.const.errors import InvalidParameters
from app.serializer.rest_approval import RestApprovalParaSchema
from app.libs.db import session

bp_rest_approval = Blueprint('rest', __name__, url_prefix='/rest')


@bp_rest_approval.route('/rest/<int:rest_id>', methods=['POST'])
@login_required
@admin_required
def rest():
    json = request.get_json()
    data, errors = RestApprovalParaSchema().load(json)

    if errors:
        return error_jsonify(InvalidParameters)

    rest = Rest.query.filter_by(Rest.id == data['rest_id']).first()
    session.query(Schedule).filter(and_(
        Schedule.user_id == rest.user_id,
        Schedule.week == rest.week,
        Schedule.time == rest.time
    )).delete()
    session.query(Rest).filter_by(Rest.id == data['rest_id']).delete()
    session.commit()