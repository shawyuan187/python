import time
import mcu

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"ip={wi.ip}")
mqtt_client = mcu.MQTT(
    "lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)


mqtt_client.connect()

while True:
    msg = input("enter:")
    mqtt_client.publish("lol", msg)
    time.sleep(0.1)
