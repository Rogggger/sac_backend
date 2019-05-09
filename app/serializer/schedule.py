from marshmallow import Schema, fields


class ScheduleParaSchema(Schema):
    department_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    position_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    week = fields.Integer(required=True, validate=lambda x: 0 < x <= 20)
