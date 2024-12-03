import json
import os
import time
from flask import request
import pandas as pd

from common.base import BaseListResource
from common.website_datetime import current_timestamp
from common.utils import error_response, get_filter_query, get_search_query, success_response
from config.authentication import authenticated
from common.config import memsql_engine
from nsepython import get_bhavcopy
from datetime import datetime, timedelta
from v1.bhavcopy.models import Bhavcopy
from v1.bhavcopy import queryset

class StoreBhavcopyToDatabaseResource(BaseListResource):
    decorators = [authenticated()]

    def get(self):
        """
        get all data with or without pagination
        """ 
        # current_date = datetime.now()

        # # Format the current date as 'DD-MM-YYYY'
        # formatted_date = current_date.strftime("%d-%m-%Y")
        
        # df = get_bhavcopy(str(formatted_date))

        # # 4. Store the DataFrame into the database
        # # 'bhavcopy_table' is the name of the table where data will be stored
        # df.to_sql('bhavcopy_table', memsql_engine, if_exists='replace', index=False)


        # Get the current date
        current_date = datetime.now()

        # Initialize an empty list to store DataFrames
        dataframes = []
        queryset.delete_bhavcopy_data({"IS_ACTIVE": True})
        # Loop through the last 200 days
        for i in range(50):
            # Calculate the date for the current iteration
            date_to_fetch = current_date - timedelta(days=i)
            
            # Format the date as 'DD-MM-YYYY'
            formatted_date = date_to_fetch.strftime("%d-%m-%Y")
            print('formated date', formatted_date)
            # Get the data for the formatted date
            try:
                df = get_bhavcopy(str(formatted_date))
                dataframes.append(df)
            except Exception as e:
                print(f'error for date {formatted_date}  --->', e)
            # Append the DataFrame to the list

        # Concatenate all DataFrames into one
        final_df = pd.concat(dataframes, ignore_index=True)

        # Store the final DataFrame into the database
        # final_df.to_sql('bhavcopy_table', memsql_engine, if_exists='replace', index=False)
        print('final_df', final_df)
        bhavcopy_data_list = []
        for _, row in final_df.iterrows():
            try:
                date1 = row[' DATE1'].strip()
                cv_to_date = datetime.strptime(date1, "%d-%b-%Y").date()
            except:
                date1 = None

            bhavcopy_data_list.append({
                "SYMBOL":row['SYMBOL'],
                "SERIES":row[' SERIES'],
                "DATE1":cv_to_date,
                "PREV_CLOSE":float(row[' PREV_CLOSE']),
                "OPEN_PRICE":float(row[' OPEN_PRICE']),
                "HIGH_PRICE":float(row[' HIGH_PRICE']),
                "LOW_PRICE":float(row[' LOW_PRICE']),
                "LAST_PRICE":row[' LAST_PRICE'],
                "CLOSE_PRICE":float(row[' CLOSE_PRICE']),
                "AVG_PRICE":float(row[' AVG_PRICE']),
                "TTL_TRD_QNTY":int(row[' TTL_TRD_QNTY']),
                "TURNOVER_LACS":float(row[' TURNOVER_LACS']),
                "NO_OF_TRADES":int(row[' NO_OF_TRADES']),
                "DELIV_QTY":row[' DELIV_QTY'],
                "DELIV_PER":row[' DELIV_PER'],

            })

        unique_entries = {}
        filtered_data = []

        for entry in bhavcopy_data_list:
            # Create a tuple (SYMBOL, DATE1) to check for duplicates
            key = (entry['SYMBOL'], entry['DATE1'])
            if key not in unique_entries:
                unique_entries[key] = entry
                filtered_data.append(Bhavcopy(**entry))
        
        print('bhavcopy_data_list', bhavcopy_data_list)
        if bhavcopy_data_list:
            queryset.delete_bhavcopy_data({"IS_ACTIVE": True})
            queryset.insert_bhavcopy_bulk_data(filtered_data)

        return success_response(data=[])

   