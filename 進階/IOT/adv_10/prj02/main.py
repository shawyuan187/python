import time
import mcu

from machine import ADC

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"ip={wi.ip}")
mqtt_client = mcu.MQTT(
    "lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)


mqtt_client.connect()
light_sensor = ADC(0)

while True:
    msg = str(light_sensor.read())
    mqtt_client.publish("lol", msg)
    time.sleep(0.1)
