from common.utils import PAGE_SIZE
import os
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv()


def get_page_size():
    return PAGE_SIZE


# MEMSQL Configuration
memsql_uri = os.environ.get("MYSQL_CONNECTION", "")

memsql_engine = create_engine(memsql_uri)
