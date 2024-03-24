#########################匯入模組#########################
from machine import Pin
from time import sleep
import adv_03.mcu as mcu

#########################函式與類別定義#########################
gpio = mcu.gpio()
r = Pin(gpio.D5, Pin.OUT)
g = Pin(gpio.D6, Pin.OUT)
b = Pin(gpio.D7, Pin.OUT)

#########################宣告與設定#########################

#########################主程式#########################
while True:
    r.value(1)
    b.value(0)
    g.value(0)
    sleep(1)
    r.value(0)
    b.value(0)
    g.value(1)
    sleep(1)
    r.value(1)
    b.value(0)
    g.value(1)
    sleep(1)
