import logging
import os
import sys

# logging for errors
logging.basicConfig(
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/error.log'),  # Output log messages to a file
        logging.StreamHandler(sys.stdout),  # Output log messages to the console
    ]
)

# logging row count
def log_row_count(filename, row_count):
    try:
        log_entry = f"ROW COUNT FOR {filename} : {row_count}\n"
        with open('logs/rowcount.txt', 'a') as file:
            file.write(log_entry)
    except Exception as e:
        logging.error(e)

# logging files counts
def file_counts(folder_path):
    extension_counts = {}
    for filename in os.listdir(folder_path):
        _, extension = os.path.splitext(filename)
        extension = extension.upper()  
        if extension not in extension_counts:
            extension_counts[extension] = 1
        else:
            extension_counts[extension] += 1

    with open('logs/file_counts.txt', 'w') as log_file:
        for extension, count in extension_counts.items():
            log_file.write(f"{extension}: {count}\n")

# list all files to log file
def file_list(folder_path):
    with open("logs/files_list.txt", 'w') as log_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                log_file.write(f"{file_path}\n")