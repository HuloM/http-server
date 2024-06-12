import socket
from app.http_response import HttpResponse
from app.http_status_code import HttpStatusCode
from app.http_headers import HttpHeaders
import threading


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        t = threading.Thread(target=lambda: request_handler(conn))
        t.start()


def request_handler(conn):
    buff = conn.recv(1024).decode("utf-8")

    split = buff.split("\r\n")

    req_path = split[0].split(" ")[1]

    if req_path == "/":
        conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '\r\n', HttpHeaders({})).construct_response())
    elif req_path.startswith("/echo"):
        req_body = req_path[1:].split("/")[1]

        conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '{body}'.format(body=req_body),
                               HttpHeaders({'content_type': 'text/plain', 'content_length': len(req_body)}))
                  .construct_response())
    elif req_path == "/user-agent":
        user_agent = [s for s in split if "User-Agent" in s][0].split(" ")[1]

        conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '{body}'.format(body=user_agent),
                               HttpHeaders({'content_type': 'text/plain', 'content_length': len(user_agent)}))
                  .construct_response())
    elif req_path.startswith("/files"):
        file_path = req_path[1:].split("/")[1]
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '{body}'.format(body=file_content),
                                       HttpHeaders({'content_type': 'application/octet-stream', 'content_length': len(file_content)}))
                          .construct_response())
        except FileNotFoundError:
            conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
    else:
        conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
