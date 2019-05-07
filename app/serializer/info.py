from marshmallow import Schema, fields


class InfoParaSchema(Schema):
    department_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 2 ** 24)
    position_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 2 ** 24)
    time = fields.Integer(required=True, validate=lambda x: 0 < x <= 2 ** 24)
