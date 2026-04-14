import socket
import threading
from database import connect_db, save_message, load_messages

HOST = '127.0.0.1'
PORT = 8000

conn, cursor = connect_db()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}

def broadcast(sender_client, message):
    for client in clients:
        if client != sender_client:
            client.send(message.encode())

def handle(client):
    name = clients[client]

    while True:
        try:
            msg = client.recv(1024).decode()

            save_message(cursor, conn, name, msg)
            broadcast(client, f"{name}:{msg}")

        except:
            client.close()
            del clients[client]
            break

def send_old_messages(client):
    for sender, msg in load_messages(cursor):
        client.send(f"{sender}:{msg}".encode())

print("Server running...")

while True:
    client, _ = server.accept()
    name = client.recv(1024).decode()

    clients[client] = name
    print(name, "connected")

    send_old_messages(client)

    threading.Thread(target=handle, args=(client,), daemon=True).start()