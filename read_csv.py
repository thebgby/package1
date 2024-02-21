import pandas as pd
from detect_delim import detect_delimiter
from detect_encoding import detect_encoding
from logging_setup import logging
def read_csv(path, chunksize):
    try:
        delimiter=detect_delimiter(path)
        encoding = detect_encoding(path)
        df = pd.read_csv(path, low_memory=False, encoding=encoding, delimiter=delimiter, chunksize=chunksize)
    except Exception as e:
        logging.error(e)
    return df
