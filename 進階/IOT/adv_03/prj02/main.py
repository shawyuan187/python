from machine import Pin, PWM
from time import sleep
from machine import Pin
import mcu as mcu

frequency = 1000
dutyc = 0
delay = 0.002
gpio = mcu.gpio()
r = PWM(Pin(gpio.D5), freq=frequency, duty=dutyc)
g = PWM(Pin(gpio.D6), freq=frequency, duty=dutyc)
b = PWM(Pin(gpio.D7), freq=frequency, duty=dutyc)

while True:
    for d in range(1023, -1, -1):
        r.duty(d)
        g.duty(1023 - d)
        sleep(delay)
    for d in range(1023, -1, -1):
        g.duty(d)
        b.duty(1023 - d)
        sleep(delay)
    for d in range(1023, -1, -1):
        b.duty(d)
        r.duty(1023 - d)
        sleep(delay)
