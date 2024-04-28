from umqtt.simple import MQTTClient
from machine import Pin, ADC
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
if wi.connect():
    print(f"ip={wi.ip}")
mqtt = mcu.MQTT("lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")


mqtt.connect()

mqtt.subscribe("lol", on_message)
gpio = mcu.gpio()
lis = ADC(0)
led = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
led.RED.value(0)
led.GREEN.value(0)
led.BLUE.value(0)
ls = ADC(0)
while True:
    mqtt.chm()
    lsr = lis.read()

    if m == "on":
        led.RED.value(1)
        led.GREEN.value(1)
        led.BLUE.value(1)
    elif m == "off":

        led.RED.value(0)
        led.GREEN.value(0)
        led.BLUE.value(0)
    elif m == "auto":
        if lsr > 700:

            led.RED.value(1)
            led.GREEN.value(1)
            led.BLUE.value(1)
        else:
            led.RED.value(0)
            led.GREEN.value(0)
            led.BLUE.value(0)
    time.sleep(0.1)
