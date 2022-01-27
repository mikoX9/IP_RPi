from mobile_control import platform
import state_machine # to acces curr_state
from state_machine import *
from time import sleep
import platform_server
import threading

state_machine.curr_state = STOP
# print(state_machine.curr_state)
# platform_server.change_state()
# print(state_machine.curr_state)


server_thread = threading.Thread(target=platform_server.start)
server_thread.start()




if __name__ == "__main__":

    platform = platform()

    prev_state = None

    print("Starting main!")
    while True:
        if state_machine.curr_state is not prev_state:
            if state_machine.curr_state == STOP:
                print("Platform stop")
                platform.stop()
            elif state_machine.curr_state == FORWARD:
                print("Platform forward")
                platform.set_speed(r=0.5,l=0.5)
                platform.forward()

            elif state_machine.curr_state == BACKWARD:
                print("Platform backward")
                platform.set_speed(r=0.5,l=0.5)
                platform.backward()
            elif state_machine.curr_state == RIGHT:
                print("Platform forward")
                platform.set_speed(r=0.5,l=0.5)
                platform.right()
            elif state_machine.curr_state == LEFT:
                print("Platform forward")
                platform.set_speed(r=0.5,l=0.5)
                platform.left()
            else:
                print("ERROR IN MAIN")

            prev_state = state_machine.curr_state