from common.models import MemBaseModel
from common.utils import generate_uuid
from database.db import mem_db


class ETFPlantationSymbols(mem_db.Model, MemBaseModel):
    id = mem_db.Column(mem_db.String(200), primary_key=True, default=generate_uuid)
    symbol_code = mem_db.Column(mem_db.String(255), nullable=True)

    __tablename__ = "etf_plantation_symbols_master"
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'
