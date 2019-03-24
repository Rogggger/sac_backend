# coding: utf-8
from marshmallow import Schema, fields


class RestApprovalParaSchema(Schema):
    rest_id = fields.Integer(required=True)
