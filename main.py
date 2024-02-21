from sql_conn import sql_con
from transfer_to_sql import transfer_to_sql
from logging_setup import  file_counts, file_list
from txt_to_csv import convert_text_files_to_csv
from row_count import row_count
import os

def main():
    # get variables from input.txt file
    with open("input.txt", 'r') as file: 
        data = file.readlines() 
        for line in data: 
            if line.startswith('source_path'):                  # If the line starts with 'source_path'
                source_directory = line.split('=')[1].strip()
            elif line.startswith('instance_name'): 
                instance_name = line.split('=')[1].strip()
            elif line.startswith('database_name'): 
                database_name = line.split('=')[1].strip() or "main"

    convert_text_files_to_csv(source_directory)
    row_count(source_directory)
    file_counts(source_directory)
    file_list(source_directory)

    engine = sql_con(instance_name, database_name)

    chunksize = 5000000 ## chunksize for split large csv files

    for root,_, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".csv"):
                transfer_to_sql(engine,chunksize,os.path.join(root,file))

main()


    

    

    

    
