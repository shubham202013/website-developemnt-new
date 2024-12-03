from common.models import MemBaseModel
from common.utils import generate_uuid
from database.db import mem_db


class ScreenerForEverest(mem_db.Model, MemBaseModel):
    id = mem_db.Column(mem_db.Integer, primary_key=True, autoincrement=True)
    sr = mem_db.Column(mem_db.Integer, nullable=True)
    stock_name = mem_db.Column(mem_db.String(255), nullable=True)
    symbol = mem_db.Column(mem_db.String(255), nullable=True)
    links = mem_db.Column(mem_db.String(255), nullable=True)
    percent_change = mem_db.Column(mem_db.Float, nullable=True)
    price = mem_db.Column(mem_db.Float, nullable=True)
    volume = mem_db.Column(mem_db.Integer, nullable=True)
    
    __tablename__ = "screener_for_everest"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'
