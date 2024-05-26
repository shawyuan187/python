import time
import mcu
from umqtt.simple import MQTTClient
from machine import Pin, I2C
import ssd1306

gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
m = "0"


#######################################################################################################
# oled.text("hi", 0, 0)
# oled.text("world", 0, 10)
# oled.show()
def on_message(topic, msg):
    global m
    msg = msg.decode("utf_8")
    m = msg
    topic = topic.decode("utf-8")
    oled.text(topic, 0, 20)
    oled.text(msg, 0, 30)

    print(f"my sub topic:{topic},msg:{msg}")


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"ip={wi.ip}")
    oled.text(f"ip={wi.ip}", 0, 0)

mqtt = mcu.MQTT("lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
mqtt.connect()
mqtt.subscribe("lol", on_message)

while True:
    mqtt.chm()
    oled.show()
    servo.angle(int(m))
    time.sleep(0.1)
