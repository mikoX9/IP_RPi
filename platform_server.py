import socket
import threading
from time import sleep

MSG_LENGHT = 64
PORT = 5050
#SERVER = socket.gethostbyname( socket.gethostname() )
SERVER = "192.168.0.101"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg = conn.recv(MSG_LENGHT).decode(FORMAT)
        print(f"[{addr}] {msg}\n\r")   
        if msg == DISCONNECT_MESSAGE:
            connected = False
            print(f"[{addr}] {msg}")   

        sleep(1)
        
        # msg_length = conn.recv(MSG_LENGHT).decode(FORMAT)
        # if msg_length:
        #     msg_length = int(msg_length)
        #     msg = conn.recv(MSG_LENGHT).decode(FORMAT)
        #     if msg == DISCONNECT_MESSAGE:
        #         connected = False
        #     print(f"[{addr}] {msg}")   
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")



if __name__ == "__main__":
    print("STARTING")
    start()
