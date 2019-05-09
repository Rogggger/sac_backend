from marshmallow import Schema, fields


class InfoParaSchema(Schema):
    department_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    position_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    time = fields.Integer(required=True, validate=lambda x: 0 < x <= 2 ** 24)


class InfoModifyParaSchema(Schema):
    name = fields.String(required=True)
    sex = fields.Integer(required=True)
    student_id = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    financial_difficulties = fields.Boolean(required=True)
    work = fields.String(required=False)
    school = fields.Integer(required=True)
    experience = fields.String(required=False)
    skill = fields.String(required=False)
    department_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    position_id = fields.Integer(required=True, validate=lambda x: 0 <= x <= 10000)
    time = fields.Integer(required=True, validate=lambda x: 0 < x <= 2 ** 24)
    username = fields.String(required=True)
