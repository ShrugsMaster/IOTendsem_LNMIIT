import socket
import threading
HOST = '127.0.0.1'
PORT = 5000
clients = []

lock = threading.Lock()

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    client.close()
                    clients.remove(client)

def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        try:
            message = client_socket.recv(1024)

            if not message:
                break
            print(f"[{address}] {message.decode()}")
            broadcast(message, client_socket)

        except:
            break

    with lock:
        if client_socket in clients:
            clients.remove(client_socket)

    client_socket.close()
    print(f"[DISCONNECTED] {address} disconnected.")
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        with lock:
            clients.append(client_socket)
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )

        thread.start()
start_server()