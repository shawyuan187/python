#########################匯入模組#########################
from machine import Pin, I2C, ADC
import dht
import time
import mcu
import json
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()  # 建立gpio物件
wi = mcu.wifi("SingularClass", "Singular#1234")  # 建立wifi物件
wi.setup(ap_active=False, sta_active=True)  # 設定wifi模式
if wi.connect():
    print(f"IP={wi.ip}")  # 連接wifi

# 連接MQTT
mqtt_client = mcu.MQTT(
    "lol", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("lol_AI", on_message)
m = "no message"

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))  # 建立I2C物件
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # 建立OLED物件
d = dht.DHT11(Pin(gpio.D0, Pin.IN))  # 建立DHT11物件
msg_json = {}  # 建立字典
adc = ADC(0)  # 建立light sensor物件
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7)  # 建立LED物件
servo = mcu.servo(gpio.D8)  # 建立servo物件
#########################主程式#########################
while True:
    mqtt_client.chm()  # 檢查MQTT訊息
    light_value = adc.read()
    d.measure()  # 讀取溫溼度
    temp = d.temperature()  # 將溫溼度分別存在不同變數
    hum = d.humidity()
    oled.fill(0)  # 清除螢幕
    oled.text(f"Humidity: {hum:02d}", 0, 0)  # 顯示文字, x座標, y座標
    oled.text(f"Temperature: {temp:02d}C", 0, 10)  # 顯示文字, x座標, y座標
    oled.text(f"Light: {light_value}", 0, 20)  # 顯示文字, x座標, y座標
    oled.show()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["lightsensor"] = light_value
    msg = json.dumps(msg_json)  # 將字典轉換成JSON格式
    mqtt_client.publish("lol_home", msg)  # 發布訊息

    if "ON" in m:  # 開燈
        LED.RED.value(1)  # 燈熱
        LED.GREEN.value(1)
        LED.BLUE.value(1)
    elif "OFF" in m:  # 關燈
        LED.RED.value(0)  # 燈熱
        LED.GREEN.value(0)
        LED.BLUE.value(0)

    if "CLOSE" in m:  # 關閉車庫
        servo.angle(90)  # 設定角度
    elif "OPEN" in m:  # 開啟車庫
        servo.angle(180)  # 設定角度
    time.sleep(1)
