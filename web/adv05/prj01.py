#######################定義常數########################
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys

os.chdir(sys.path[0])  # 設定工作目錄
api_key = "892da2f13edf3c7f382637760e72d224"  # 請填入你的api key
base_url = "http://api.openweathermap.org/data/2.5/forecast?"  # 基本url
units = "metric"  # 單位
lang = "zh_tw"  # 語言
#######################主程式########################
city_name = "Taipei"
send_url = f"{base_url}q={city_name}&appid={api_key}&units={units}&lang={lang}"
print(f"發送的url是：{send_url}")
response = requests.get(send_url)
response.raise_for_status()
info = response.json()
xlist = []
ylist = []
if "city" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        time = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime(
            "%m/%d %H"
        )
        xlist.append(time)
        ylist.append(temp)
        print(f"{dt_txt}-{temp}°度")
        weather_description = forecast["weather"][0]["description"]
        print(f"{dt_txt}-{temp}°度，天氣狀況:{weather_description}")
else:
    print("未知")
#######################繪圖########################
font = FontProperties(fname="LXGWWenKaiMonoTC-Regular.ttf", size=14)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(xlist, ylist)
ax.set_title(f"{city_name}天氣預報", fontproperties=font)
ax.set_xlabel("時間", fontproperties=font)
plt.xticks(rotation=45)
plt.tight_layout()
fig.savefig("weather_forecast.png")
plt.show()
