

from flask import request
from common.base import BaseListResource
from common.utils import error_response, success_response
from config.authentication import authenticated, current_identity
import csv
from database.helper.memsql import get_aggregate_data_v2
from v1.ETF import queryset as etf_queryset

from v1.ETF.models import ETFSymbols
from v1.bhavcopy import queryset as bhavcopy_queryset
from datetime import datetime, timedelta

from v1.bhavcopy.models import Bhavcopy
from database.db import mem_db
from sqlalchemy import func, desc


class ETFSymbolImportResource(BaseListResource):
    decorators = [authenticated()]

    def post(self):
        current_user_id = current_identity['user_id'] if current_identity else None

        data_file = request.files['file']

        if not data_file:
            return error_response(message="Please upload file")

        decoded_file = data_file.read().decode("utf-8", errors="replace").splitlines()
        csvreader = csv.reader(decoded_file)

        rows = []
        for row in csvreader:
            rows.append(row)

        data_file.close()
        del rows[0]

        eft_symbol_code_data = []

        for data in rows:
            symbol_code = data[0]
            eft_symbol_code_data.append(ETFSymbols(**{
                 "symbol_code": symbol_code
            }))
            print("symbol_code", symbol_code)

        if eft_symbol_code_data:
                etf_queryset.delete_etfSymbols_data(where_condition={"is_active":1})
                etf_queryset.insert_etfSymbols_bulk_data(eft_symbol_code_data)

        return success_response(data="")
    

class ETFSymbolResource(BaseListResource):
    decorators = [authenticated()]

    def post(self):
        """
        get all data with or without pagination
        """
        where_query = {}
        response_data = []
        where_query['is_active'] = True

        if request.args.get("is_active"):
            where_query.pop("is_active")

        # search_condition = get_search_query(self.search_fields, request) if self.search_fields else dict()
        # filter_condition = get_filter_query(self.filter_fields, request) if self.filter_fields else dict()
        # if search_condition:
        #     where_query.update(**search_condition)
        # if filter_condition:
        #     where_query.update(**filter_condition)

        etf_symbols_objects = etf_queryset.get_all_etfSymbols_data(where_query=where_query)
        etf_symbol_list = []
        for etf_symbol in etf_symbols_objects:
            try:
                etf_symbol_code = etf_symbol.get('symbol_code', '').split(':')[1]
                etf_symbol_list.append(etf_symbol_code)
            except Exception as e:
                print('Error in Symbol', e)
        print('etf_symbol_list', etf_symbol_list)

        latest_per_symbol = (
            mem_db.session.query(
                Bhavcopy.SYMBOL,
                func.max(Bhavcopy.DATE1).label("latest_date")
            )
            .filter(Bhavcopy.SYMBOL.in_(etf_symbol_list))  # Filter by the symbol list
            .group_by(Bhavcopy.SYMBOL)
            .subquery()
        )

        # Join the main Bhavcopy table with the subquery to get the latest record per symbol
        get_cmp_data = (
            mem_db.session.query(Bhavcopy)
            .join(
                latest_per_symbol,
                (Bhavcopy.SYMBOL == latest_per_symbol.c.SYMBOL) &
                (Bhavcopy.DATE1 == latest_per_symbol.c.latest_date)
            )
            .all()
        )
        symbol_wise_cmp_data_dect = {i.SYMBOL: i.LAST_PRICE  for i in get_cmp_data}
        print(symbol_wise_cmp_data_dect)


        get_21_dma_data = []
        for symbol in etf_symbol_list:
            # Subquery to get the latest 21 dates for the current symbol
            latest_dates_subquery = (
                mem_db.session.query(Bhavcopy.DATE1)
                .filter(Bhavcopy.SYMBOL == symbol.upper())
                .order_by(desc(Bhavcopy.DATE1))
                .limit(21)
                .subquery()
            )

            # Query to get data for the latest 21 dates for the current symbol
            symbol_data_query = (
                mem_db.session.query(Bhavcopy)
                .filter(Bhavcopy.SYMBOL == symbol.upper())
                .filter(Bhavcopy.DATE1.in_(latest_dates_subquery))
                .order_by(desc(Bhavcopy.DATE1))
                .all()
            )

            # Add results for the current symbol to the list
            get_21_dma_data.extend(symbol_data_query)

        get_daily_avg_volum_data = []
        for symbol in etf_symbol_list:
            # Subquery to get the latest 21 dates for the current symbol
            latest_dates_subquery = (
                mem_db.session.query(Bhavcopy.DATE1)
                .filter(Bhavcopy.SYMBOL == symbol.upper())
                .order_by(desc(Bhavcopy.DATE1))
                .limit(31)
                .subquery()
            )

            # Query to get data for the latest 21 dates for the current symbol
            symbol_data_query = (
                mem_db.session.query(Bhavcopy)
                .filter(Bhavcopy.SYMBOL == symbol.upper())
                .filter(Bhavcopy.DATE1.in_(latest_dates_subquery))
                .order_by(desc(Bhavcopy.DATE1))
                .all()
            )

            # Add results for the current symbol to the list
            get_daily_avg_volum_data.extend(symbol_data_query)



        symbol_wise_close_price_list = {}

        for i in get_21_dma_data:
            if i.SYMBOL in symbol_wise_close_price_list:
                symbol_wise_close_price_list[i.SYMBOL].append(float(i.CLOSE_PRICE))
            else:
                symbol_wise_close_price_list[i.SYMBOL] = [float(i.CLOSE_PRICE)]

        symbol_wise_daily_volum_list = {}

        for j in get_daily_avg_volum_data:
            if j.SYMBOL in symbol_wise_daily_volum_list:
                symbol_wise_daily_volum_list[j.SYMBOL].append(float(j.TTL_TRD_QNTY))
            else:
                symbol_wise_daily_volum_list[j.SYMBOL] = [float(j.TTL_TRD_QNTY)]

        for symbol in etf_symbol_list:
            # print('symbol', symbol)
            close_price_list = symbol_wise_close_price_list.get(symbol.upper(), 0)
            print(len(close_price_list))
            dma = sum(close_price_list) / len(close_price_list) if close_price_list else 0
            daily_volum_list = symbol_wise_daily_volum_list.get(symbol.upper(), 0)
            avg_volum = sum(daily_volum_list) / len(daily_volum_list) if daily_volum_list else 0
            data_dict = dict()
            data_dict['symbol'] = symbol
            # print(symbol_wise_cmp_data_dect.get(symbol, 0))
            data_dict['cmp'] = float(symbol_wise_cmp_data_dect.get(symbol.upper(), 0))
            data_dict['21_dma'] = dma
            data_dict['21dma_vs_cmp'] = float(symbol_wise_cmp_data_dect.get(symbol.upper(), 0)) - dma
            data_dict['daily_avg_volume'] = round(avg_volum, 2)
            response_data.append(data_dict)


        # print('get_cmp_data', get_cmp_data)

        return success_response(data=response_data)