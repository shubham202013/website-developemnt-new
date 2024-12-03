from marshmallow import Schema, fields


class GetReferralSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=False)
    referral_type = fields.Str(required=False)
    from_user_referral_amount = fields.Float(required=False)
    to_user_referral_amount = fields.Float(required=False)
    is_active = fields.Bool(required=False)
   

class CreateReferralSchema(Schema):
    title = fields.Str(required=True)
    referral_type = fields.Str(required=True)
    from_user_referral_amount = fields.Float(required=False)
    to_user_referral_amount = fields.Float(required=False)
    
    
