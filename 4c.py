import socket

def request_sum():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Request sent for sum of integers from 1 to 10.")

    # Receive sabotaged sum
    result = client_socket.recv(1024).decode()
    print(f"Received result (sabotaged): {result}")
    client_socket.close()

if __name__ == "__main__":
    request_sum()
