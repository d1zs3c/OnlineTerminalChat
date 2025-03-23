# OnlineTerminalChat
Using these scripts you will be able to communicate with anyone in the world via a terminal in an encrypted way. Set up an initial password and a 32-bit key to encrypt the message when sending it.

Yo need to execute firts the script "launch_serverchat.sh" and in another terminal the script "launch_client.sh" with two parameters (the ip and port provided to you by ngrok). If you need the server online without traffic, you need to launch the bot.py; this script act like a client and send a message each 4 minutes. Have fun :)

Steps:

1. Download all the libraries (cryptography, tk).
2. Choose the password and 32bits key (change it in the 3 scripts).
3. Configure ngrok (it's free) with your mail and your token.
4. Execute launch_serverchat.sh.
5. Copy the ip-address and port provided by ngrok.
6. Execute launch_client.py with the two parametres (ip, port).
7. If you need keep alive the conection, launch the script launch_bot.sh.
8. Login with the password, type a username.
9. Have fun x2 :)




![image](https://github.com/user-attachments/assets/a477a0f2-e2ca-4ebc-adf3-d92ee017f936)
