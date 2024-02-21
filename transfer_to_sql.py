from read_csv import read_csv
import re
import os

def format_table_name(name):
        name = name.replace('.csv', '') # Remove the .csv extension
        name = re.sub(r'[^a-zA-Z0-9_]', '', name) # Remove all non-alphanumeric characters
        name = name.replace(' ', '') # Remove all spaces
        return name

def transfer_to_sql(engine,  chunksize, csv_path):
    for chunk in read_csv(csv_path, chunksize):
        table_name = format_table_name(os.path.basename(csv_path))
        chunk.to_sql(table_name, engine, if_exists="append", index=False)

