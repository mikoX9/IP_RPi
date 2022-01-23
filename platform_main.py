from mobile_control import platform
import server

# states
FORWARD = "forward"
BACKWARD = "backward"
STOP = "stop"

curr_state = STOP

if __name__ == "__mian__":

    platform = platform()


    while True:
    
        if curr_state == STOP:
            platform.stop()
        elif curr_state == FORWARD:
            platform.set_speed(r=0.5,l=0.5)
            platform.forward()

        elif curr_state == FORWARD:
            platform.set_speed(r=0.5,l=0.5)
            platform.backward()

        else:
            print("ERROR")
