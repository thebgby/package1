import chardet

def detect_encoding(path):
    result = chardet.detect(open(path, 'rb').read(100000))
    return result['encoding']