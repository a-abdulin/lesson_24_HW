from marshmallow import Schema, fields


class RequestJsonSchema(Schema):
    file_name = fields.Str(required=True)
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

