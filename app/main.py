import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        conn, addr = server_socket.accept() # wait for client
        buff = conn.recv(1024).decode("utf-8")

        print(buff)

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        # conn.close()


if __name__ == "__main__":
    main()
