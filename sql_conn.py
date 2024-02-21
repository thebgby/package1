import pyodbc
from logging_setup import logging

def sql_con(instance_name, database_name):
    ## SQL Server connection
    drivers = [driver for driver in pyodbc.drivers() if 'ODBC Driver' in driver]

    if drivers:
        try:
            driver_name = drivers[0]
            conn = f"mssql+pyodbc://{instance_name}/{database_name}?driver={driver_name}"
            return conn
        except Exception as e:
            logging.error(e)
    else:
        logging.error("No driver found, set manually in sql_conn.py file.")
        
    
    