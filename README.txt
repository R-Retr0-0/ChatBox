(OPEN ON FULL SCREEN)

.--------------------------------------------------------.      ChatBox is a cmd based chatting software. By default it connects to port 8080 and to your local ip (127.0.0.1), to connect
|                                                        |      to a specific host you need to change the host and port variables values, they can be found at lines 15 and 16 of the main
|  _________ .__            __ __________                |      script. Specifically you need to change the host variable value from your local ip to the one you're trying to connect to
|  \_   ___ \|  |__ _____ _/  |\______   \ _______  ___  |      and the port variable value from 8080 to the port your host is using to host the server.
|  /    \  \/|  |  \\__  \\   __\    |  _//  _ \  \/  /  |      To host a server you need to do port forwarding on the specific port you're gonna use.
|  \     \___|   Y  \/ __ \|  | |    |   (  <_> >    <   |      Port forwarding acts like a "switchboard" that receives calls from the Internet on a specific port and passes them directly
|   \______  /___|  (____  /__| |______  /\____/__/\_ \  |      to your computer, allowing others to reach you even beyond the router.
|         \/     \/     \/            \/            \/   |      Learn more about it at "https://en.wikipedia.org/wiki/Port_forwarding".
|                                                        |      To do port forwarding on a specific port you need to:
.--------------------------------------------------------.      1) open your browser and access your router panel on 192.168.1.0 or 192.168.1.1 

2) add the username and password (wich you can find behind your router (where's the wifi password as well))
3) search the section called Port Forwarding, NAT or Virtual Server and add a new rule:

# External/Internal Port: Enter the port used by your script (e.g., 5000).
# Protocol: Select TCP (standard for sockets).

After all this, if you've done everything correctly, you should be able to use that port to make other ip's around the internet connect to your ChatBox server.

ChatBox can only make 2 users connect to each other, any other user will be able to connect to the server, but will not be able to write or read any messages.

ChatBox uses a weak encryption (XOR encryption). Learn more about it at "https://www.101computing.net/xor-encryption-algorithm/".

Given the overall structure of the program, its not suggested to use it in real life scenarios, but in developing enviroments only.