import datetime
import os

from passlib.apps import django_context
from passlib.hash import django_pbkdf2_sha256 as handler
from six import python_2_unicode_compatible

from common.models import MemBaseModel
from common.website_datetime import current_timestamp
from common.utils import generate_uuid
from database.db import mem_db


class Referral(mem_db.Model, MemBaseModel):
    id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)
    title = mem_db.Column(mem_db.String(255), nullable=True)
    referral_type = mem_db.Column(mem_db.String(255), nullable=True)
    from_user_referral_amount = mem_db.Column(mem_db.Float, default=0)
    to_user_referral_amount = mem_db.Column(mem_db.Float, default=0)

    __tablename__ = "referral_master"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'
