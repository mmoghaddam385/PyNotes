import util.constants as consts

import base64

# convert from bytes to base64 string
def bytes_to_b64string(to_decode):
    return base64.urlsafe_b64encode(to_decode).decode(consts.STANDARD_ENCODING)

# convert from string to bytes
def string_to_bytes(to_encode):
    return to_encode.encode(consts.STANDARD_ENCODING)

def encoded_string_to_bytes(to_encode):
    return base64.urlsafe_b64decode(string_to_bytes(to_encode))