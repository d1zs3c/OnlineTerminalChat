#!/bin/bash

echo -e "Activating bot...\n"

if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <nuevo_host> <nuevo_puerto>"
    exit 1
fi

host=$1
port=$2

sed -i "s/HOST = '.*'/HOST = '${host}'/" bot.py
sed -i "s/PORT = [0-9]*/PORT = ${port}/" bot.py

python3 bot.py
