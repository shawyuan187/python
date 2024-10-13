#######################定義常數########################
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys
from ttkbootstrap import *
from PIL import Image, ImageTk

os.chdir(sys.path[0])  # 設定工作目錄
api_key = "892da2f13edf3c7f382637760e72d224"  # 請填入你的api key
base_url = "http://api.openweathermap.org/data/2.5/forecast?"  # 基本url
units = "metric"  # 單位
lang = "zh_tw"  # 語言


#######################定義函數########################
def draw_graph():
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
            time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime("%m/%d %H")
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
    plt.close()
    image = Image.open("weather_forecast.png")
    img = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.create_image(image.width // 2, image.height // 2, image=img)
    canvas.image = img


#######################建立視窗########################
window = tk.Tk()
window.title("weather app")
######################創建畫布########################
canvas = tk.Canvas(window, width=0, height=0, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)
#######################設定字型########################
font_size = 20
window.option_add("*Font", ("Helvetica", font_size))
#######################設定主題########################
style = Style(theme="superhero")
style.configure("my.TButton", font=("Helvetica", font_size))
#######################建立變數########################
check_type = BooleanVar()
check_type.set(True)

#######################建立按鈕########################
draw_button = Button(window, text="show", command=draw_graph, style="my.TButton")
draw_button.grid(row=1, column=0, padx=10, pady=10)
#######################運行應用程式########################
window.mainloop()
