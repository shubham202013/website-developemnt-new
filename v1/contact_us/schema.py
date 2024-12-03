from marshmallow import Schema, fields


class GetContactUsSchema(Schema):
    user_id = fields.Str(dump_only=True)
    full_name = fields.Str(required=False)
    email = fields.Str(required=False)
    subject = fields.Str(required=False)
    message = fields.Str(required=False)
    

class CreateContactUsSchema(Schema):
    full_name = fields.Str(required=True)
    email = fields.Str(required=True)
    subject = fields.Str(required=False)
    message = fields.Str(required=False)
    