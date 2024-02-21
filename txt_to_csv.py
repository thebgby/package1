import pandas as pd
import os
from detect_delim import detect_delimiter
from logging_setup import logging


def convert_text_files_to_csv(folder_path): # folder_path is the path to the folder containing the .txt files
    try:
        for root,_, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                    filename = file.replace(".txt", ".csv")
                    output_file_path = os.path.join(root,filename)
                    file_path = os.path.join(root, file)
                    delimiter = detect_delimiter(file_path)
                    df = pd.read_csv(file_path, delimiter=delimiter)
                    df.to_csv(output_file_path,index=False)
    except Exception as e:
        logging.error(e)
                

