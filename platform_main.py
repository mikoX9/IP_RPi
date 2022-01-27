from mobile_control import platform, encoder_states
import state_machine # to acces curr_state
from state_machine import *
from time import sleep
import platform_server
import threading

state_machine.curr_state = STOP
prev_state = None

print("Starting server...")
server_thread = threading.Thread(target=platform_server.start)
server_thread.start()
print("Server started!")

def platform_steering(platform):
    global prev_state
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


def platform_encoders_check(platform):
    if platform.l_encoder.steps is not 0:
        encoder_states[0] = encoder_states[0] + platform.l_encoder.steps
        platform.l_encoder.steps = 0


if __name__ == "__main__":

    platform = platform()

    while True:
        platform_encoders_check(platform)
        print(encoder_states)
        sleep(1)
        # print(platform.l_encoder.steps)
        # platform.l_encoder.steps = 0
        # print(platform.l_encoder.steps)
        # sleep(1)




    print("Starting main!")
    while True:
        platform_steering(platform)