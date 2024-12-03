# from database.db import mongo_db
from database.db import mem_db
from sqlalchemy import Column, String
import datetime
from common.website_datetime import current_timestamp


# class BaseModel(mongo_db.Document):
#     """
#     Base model MongoDB
#     """
#     timezone_offset = mongo_db.StringField(max_length=200, blank=True, null=True, db_column='timezone_offset')
#     company_id = mongo_db.StringField(blank=True, null=True, max_length=255, db_column='company_id')
#     is_active = mongo_db.BooleanField(db_index=True, default=True, db_column='is_active')
#     created_by = mongo_db.StringField(blank=True, max_length=255, null=True, db_column='created_by')
#     created_date = mongo_db.DateTimeField(blank=True, null=True, db_column='created_date')
#     updated_by = mongo_db.StringField(blank=True, max_length=255, null=True, db_column='updated_by')
#     updated_date = mongo_db.DateTimeField(blank=True, null=True, db_column='updated_date')

#     meta = {'abstract': True, 'index_cls': False}


class MemBaseModel(object):
    """
    common model with default common fields
    """

    timezone_offset = mem_db.Column(mem_db.String(255), nullable=True)
    company_id = mem_db.Column(mem_db.String(255), nullable=True)
    is_active = mem_db.Column(mem_db.Boolean, default=True)
    created_by = mem_db.Column(mem_db.String(255), nullable=True)
    created_date = mem_db.Column(mem_db.Numeric(precision=20, scale=2), nullable=True, default=current_timestamp)
    updated_by = mem_db.Column(mem_db.String(255), nullable=True)
    updated_date = mem_db.Column(mem_db.Numeric(precision=20, scale=2), nullable=True, default=current_timestamp)