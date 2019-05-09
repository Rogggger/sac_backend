# coding: utf-8
from marshmallow import Schema, fields


class RestParaSchema(Schema):
    week = fields.Integer(required=True, validate=lambda x: 0 < x <= 20)
    free_time = fields.Integer(required=True, validate=lambda x: 0 < x <= 2 ** 24)

class RestApprovalParaSchema(Schema):
    rest_id = fields.Integer(required=True)