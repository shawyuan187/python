from machine import Pin
import time
import mcu

gpio = mcu.gpio()
eq = Pin(gpio.D3, Pin.IN)
while True:
    print(eq.value())
    if eq.value() == 1:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(0.5)
