from dataclasses import dataclass
from app.http_status_code import HttpStatusCode
from app.http_headers import HttpHeaders


@dataclass
class HttpResponse:
    http_version: bytes
    status_code: HttpStatusCode
    body: bytes
    headers: HttpHeaders

    def __init__(self, http_version: bytes, status_code: HttpStatusCode, body: bytes, headers: HttpHeaders):
        self.http_version = http_version
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def construct_response(self) -> bytes:
        return '{http_version} {status_code}\r\n{headers}\r\n{body}'.format(http_version=self.http_version,
                                                                            status_code=self.status_code.value,
                                                                            headers=self.headers.construct_headers(),
                                                                            body=self.body).encode()
