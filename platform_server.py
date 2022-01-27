import socket
import threading
from time import sleep
import state_machine # to acces curr_state
from state_machine import *

MSG_LENGHT = 64
PORT = 5050
#SERVER = socket.gethostbyname( socket.gethostname() )
SERVER = "192.168.0.106"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"






def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg = conn.recv(MSG_LENGHT).decode(FORMAT)
        print(f"[{addr}] {msg}\n\r")   
        message_handle(msg)
        
        if msg is DISCONNECT_MESSAGE or msg is "":
            connected = False
            print(f"[{addr}] {msg}") 
            print("DISCONNECTED!")
        
        # msg_length = conn.recv(MSG_LENGHT).decode(FORMAT)
        # if msg_length:
        #     msg_length = int(msg_length)
        #     msg = conn.recv(MSG_LENGHT).decode(FORMAT)
        #     if msg == DISCONNECT_MESSAGE:
        #         connected = False
        #     print(f"[{addr}] {msg}")   
    conn.close()


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


def message_handle(msg):
    msg = msg.strip()
    print(f"Message in handle: {msg}")
    if msg == FORWARD:
        state_machine.curr_state = FORWARD
    elif msg == BACKWARD:
        state_machine.curr_state = BACKWARD
    elif msg == STOP:
        state_machine.curr_state = STOP
    elif msg == RIGHT:
        state_machine.curr_state = RIGHT
    elif msg == LEFT:
        state_machine.curr_state = LEFT
    else:
        print("ERROR IN MESSAGE_HANDLE!")

if __name__ == "__main__":
    print("STARTING")
    thread_start = threading.Thread(target=start)
    thread_start.start()