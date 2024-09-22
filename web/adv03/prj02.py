import requests
import os
import sys

############################################定義常數##########################################
api_key = "892da2f13edf3c7f382637760e72d224"  # 請填入你的api key
base_url = "https://api.openweathermap.org/data/2.5/weather?"  # 基本url
units = "metric"  # 單位
lang = "zh-tw"  # 語言
icon_base_url = "https://openweathermap.org/img/wn/"  # 圖示的基本url
os.chdir(sys.path[0])  # 設定工作目錄
city = input("請輸入要查詢的城市：")
send_url = f"{base_url}appid={api_key}&q={city}&units={units}&lang={lang}"
print(f"查詢的url是：{send_url}")
response = requests.get(send_url)
info = response.json()


############################################主程式##########################################

if "weather" in info and "main" in info:
    weather_description = info["weather"][0]["description"]
    current_temperature = info["main"]["temp"]

    print(info)
    print(f"測量時間是：{info['dt']}")  # 時間是UTC時間
    print(f"測量城市是：{info['name']}")
    print(f"測量城市的溫度是：{info['main']['temp']}")
    print(f"測量城市的氣壓是：{info['main']['pressure']}")
    print(f"測量城市的氣溫是：{info['main']['humidity']}")  # 百分比
    print(f"測量城市的風速是：{info['wind']['speed']}")
    print(f"測量城市的風向是：{info['wind']['deg']}")  # 風向是度數
    print(f"describe:{info['weather'][0]['description']}")
    icon_code = info["weather"][0]["icon"]
    icon_url = f"{icon_base_url}{icon_code}@2x.png"
    print(f"icon:{icon_url}")
    icon_response = requests.get(icon_url)
    if icon_response.status_code == 200:
        with open("icon.png", "wb") as icon_file:
            icon_file.write(icon_response.content)
            print("圖片已下載")
    else:
        print("圖片下載失敗")
    icon_response = requests.get(icon_url)
