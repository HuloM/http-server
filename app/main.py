import socket
from app.http_response import HttpResponse
from app.http_status_code import HttpStatusCode
from app.http_headers import HttpHeaders


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()  # wait for client
        buff = conn.recv(1024).decode("utf-8")

        split = buff.split(" ")
        req_path = split[1]
        print(split)
        if req_path == "/":
            conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '\r\n', HttpHeaders({})).construct_response())
        elif req_path.startswith("/echo"):
            req_body = req_path[1:].split("/")[1]
            print(req_body)
            conn.send(HttpResponse('HTTP/1.1', HttpStatusCode.OK, '{body}'.format(body=req_body),
                                   HttpHeaders({'content_type': 'text/plain', 'content_length': len(req_body)}))
                      .construct_response())
        else:
            conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
