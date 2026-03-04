from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit import PromptSession
from colorama import Fore, Style, init
from datetime import datetime
import threading
import platform
import random
import socket
import time
import sys
import os

server = '0.0.0.0'
host = '127.0.0.1'
port = 8080
addr = (host, port)
client = None

init(autoreset=True)

ascii_art_list = [r"""
_________ .__            __ __________              
\_   ___ \|  |__ _____ _/  |\______   \ _______  ___
/    \  \/|  |  \\__  \\   __\    |  _//  _ \  \/  /
\     \___|   Y  \/ __ \|  | |    |   (  <_> >    < 
 \______  /___|  (____  /__| |______  /\____/__/\_ \
        \/     \/     \/            \/            \/
""",
                  
r"""
  /$$$$$$  /$$                   /$$     /$$$$$$$                     
 /$$__  $$| $$                  | $$    | $$__  $$                    
| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$  | $$  \ $$  /$$$$$$  /$$   /$$
| $$      | $$__  $$ |____  $$|_  $$_/  | $$$$$$$  /$$__  $$|  $$ /$$/
| $$      | $$  \ $$  /$$$$$$$  | $$    | $$__  $$| $$  \ $$ \  $$$$/ 
| $$    $$| $$  | $$ /$$__  $$  | $$ /$$| $$  \ $$| $$  | $$  >$$  $$ 
|  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/| $$$$$$$/|  $$$$$$/ /$$/\  $$
 \______/ |__/  |__/ \_______/   \___/  |_______/  \______/ |__/  \__/
""",

r"""
    __  __ __   ____  ______  ____    ___   __ __ 
   /  ]|  |  | /    ||      ||    \  /   \ |  |  |
  /  / |  |  ||  o  ||      ||  o  )|     ||  |  |
 /  /  |  _  ||     ||_|  |_||     ||  O  ||_   _|
/   \_ |  |  ||  _  |  |  |  |  O  ||     ||     |
\     ||  |  ||  |  |  |  |  |     ||     ||  |  |
 \____||__|__||__|__|  |__|  |_____| \___/ |__|__|
""",

r"""
 _______  __   __  _______  _______  _______  _______  __   __ 
|       ||  | |  ||   _   ||       ||  _    ||       ||  |_|  |
|       ||  |_|  ||  |_|  ||_     _|| |_|   ||   _   ||       |
|       ||       ||       |  |   |  |       ||  | |  ||       |
|      _||       ||       |  |   |  |  _   | |  |_|  | |     | 
|     |_ |   _   ||   _   |  |   |  | |_|   ||       ||   _   |
|_______||__| |__||__| |__|  |___|  |_______||_______||__| |__|
""",

r"""
  ______  __    __       ___   .___________..______     ______   ___   ___ 
 /      ||  |  |  |     /   \  |           ||   _  \   /  __  \  \  \ /  / 
|  ,----'|  |__|  |    /  ^  \ `---|  |----`|  |_)  | |  |  |  |  \  V  /  
|  |     |   __   |   /  /_\  \    |  |     |   _  <  |  |  |  |   >   <   
|  `----.|  |  |  |  /  _____  \   |  |     |  |_)  | |  `--'  |  /  .  \  
 \______||__|  |__| /__/     \__\  |__|     |______/   \______/  /__/ \__\ 
""",

r"""
 ________  ___  ___  ________  _________  ________  ________     ___    ___ 
|\   ____\|\  \|\  \|\   __  \|\___   ___\\   __  \|\   __  \   |\  \  /  /|
\ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_\ \  \|\ /\ \  \|\  \  \ \  \/  / /
 \ \  \    \ \   __  \ \   __  \   \ \  \ \ \   __  \ \  \\\  \  \ \    / / 
  \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ \ \  \|\  \ \  \\\  \  /     \/  
   \ \_______\ \__\ \__\ \__\ \__\   \ \__\ \ \_______\ \_______\/  /\   \  
    \|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|_______/__/ /\ __\ 
                                                                |__|/ \|__| 
""",

r"""
   █████████  █████                 █████    ███████████                      
  ███▒▒▒▒▒███▒▒███                 ▒▒███    ▒▒███▒▒▒▒▒███                     
 ███     ▒▒▒  ▒███████    ██████   ███████   ▒███    ▒███  ██████  █████ █████
▒███          ▒███▒▒███  ▒▒▒▒▒███ ▒▒▒███▒    ▒██████████  ███▒▒███▒▒███ ▒▒███ 
▒███          ▒███ ▒███   ███████   ▒███     ▒███▒▒▒▒▒███▒███ ▒███ ▒▒▒█████▒  
▒▒███     ███ ▒███ ▒███  ███▒▒███   ▒███ ███ ▒███    ▒███▒███ ▒███  ███▒▒▒███ 
 ▒▒█████████  ████ █████▒▒████████  ▒▒█████  ███████████ ▒▒██████  █████ █████
  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒ 
""",

r"""
 e88~-_  888                  d8   888~~\                    
d888   \ 888-~88e   /~~~8e  _d88__ 888   |  e88~-_  Y88b  /  
8888     888  888       88b  888   888 _/  d888   i  Y88b/   
8888     888  888  e88~-888  888   888  \  8888   |   Y88b   
Y888   / 888  888 C888  888  888   888   | Y888   '   /Y88b  
 "88_-~  888  888  "88_-888  "88_/ 888__/   "88_-~   /  Y88b 
""",

r"""
 .d8888b.  888               888    888888b.                     
d88P  Y88b 888               888    888  "88b                    
888    888 888               888    888  .88P                    
888        88888b.   8888b.  888888 8888888K.   .d88b.  888  888 
888        888 "88b     "88b 888    888  "Y88b d88""88b `Y8bd8P' 
888    888 888  888 .d888888 888    888    888 888  888   X88K   
Y88b  d88P 888  888 888  888 Y88b.  888   d88P Y88..88P .d8""8b. 
 "Y8888P"  888  888 "Y888888  "Y888 8888888P"   "Y88P"  888  888 
""",

r"""                                                       
 _______ _______ _______ _______ _______ _______ _______ 
|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |C  | | |h  | | |a  | | |t  | | |B  | | |o  | | |x  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
"""

]

session = PromptSession()

current_hour = datetime.now()
formatted_current_hour = current_hour.strftime("%H:%M:%S")

if platform.system() == "Windows":
    os.system("title ChatBox")
else:
    os.system("echo -ne '\033]0;ChatBox\007'")

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def exit_app():
    print(f"\n{Fore.RED}See you soon!{Fore.RESET}")
    time.sleep(1)
    sys.exit()

def make_log_file():
    if platform.system() == "Windows":
        os.system("type nul > error_log.txt")
    else:
        os.system("touch error_log.txt")

def write_in_error_log(e):
    with open("error_log.txt", "a") as log_file:
        log_file.write("[" + formatted_current_hour + "] " + str(e) + "\n")
    if not log_file:
        make_log_file()
        log_file.write("[" + formatted_current_hour + "] " + str(e) + "\n")

chosen_ascii = random.choice(ascii_art_list)

def ASCII():
    print(chosen_ascii)
    
def Main_menu():
    ASCII()
    print("CMD Powered Chatroom")
    print("\n[1] Start server")
    print("[2] Connect to server")
    print("[3] Exit")
    print("")
    User_Choice = input("@ChatBox> ")
    if User_Choice == "1":
        clear_terminal()
        start_server()
    elif User_Choice == "2":
        clear_terminal()
        connect()
    elif User_Choice == "3":
        exit_app()
    else:
        clear_terminal()
        Main_menu()

def start_server():
    serverpart = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverpart.bind((server, port))
        serverpart.listen()
        ASCII()
        print(f"{Fore.RED}Listening for new connections. . .{Fore.RESET}")
        conn, addr = serverpart.accept()
        print(f"{Fore.RED}There's a connection!")
        listen_thread = threading.Thread(target=listen_text, args=(conn,))
        listen_thread.start()
        send_text(conn)
        return
    except Exception as e:
        clear_terminal()
        time.sleep(3)
        start_server()

def connect():
    ASCII()
    print(f"{Fore.RED}Trying the connection. . .{Fore.RESET}")
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(addr)
        print(f"{Fore.RED}Connected!{Fore.RESET}")
        listen_thread = threading.Thread(target=listen_text, args=(client,))
        listen_thread.start()
        send_text(client)
    except Exception as e:
        while True:
            time.sleep(1)
            clear_terminal()
            connect()

def send_text(conn):
    try:
        with patch_stdout():
            nickname = session.prompt("\nNickname: ")
            enc_nickname = xor_encrypt_decrypt(nickname, 934028)
            conn.send(enc_nickname.encode())
        while True:
            message = session.prompt(nickname + "> ")
            enc_message = xor_encrypt_decrypt(message, 934028)
            conn.send(enc_message.encode())
    except Exception as e:
        write_in_error_log(e)
        input("\nAll users left or there was a problem, press ENTER to go back. . .")
        clear_terminal()
        Main_menu()

def listen_text(conn):
    try:
        with patch_stdout():
            nickname = conn.recv(1024).decode()
            decrypted_nick = xor_encrypt_decrypt(nickname, 934028)
            print_formatted_text(HTML(f'<style fg="red">{decrypted_nick}</style> has entered the chat!'))
        while True:
            with patch_stdout():
                data = conn.recv(1024).decode()
                decrypted_data = xor_encrypt_decrypt(data, 934028)
                print(f"\n" + decrypted_nick + "> " + decrypted_data)
    except Exception as e:
        write_in_error_log(e)
        input("\nAll users left or there was a problem, press ENTER to go back. . .")
        clear_terminal()
        Main_menu()

if __name__ == '__main__':
    Main_menu()
    conn = start_server()
