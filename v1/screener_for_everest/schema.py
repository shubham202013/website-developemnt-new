from marshmallow import Schema, fields


class GetSFESchema(Schema):
    id = fields.Int(dump_only=True)
    sr = fields.Int(required=False)
    stock_name = fields.Str(required=False)
    symbol = fields.Str(required=False)
    links = fields.Str(required=False)
    percent_change = fields.Float(required=False)
    price = fields.Float(required=False)
    volume = fields.Int(required=False)
