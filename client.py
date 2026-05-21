import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\nMessage:", message)

        except:
            print("Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        message = input()

        try:
            client.send(message.encode())

        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()