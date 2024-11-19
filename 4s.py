import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server started...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Sabotaged sum calculation: computes 3 to 20
    sabotaged_sum = sum(range(3, 21))
    conn.sendall(str(sabotaged_sum).encode())
    conn.close()

if __name__ == "__main__":
    start_server()
