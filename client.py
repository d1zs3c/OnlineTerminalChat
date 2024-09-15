import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

HOST = 'parameter1'
PORT = 12345
KEY = b'string32bits_thisisanexample'

class ClientGUI:
    def __init__(self, master, client_socket):
        self.master = master
        self.client_socket = client_socket
        self.master.configure(bg='black')
        self.master.title("MultiUserChat")
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', bg='black', fg='green', font=('Courier', 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.msg_entry = tk.Entry(master, bg='black', fg='green', font=('Courier', 12))
        self.msg_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_message)
        
        self.password = simpledialog.askstring("Password", "Type the server password:", parent=self.master, show="*")
        if not self.password:
            messagebox.showerror("Error", "Password required.")
            master.destroy()
            return

        self.username = simpledialog.askstring("Username", "Type your User:", parent=self.master)
        if not self.username:
            messagebox.showerror("Error", "Username required.")
            master.destroy()
            return
        self.display_message(f"whoami:{self.username}")
        self.authenticate_password()
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def authenticate_password(self):
        try:
            encrypted_password = self.encrypt_message(self.password)
            self.client_socket.send(encrypted_password)
            response = self.client_socket.recv(1024)
            response_message = self.decrypt_message(response)

            if response_message != "Password accepted.":
                messagebox.showerror("Error", response_message)
                self.master.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error during authentication: {e}")
            self.master.destroy()

    def encrypt_message(self, message):
        aesgcm = AESGCM(KEY)
        nonce = os.urandom(12)
        encrypted_message = aesgcm.encrypt(nonce, message.encode('utf-8'), None)
        return nonce + encrypted_message

    def decrypt_message(self, encrypted_message):
        aesgcm = AESGCM(KEY)
        nonce = encrypted_message[:12]
        ciphertext = encrypted_message[12:]
        return aesgcm.decrypt(nonce, ciphertext, None).decode('utf-8')

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            full_message = f"{self.username} -> {message}"
            try:
                encrypted_message = self.encrypt_message(full_message)
                self.client_socket.send(encrypted_message)
                self.display_message(full_message)
                self.msg_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Message can't be sent: {e}")

    def receive_messages(self):
        while True:
            try:
                encrypted_message = self.client_socket.recv(1024)
                if encrypted_message:
                    message = self.decrypt_message(encrypted_message)
                    self.display_message(message)
                else:
                    self.display_message("Connection closed.")
                    break
            except:
                self.display_message("Connection error.")
                break
    def receive_messages(self):
        while True:
            try:
                encrypted_message = self.client_socket.recv(1024)
                if encrypted_message:
                    message = self.decrypt_message(encrypted_message)
                
                # Ignorar mensajes "ping"
                    if message == "ping":
                        continue
                
                    self.display_message(message)
                else:
                    self.display_message("Connection closed.")
                    break
            except:
                self.display_message("Connection error.")
                break
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except Exception as e:
        messagebox.showerror("Error", f"Error connecting to the server: {e}")
        return

    root = tk.Tk()
    gui = ClientGUI(root, client_socket)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, client_socket))
    root.mainloop()

def on_closing(root, client_socket):
    try:
        client_socket.close()
    except:
        pass
    root.destroy()

if __name__ == "__main__":
    main()
