import socket

def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    
    # Send the original message to the server
    message = "Mid exams are from next Monday"
    client_socket.sendall(message.encode())
    print("Message sent to the server.")
    
    # Receive the modified message from the server
    modified_message = client_socket.recv(1024).decode()
    print(f"Modified message received from server: {modified_message}")
    client_socket.close()

if __name__ == "__main__":
    send_message()
