from machine import Pin, ADC, PWM
from time import sleep
import mcu

frequency = 1000
dutyc = 0
delay = 0.002
gpio = mcu.gpio()
light_sensor = ADC(0)

r = Pin(gpio.D5, Pin.OUT)
g = Pin(gpio.D6, Pin.OUT)
b = Pin(gpio.D7, Pin.OUT)

r = PWM(Pin(gpio.D5), freq=frequency, duty=dutyc)
g = PWM(Pin(gpio.D6), freq=frequency, duty=dutyc)
b = PWM(Pin(gpio.D7), freq=frequency, duty=dutyc)

while True:
    dutyc = light_sensor.read()
    print(dutyc)
    sleep(0.5)
    if dutyc < 400:
        dutyc = 0
    r.duty(dutyc)
    g.duty(dutyc)
    b.duty(dutyc)
