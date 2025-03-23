# -*- coding: utf-8 -*-
# ============================================================
# Script Name : bot.py
# Author      : d1zs3c
# Date        : 2025-03-23
# Version     : 3.0
# Description : With this script the server will be always online.
# ============================================================

import socket
import threading
import time
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

HOST = '4.tcp.eu.ngrok.io'
PORT = 10947                
KEY = b'11010110011100011001010101101100'
PASSWORD = "password"
USERNAME = "[bot]"

def encrypt_message(message):
    aesgcm = AESGCM(KEY)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, message.encode('utf-8'), None)
    return nonce + encrypted

def decrypt_message(encrypted_message):
    if len(encrypted_message) < 12:
        raise ValueError("Encrypted message too short for nonce.")
    aesgcm = AESGCM(KEY)
    nonce = encrypted_message[:12]
    ciphertext = encrypted_message[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode('utf-8')

def send_periodic_messages(sock):
    while True:
        try:
            msg = f"{USERNAME} ----------OK----------"
            encrypted = encrypt_message(msg)
            sock.send(encrypted)
            print(f"[Sent] {msg}")
        except Exception as e:
            print(f"[Error] Could not send message: {e}")
            break
        time.sleep(240) #4 min

def listen_to_server(sock):
    while True:
        try:
            encrypted = sock.recv(1024)
            if encrypted:
                try:
                    msg = decrypt_message(encrypted)
                    print(f"[Server] {msg}")
                except Exception as e:
                    print(f"[Decrypt Error] {e}")
            else:
                print("[Disconnected] Server closed connection.")
                break
        except Exception as e:
            print(f"[Error] Connection lost: {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"[OK] Connected to {HOST}:{PORT}")
    except Exception as e:
        print(f"[Error] Can't connect to server: {e}")
        return

    try:
        encrypted_password = encrypt_message(PASSWORD)
        client_socket.send(encrypted_password)
        response = client_socket.recv(1024)
        message = decrypt_message(response)
        if message != "Password accepted.":
            print(f"[Error] Auth failed: {message}")
            return
        else:
            print("[OK] Authenticated successfully.")
    except Exception as e:
        print(f"[Error] During authentication: {e}")
        return

    threading.Thread(target=send_periodic_messages, args=(client_socket,), daemon=True).start()
    listen_to_server(client_socket)

if __name__ == "__main__":
    main()
