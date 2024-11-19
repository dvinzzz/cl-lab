import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server started, waiting for a connection...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Receive message from the client
    client_message = conn.recv(1024).decode()
    print(f"Message from client: {client_message}")
    
    # Modify the message
    modified_message = client_message + " - Message has been modified by the server."
    
    # Send the modified message back to the client
    conn.sendall(modified_message.encode())
    print(f"Modified message sent back to client: {modified_message}")
    conn.close()

if __name__ == "__main__":
    start_server()
