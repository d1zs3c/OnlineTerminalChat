🖥️ OnlineTerminalChat

Using these scripts, you can communicate with anyone in the world via a terminal in an encrypted way. Set an initial password and a 32-bit key to encrypt the messages.


🚀 Steps
    Download the required libraries:
    
    pip install cryptography tk

Choose a password and a 32-bit key, edit the following scripts and set your values:

    launch_serverchat.sh

    launch_client.sh

    launch_bot.sh

Create account and install ngrok (it's free):
    
    sudo apt install ngrok

Add your auth token:

    ngrok config add-authtoken YOUR_TOKEN_HERE

Run the server:

    ./launch_serverchat.sh

Copy the IP and port provided by ngrok, for example:

    2.tcp.eu.ngrok.io 10982

Run the client in another terminal:

    ./launch_client.sh 2.tcp.eu.ngrok.io 10982

(Optional) Keep the connection alive with the bot:

    ./launch_bot.sh 2.tcp.eu.ngrok.io 10982

Login and have fun!!
