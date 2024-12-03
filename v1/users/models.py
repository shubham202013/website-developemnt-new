import datetime
import os

from passlib.apps import django_context
from passlib.hash import django_pbkdf2_sha256 as handler
from six import python_2_unicode_compatible

from common.models import MemBaseModel
from common.website_datetime import current_timestamp
from common.utils import generate_uuid
from database.db import mem_db


class User(mem_db.Model, MemBaseModel):
    user_id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)
    full_name = mem_db.Column(mem_db.String(255), nullable=True)
    email = mem_db.Column(mem_db.String(255), nullable=True)
    is_active = mem_db.Column(mem_db.Boolean, nullable=True, default=True)
    is_deleted = mem_db.Column(mem_db.Boolean, nullable=True, default=False)
    username = mem_db.Column(mem_db.String(255), nullable=True)
    password = mem_db.Column(mem_db.String(500), nullable=True)
    dial_code = mem_db.Column(mem_db.String(255), nullable=True)
    phone_number = mem_db.Column(mem_db.String(255), nullable=True)
    image = mem_db.Column(mem_db.String(255), nullable=True)

    phone_verified = mem_db.Column(mem_db.Boolean, nullable=True, default=0)

    # for block
    is_blocked = mem_db.Column(mem_db.Boolean, default=False)
    blocked_date_time = mem_db.Column(mem_db.Float, nullable=True)


    # for forgot password
    forgot_password_verify_code = mem_db.Column(mem_db.String(255), nullable=True)
    forgot_password_verify_code_date = mem_db.Column(mem_db.Float, nullable=True)

    is_superuser = mem_db.Column(mem_db.Boolean, default=False)
    referral_code = mem_db.Column(mem_db.String(255), nullable=True)
    invite_referral_code = mem_db.Column(mem_db.String(255), nullable=True)
   
    google_auth_id = mem_db.Column(mem_db.String(355), nullable=True)

    __tablename__ = "user_master"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    def __repr__(self):
        return '<User %r>' % self.get_full_name()

    # def set_password(self, password):
    #     return handler.hash(password)

    def save(self):
        if self.user_id is None:
            mem_db.session.add(self)
        return mem_db.session.commit()

    def destroy(self):
        mem_db.session.delete(self)
        return mem_db.session.commit()

    def check_password(self, password, hash_password):
        """
        Verify Django algo password
        """
        try:
            result = django_context.verify(password, hash_password)
        except Exception as e:
            print("\n django_context.verify Error : ", e)
            result = False
        return result


@python_2_unicode_compatible
class Token(mem_db.Model):
    """
    This is a mongoengine adaptation of DRF's default Token.
    The default authorization token model.
    """
    id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)

    key = mem_db.Column(mem_db.String(255))
    created = mem_db.Column(mem_db.DateTime, default=datetime.datetime.now)
    # Relational
    user = mem_db.Column(mem_db.Text)

    __tablename__ = "auth_token"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        if not self.key:
            self.key = self.generate_key()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
        return super().save(*args, **kwargs)

    def generate_key(self):
        import binascii

        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

class UserWallet(mem_db.Model):
    """
    This is a mongoengine adaptation of DRF's default Token.
    The default authorization token model.
    """
    id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)

    user_id = mem_db.Column(mem_db.String(255), nullable=True)
    wallet_amount = mem_db.Column(mem_db.Float, nullable=True)

    __tablename__ = "auth_token"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'