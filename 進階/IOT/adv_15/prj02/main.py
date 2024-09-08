#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time

import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage

print(model.invoke([HumanMessage(content="你好")]).content)


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


def on_connect(client, userdata, mid, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("lol")


def on_message(client, userdata, msg):
    print(f"my sub topic: {msg.topic}, my sub data: {msg.payload.decode('utf-8')}")
    home_config = str(msg.payload.decode("utf-8"))


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
home_config = "none"

#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
        你是一個負責開燈跟關燈負責開關車庫的門的管理員
        你只能根據使用者的回應來決定要回答'ON'或'OFF'或'close'或'open'
    
        回答的格式是'ON'或'OFF'或'close'或'open'或'home_config'
        on 代表開燈
        off 代表關燈
        close 代表關閉車庫
        open 代表開啟車庫
        'home_config'代表家裡狀態

                    """
            ),
            HumanMessage(content=ans),
        ]
    ).content

    result = client.publish("lol", msg)
    result.wait_for_publish()  # 等待發布完成
    if msg == "home_config":
        msg == model.invoke(
            [
                HumanMessage(x``
                    content="""
                你是一個負責解釋家裡狀態的小幫手，你只能回答100個字，
                感測器位置沒有問題，光感應器數值越大代表越暗，數值範圍在0~1023之間，
                有問題請解釋可能發生災難或狀況，
                家裡感測器不可能壞掉喔!，目前家裡的狀態是:
                """
                ),
                HumanMessage(content=home_config),
            ]
        ).content
        print(msg)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published")
    else:
        print("Message not published")
    time.sleep(0.1)
