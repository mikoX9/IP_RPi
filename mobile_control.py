from tkinter.font import ROMAN
from gpiozero import RotaryEncoder
from gpiozero import Motor

from time import sleep

# GPIOx
ENB = 12
ENA = 13
IN1 = 21
IN2 = 20
IN3 = 26
IN4 = 19

R_ENC_A = 0
R_ENC_B = 0

L_ENC_A = 1
L_ENC_B = 7


class own_motor():
    def __init__(self):
        pass


def platform_init():

    r_encoder = RotaryEncoder(R_ENC_A, R_ENC_B)
    l_encoder = RotaryEncoder(L_ENC_A, L_ENC_B)    






rotor = RotaryEncoder(2, 3)


while True:
    print(f"{rotor.values}")
    sleep(1)