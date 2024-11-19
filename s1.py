import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server started, waiting for a connection...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    print(f"Message from client: {conn.recv(1024).decode()}")
    conn.close()

if __name__ == "__main__":
    start_server()
