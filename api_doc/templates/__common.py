from marshmallow import Schema, fields


class CommonResponseSchema(Schema):
    success = fields.Str(required=False)
    message = fields.Str(required=False)
    status = fields.Int(required=False)


class LogoutResponseSchema(Schema):
    success = fields.Str(required=False)
    message = fields.Str(required=False)
    status = fields.Int(required=False)


class DeleteResponseSchema(Schema):
    success = fields.Str(required=False)
    message = fields.Str(required=False)
    status = fields.Int(required=False)


class NoSchema(Schema):
    pass
