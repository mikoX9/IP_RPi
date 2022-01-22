from gpiozero import RotaryEncoder
from gpiozero import PWMLED
from gpiozero import LED

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
    def __init__(self, A, B, PWM):
        self.in_a = LED(A)
        self.in_b = LED(B)
        self.pwm = PWMLED(PWM)

    def forward(self, prec):
        self.in_a.on()
        self.in_b.on()
        self.pwm.value(prec)
    

class platform():
    def __init__(self):
        pass

    r_encoder = None
    l_encoder = None


    def platform_init(self):
        self.r_encoder = RotaryEncoder(R_ENC_A, R_ENC_B)
        self.l_encoder = RotaryEncoder(L_ENC_A, L_ENC_B)    






# rotor = RotaryEncoder(2, 3)

r_motor = own_motor(IN1, IN2, ENA)

while True:
    # print(f"{rotor.steps}")
    # sleep(1)
    r_motor.forward(1.0)
    sleep(1)



