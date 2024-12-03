from marshmallow import Schema, fields


class SuperUserSchema(Schema):
    full_name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class LoginSchema(Schema):
    email = fields.Str(required=False)
    password = fields.Str(required=False)
    remember_me = fields.Bool(required=False, allow_none=True)
    device_id = fields.Str(required=False)
    device_type = fields.Str(required=False)
    company_id = fields.Str(required=False)
    is_google_signup = fields.Bool(required=False)
    google_signup_details = fields.Dict(required=False)


class ResetPasswordSchema(Schema):
    password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)
    company_id = fields.Str(required=False)


class SetPasswordSchema(Schema):
    password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)
    company_id = fields.Str(required=False)


class ForgotPasswordSchema(Schema):
    email = fields.Str(required=True)
    company_id = fields.Str(required=False)


class ChangePasswordSchema(Schema):
    old_password = fields.Str(required=True)
    new_password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)
    company_id = fields.Str(required=False)
