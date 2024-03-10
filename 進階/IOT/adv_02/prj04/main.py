from machine import Pin
from time import sleep

r = Pin(14, Pin.OUT)
g = Pin(12, Pin.OUT)
b = Pin(13, Pin.OUT)
r.value(0)
b.value(0)
g.value(0)
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
