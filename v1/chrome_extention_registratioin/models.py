import datetime
import os

from passlib.apps import django_context
from passlib.hash import django_pbkdf2_sha256 as handler
from six import python_2_unicode_compatible

from common.models import MemBaseModel
from common.website_datetime import current_timestamp
from common.utils import generate_uuid
from database.db import mem_db


class ChromeExtentionUser(mem_db.Model, MemBaseModel):
    id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)
    full_name = mem_db.Column(mem_db.String(255), nullable=True)
    email = mem_db.Column(mem_db.String(255), nullable=True)
    is_active = mem_db.Column(mem_db.Boolean, nullable=True, default=True)
    is_deleted = mem_db.Column(mem_db.Boolean, nullable=True, default=False)
    

    __tablename__ = "chrome_extention_user"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'
