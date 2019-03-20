# coding: utf-8
from marshmallow import Schema, fields


class ArrangeParaSchema(Schema):
    user_id = fields.Steing(required=True)
    free_time = fields.Integer(required=True, validate=lambda x: 0 < x <= 2 ** 24)
