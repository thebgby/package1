import os
import pandas as pd
from detect_delim import detect_delimiter
from detect_encoding import detect_encoding
from logging_setup import log_row_count

def row_count(folder_path):
    for root,_, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                filepath = os.path.join(root, file)
                encoding = detect_encoding(filepath)
                delimiter = detect_delimiter(filepath)
                df = pd.read_csv(os.path.join(root,file), low_memory=False, encoding=encoding, delimiter=delimiter)
                log_row_count(file, df.shape[0])
