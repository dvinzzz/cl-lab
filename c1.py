import socket

def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    client_socket.sendall("Mid exams are from next Monday".encode())
    print("Message sent.")
    client_socket.close()

if __name__ == "__main__":
    send_message()
