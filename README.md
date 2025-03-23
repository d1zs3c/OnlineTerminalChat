🖥️ OnlineTerminalChat

Using these scripts, you can communicate with anyone in the world via a terminal in an encrypted way. Set an initial password and a 32-bit key to encrypt the messages.


🚀 Steps:

a) Download the required libraries:
    
    pip install cryptography tk

b) Choose a password and a 32-bit key, edit the following scripts and set your values:

    launch_serverchat.sh

    launch_client.sh

    launch_bot.sh

c) Create account and install ngrok (it's free):
    
    sudo apt install ngrok

d) Add your auth token:

    ngrok config add-authtoken YOUR_TOKEN_HERE

e) Run the server:

    ./launch_serverchat.sh

f) Copy the IP and port provided by ngrok, for example:

    2.tcp.eu.ngrok.io 10982

g) Run the client in another terminal:

    ./launch_client.sh 2.tcp.eu.ngrok.io 10982

h) (Optional) Keep the connection alive with the bot:

    ./launch_bot.sh 2.tcp.eu.ngrok.io 10982

Login and have fun!!
