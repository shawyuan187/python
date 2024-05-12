from machine import Pin, I2C, ADC
import dht
import time
import mcu
import json
import ssd1306

gpio = mcu.gpio()
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"ip={wi.ip}")
mqtt_client = mcu.MQTT(
    "lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
msg_json = {}
mqtt_client.connect()
light_sensor = ADC(0)


while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    oled.fill(0)
    oled.text(f"hum:{hum:02d}", 0, 0)
    oled.text(f"temperature:{temp:02d}c", 0, 10)
    oled.show()
    ggg = str(light_sensor.read())

    msg_json["humidity:"] = hum
    msg_json["Temperature:"] = temp
    msg_json["light_sensor_reading:"] = ggg
    msg = json.dumps(msg_json)
    mqtt_client.publish("lol", msg)

    time.sleep(1)
