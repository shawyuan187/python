from machine import Pin, PWM
from time import sleep

frequency = 1000
dutyc = 0
led = PWM(Pin(2), freq=frequency, duty=dutyc)
i = 0
while True:
    while i != 1023:
        i += 1
        led.duty(i)
        sleep(0.005)
    while i != 0:
        i -= 1
        led.duty(i)
        sleep(0.005)
