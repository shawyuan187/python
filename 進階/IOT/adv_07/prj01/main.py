from umqtt.simple import MQTTClient
import sys
import time
import mcu


def on_message(topic, msg):
    msg = msg.decode("utf_8")
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
while True:
    mqc0.check_msg()
    mqc0.ping()
    time.sleep(0.1)
