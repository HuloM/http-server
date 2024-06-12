from enum import Enum


class HttpStatusCode(Enum):
    OK                 = '200 OK'
    CREATED            = '201 CREATED'
    ACCEPTED           = '202 ACCEPTED'
    NO_CONTENT         = '204 NO CONTENT'

    BAD_REQUEST        = '400 BAD REQUEST'
    UNAUTHORIZED       = '401 UNAUTHORIZED'
    FORBIDDEN          = '403 FORBIDDEN'
    NOT_FOUND          = '404 NOT FOUND'
    METHOD_NOT_ALLOWED = '405 METHOD NOT ALLOWED'
    NOT_ACCEPTABLE     = '406 NOT ACCEPTABLE'
