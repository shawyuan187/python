from umqtt.simple import MQTTClient
from machine import Pin, ADC
import sys
import time
import mcu

m = "off"


def on_message(topic, msg):
    global m
    msg = msg.decode("utf_8")
    m = msg
    topic = topic.decode("utf-8")

    print(f"my sub topic:{topic},msg:{msg}")


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
wi.scan()
if wi.connect():
    print(f"ip={wi.ip}")
mqs = "mqtt.singularinnovation-ai.com"
mqid = "lol"
mqn = "singular"
mqp = "Singular#1234"
mqc0 = MQTTClient(mqid, mqs, user=mqn, password=mqp, keepalive=30)
try:
    mqc0.connect()
except:
    sys.exit()
finally:
    print("connected mqs")
mqc0.set_callback(on_message)
mqc0.subscribe("shawyuan")

gpio = mcu.gpio()
lis = ADC(0)
r = Pin(gpio.D5, Pin.OUT)
g = Pin(gpio.D6, Pin.OUT)
b = Pin(gpio.D7, Pin.OUT)
r.value(0)
g.value(0)
b.value(0)
while True:
    lsr = lis.read()
    mqc0.check_msg()
    mqc0.ping()
    if m == "on":
        r.value(1)
        g.value(1)
        b.value(1)
    elif m == "off":

        r.value(0)
        g.value(0)
        b.value(0)
    elif m == "auto":
        if lsr > 700:

            r.value(1)
            g.value(1)
            b.value(1)
        else:
            r.value(0)
            g.value(0)
            b.value(0)
    time.sleep(0.1)
