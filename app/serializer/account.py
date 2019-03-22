from marshmallow import Schema, fields


class AccountParaSchema(Schema):
    username = fields.String(required=True)
