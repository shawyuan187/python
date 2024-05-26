from machine import Pin, PWM
import time
import mcu


def servo_angle(sg: PWM, angle: int):
    if 0 <= angle <= 180:
        sg.duty(int(1023 * (0.5 + angle / 90) / 20))


gpio = mcu.gpio()
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
servo_angle(sg_pin, 180)
time.sleep(1)
servo_angle(sg_pin, 90)
time.sleep(1)
