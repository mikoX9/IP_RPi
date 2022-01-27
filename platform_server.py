import socket
import threading
from time import sleep
import state_machine # to acces curr_state
from state_machine import *
from mobile_control import encoder_states

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
    sending_thread = threading.Thread(target=send_encoders_values, args=(conn,addr))
    sending_thread.start()

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



def send_encoders_values(conn, addr):
    prev_encoder_states = [0,0]
    while True:
        if prev_encoder_states != encoder_states: #not encoder_states == [0,0]:
            curr_encoder_states = [prev_encoder_states[0]- encoder_states[0],prev_encoder_states[1]- encoder_states[1]]
            print(f"ENC state: {curr_encoder_states}")
            msg = str(curr_encoder_states).encode(FORMAT)
            print(f"Sending {msg}")
            conn.send(msg)
            prev_encoder_states = encoder_states.copy()
            sleep(0.1) # tu zmienic 






if __name__ == "__main__":
    print("STARTING")
    thread_start = threading.Thread(target=start)
    thread_start.start()