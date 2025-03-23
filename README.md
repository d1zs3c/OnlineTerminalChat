🖥️ OnlineTerminalChat

With these scripts, you can communicate securely with anyone in the world via the terminal using end-to-end encryption. Just set an initial password and a 32-bit key to encrypt messages.
🚀 Getting Started
1. Install Dependencies

Make sure you have Python installed. Then, install the required libraries:

pip install cryptography tk

2. Configure

    Choose a password and a 32-bit key.

    Update these values in the three scripts: launch_serverchat.sh, launch_client.sh, and launch_bot.sh.

3. Set Up Ngrok

    Create a free Ngrok account.

    Connect your authtoken:

ngrok config add-authtoken YOUR_TOKEN_HERE

4. Launch the Server

./launch_serverchat.sh

This will start the chat server and open a tunnel with Ngrok.
5. Copy the Ngrok Address

Copy the IP address and port shown by Ngrok (something like 2.tcp.eu.ngrok.io 10982).
6. Launch the Client

In a new terminal:

./launch_client.sh 2.tcp.eu.ngrok.io 10982

7. (Optional) Keep the Server Alive

If you want the server to stay online even without traffic, run the bot script:

./launch_bot.sh 2.tcp.eu.ngrok.io 10982

8. Login & Chat

    Enter your password and pick a username.

    Start chatting securely from your terminal!
