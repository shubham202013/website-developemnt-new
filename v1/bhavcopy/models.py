# from common.models import MemBaseModel
from common.utils import generate_uuid
from database.db import mem_db



class Bhavcopy(mem_db.Model):
    # id = mem_db.Column(mem_db.Integer)
    SYMBOL = mem_db.Column(mem_db.String, primary_key=True)  # Corresponds to SYMBOL (text)
    SERIES = mem_db.Column(mem_db.String, nullable=True)  # Corresponds to SERIES (text)
    DATE1 = mem_db.Column(mem_db.DATE, primary_key=True)  # Corresponds to DATE1 (text)
    PREV_CLOSE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to PREV_CLOSE (double)
    OPEN_PRICE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to OPEN_PRICE (double)
    HIGH_PRICE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to HIGH_PRICE (double)
    LOW_PRICE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to LOW_PRICE (double)
    LAST_PRICE = mem_db.Column(mem_db.String, nullable=True)  # Corresponds to LAST_PRICE (text)
    CLOSE_PRICE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to CLOSE_PRICE (double)
    AVG_PRICE = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to AVG_PRICE (double)
    TTL_TRD_QNTY = mem_db.Column(mem_db.BigInteger, nullable=True)  # Corresponds to TTL_TRD_QNTY (bigint)
    TURNOVER_LACS = mem_db.Column(mem_db.Float, nullable=True)  # Corresponds to TURNOVER_LACS (double)
    NO_OF_TRADES = mem_db.Column(mem_db.BigInteger, nullable=True)  # Corresponds to NO_OF_TRADES (bigint)
    DELIV_QTY = mem_db.Column(mem_db.String, nullable=True)  # Corresponds to DELIV_QTY (text)
    DELIV_PER = mem_db.Column(mem_db.String, nullable=True)  # Corresponds to DELIV_PER (text)
    IS_ACTIVE = mem_db.Column(mem_db.Boolean, default=True)
    
    __tablename__ = 'bhavcopy_table'
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'mysql'
