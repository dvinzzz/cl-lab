import socket
from Crypto.Cipher import DES

key = b'8bytekey'  # DES key must be exactly 8 bytes
cipher = DES.new(key, DES.MODE_ECB)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server listening...")

client_socket, addr = server.accept()
print(f"Connected by {addr}") 

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    decrypted_message = cipher.decrypt(data).decode().strip()
    print(f"Decrypted message: {decrypted_message}")

client_socket.close()
server.close()