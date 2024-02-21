
def detect_delimiter(path):
    with open(path, 'r') as f:
        first_line = f.readline()
        common_delimiters = ',', ';', '\t', '|'
        for delimiter in common_delimiters:
            if delimiter in first_line:
                return delimiter
            

