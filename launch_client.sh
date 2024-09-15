#!/bin/bash

echo -e "Welcome to the OnlineMultiUserChat\n"

if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <nuevo_host> <nuevo_puerto>"
    exit 1
fi

host=$1
port=$2

sed -i "s/HOST = '.*'/HOST = '${host}'/" client.py
sed -i "s/PORT = [0-9]*/PORT = ${port}/" client.py

python3 client.py
