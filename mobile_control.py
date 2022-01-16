from gpiozero import RotaryEncoder
from time import sleep

rotor = RotaryEncoder(2, 3)


while True:
    print(f"{rotor.values}")
    sleep(1)