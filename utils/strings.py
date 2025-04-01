import json
import base64
import hashlib
import sys

def quote(command):
    return command.replace("\\", "\\\\").replace("\"", "\\\"")

def base64encode(data):
    if sys.version_info.major >= 3 and isinstance(data, str):
        data = data.encode('utf-8')
    return base64.b64encode(data)

def base64decode(data):
    if sys.version_info.major >= 3 and isinstance(data, str):
        data = data.encode('utf-8')
    result = base64.b64decode(data)
    if sys.version_info.major >= 3:
        try:
            return result.decode('utf-8')
        except UnicodeDecodeError:
            return result
    return result

def chunkit(seq, n):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

def md5(data):
    if sys.version_info.major >= 3 and isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()
