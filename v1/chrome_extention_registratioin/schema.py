from marshmallow import Schema, fields


class GetContactUsSchema(Schema):
    id = fields.Str(dump_only=True)
    email = fields.Str(required=False)
   
    

class CreateContactUsSchema(Schema):
    email = fields.Str(required=True)
    