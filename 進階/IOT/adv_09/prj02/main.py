import paho.mqtt.client as mqtt
import time
def on_publish(Client, userdata, mid, reason_code,properties)
    print(f'msg{mid}has publishhhhhhedddddd')
client=mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish=on_publish
client.username_pw_set('singular','Singular#1234')
client.connect('mqtt.singularinnovation-ai.com',1883,60)
client.loop_start()


while True:
    msg=input('word:')
    result= client.publish('hi', msg)
    result.wait_for_publish()
    if result.rc==mqtt.MQTT_ERR_SUCCESS:
        print(':3')
    else:
        print(':<')
    time.sleep(0.1)