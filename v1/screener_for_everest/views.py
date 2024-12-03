

from flask import request
from common.base import BaseListResource
from common.utils import error_response, success_response
from config.authentication import authenticated, current_identity
import csv
from database.helper.memsql import get_aggregate_data_v2
from v1.screener_for_everest import queryset as sfe_queryset

from v1.screener_for_everest.models import ScreenerForEverest
from v1.screener_for_everest.helper import scrape_sfe_data
# from v1.bhavcopy import queryset as bhavcopy_queryset
from datetime import datetime, timedelta

from v1.screener_for_everest.schema import GetSFESchema

# from database.db import mem_db
# from sqlalchemy import func



class MigrateScreenerForEverestResource(BaseListResource):
    decorators = [authenticated()]

    def get(self):
        """
        get all data with or without pagination
        """

        sfe_data_list = []
        sfe_data = scrape_sfe_data()
        for _, row in sfe_data.iterrows():
            sfe_data_list.append(ScreenerForEverest(**{
                "sr": int(row['Sr.']),
                "stock_name": row['Stock Name'],
                "symbol": row['Symbol'],
                "links": row['Links'],
                "percent_change": float(row['% Chg'].replace('%', '')),
                "price": float(row['Price']),
                "volume": int(row['Volume'].replace(',', ''))
            }))

        if sfe_data_list:
            sfe_queryset.delete_screener_for_everest_data(where_condition={"is_active":1})
            sfe_queryset.insert_screener_for_everest_bulk_data(sfe_data_list)
        
        return success_response(data={})
    
class ScreenerForEverestResource(BaseListResource):
    decorators = [authenticated()]

    get_data = sfe_queryset.get_screener_for_everest_data
    get_all_data = staticmethod(sfe_queryset.get_all_screener_for_everest_data)
    insert_data = staticmethod(sfe_queryset.insert_screener_for_everest_data)
    count_data = staticmethod(sfe_queryset.get_screener_for_everest_count)

    search_fields = []
    filter_fields = []
    order_by = []
    data_label = 'data'

    get_response_schema = GetSFESchema

    apply_pagination = True
