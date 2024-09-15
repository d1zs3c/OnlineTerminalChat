import socket
import threading
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import time

HOST = '0.0.0.0'
PORT = 12345
MAX_CLIENTS = 5
KEY = b'string32bits_thisisanexample'
PASSWORD = "yourpassword"

clients = []
usernames = []
'''
def ping_clients():
    while True:
        time.sleep(30)  # Cada 30 segundos
        for client in clients:
            try:
                client.send(encrypt_message("ping"))
            except:
                remove_client(client)
'''
def encrypt_message(message):
    aesgcm = AESGCM(KEY)
    nonce = os.urandom(12)
    encrypted_message = aesgcm.encrypt(nonce, message.encode('utf-8'), None)
    return nonce + encrypted_message

def decrypt_message(encrypted_message):
    aesgcm = AESGCM(KEY)
    nonce = encrypted_message[:12]
    ciphertext = encrypted_message[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode('utf-8')

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(encrypt_message(message))
            except:
                client.close()
                remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        username = usernames[index]
        print(f"{username}-disconnect.")
        usernames.remove(username)

def handle_client(client, addr):
    print(f"New connection: {addr}")
    
    try:
        encrypted_password = client.recv(1024)
        password = decrypt_message(encrypted_password)

        if password != PASSWORD:
            client.send(encrypt_message("Invalid password. Connection refused."))
            client.close()
            return
        else:
            client.send(encrypt_message("Password accepted."))
    except:
        client.close()
        return
    
    while True:
        try:
            encrypted_message = client.recv(1024)
            if encrypted_message:
                message = decrypt_message(encrypted_message)
                print(f"New message: {message}")
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break

def receive_connections():
    server.listen()
    print(f"Server listening {HOST}:{PORT}")
    while True:
        if len(clients) < MAX_CLIENTS:
            client, addr = server.accept()
            clients.append(client)
            threading.Thread(target=handle_client, args=(client, addr)).start()
        else:
            print("Max User error(5)")
            client, addr = server.accept()
            client.send(encrypt_message("Server Full. Try later."))
            client.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    server.bind((HOST, PORT))
    #threading.Thread(target=ping_clients, daemon=True).start()
    receive_connections()
