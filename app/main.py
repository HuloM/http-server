import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept() # wait for client
    server_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")


if __name__ == "__main__":
    main()
