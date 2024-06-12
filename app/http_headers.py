from dataclasses import dataclass
from enum import Enum

@dataclass
class HttpHeaders:
    accept: str
    accept_charset: str
    accept_encoding: str
    accept_language: str
    authorization: str
    cache_control: str
    content_length: str
    content_type: str
    cookie: str
    host: str
    if_modified_since: str
    pragma: str

    def __init__(self, headers: dict):
        self.headers = headers

    def construct_headers(self):
        byte_str = ''
        for k, v in self.headers.items():
            if v is not None:
                byte_str += f'{k}: {v}\r\n'
        return byte_str.encode()


class HttpHeaderObject(Enum):
    accept            = "Accept"
    accept_charset    = "Accept-Charset"
    accept_encoding   = "Accept-Encoding"
    accept_language   = "Accept-Language"
    authorization     = "Authorization"
    cache_control     = "Cache-Control"
    content_length    = "Content-Length"
    content_type      = "Content-Type"
    cookie            = "Cookie"
    host              = "Host"
    if_modified_since = "If-Modified-Since"
    pragma            = "Pragma"