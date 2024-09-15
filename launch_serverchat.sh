#!/bin/bash

echo -e "Welcome to the OnlineMultiUserChat\n";

gnome-terminal -- bash -c "/home/kali/Documents/ngrok tcp 12345; exec bash"

python3 server.py
