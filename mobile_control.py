from gpiozero import RotaryEncoder
from time import sleep

rotor = RotaryEncoder(2,3)


while True:
    print(f"{rotor.steps}")
    sleep(1)
