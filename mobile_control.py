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

encoder_states = [0,0]


class own_motor():
    def __init__(self, A, B, PWM):
        self.in_a = LED(A)
        self.in_b = LED(B)
        self.pwm = PWMLED(PWM)

    def forward(self, prec):
        self.in_a.off()
        self.in_b.on()
        self.pwm.on()
        self.pwm.value = prec
    
    def backward(self, prec):
        self.in_a.on()
        self.in_b.off()
        self.pwm.on()
        self.pwm.value = prec

    def stop(self):
        self.in_a.on()
        self.in_b.on()
        




class platform():
    def __init__(self):
        self.l_motor = own_motor(IN1, IN2, ENA)
        self.r_motor = own_motor(IN4, IN3, ENB)

        #self.r_encoder = RotaryEncoder(R_ENC_A, R_ENC_B)
        self.l_encoder = RotaryEncoder(L_ENC_A, L_ENC_B, max_steps=1000)    

        self.l_speed = 0.0
        self.r_speed = 0.0

    def set_speed(self, r=0.0, l=0.0):
        self.l_speed = l
        self.r_speed = r

    def forward(self):
        self.l_motor.forward(self.l_speed)
        self.r_motor.forward(self.r_speed)

    def backward(self):
        self.l_motor.backward(self.l_speed)
        self.r_motor.backward(self.r_speed)

    def stop(self):
        self.l_motor.stop()
        self.r_motor.stop()

    def left(self):
        self.l_motor.backward(self.l_speed)
        self.r_motor.forward(self.r_speed)

    def right(self):
        self.l_motor.forward(self.l_speed)
        self.r_motor.backward(self.r_speed)



if __name__ == "__main__":

    platform = platform()
    platform.set_speed(r=0.5,l=0.5)
    
    while True:
        platform.forward()
        sleep(3)
        platform.stop()
        sleep(3)
        platform.backward() 
        sleep(3)
        platform.right()
        sleep(3)
        platform.left()
        sleep(3)

