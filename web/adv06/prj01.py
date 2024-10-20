from ttkbootstrap import *
import sys
import os
from PIL import Image, ImageTk
import requests

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄
#######################定義常數########################
api_key = "892da2f13edf3c7f382637760e72d224"  # 請填入你的api key
base_url = "https://api.openweathermap.org/data/2.5/weather?"  # 基本url
units = "metric"  # 單位
lang = "zh-tw"  # 語言
icon_base_url = "https://openweathermap.org/img/wn/"  # 圖示的基本url
#######################定義函數########################


def get_weather_info():
    global units, current_temperature
    city_name = city_name_entry.get()
    send_url = f"{base_url}appid={api_key}&q={city_name}&units={units}&lang={lang}&appid={api_key}"
    response = requests.get(send_url)
    info = response.json()
    if "weather" in info and "main" in info:
        current_temperature = info["main"]["temp"]
        weather_description = info["weather"][0]["description"]
        icon_code = info["weather"][0]["icon"]
        icon_url = f"{icon_base_url}{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
            with open(f"{icon_code}.png", "wb") as icon_file:
                icon_file.write(icon_response.content)
        image = Image.open(f"{icon_code}.png")
        tk_image = ImageTk.PhotoImage(image)
        icon_label.config(image=tk_image)
        icon_label.image = tk_image
        temperature_label.config(
            text=f'{current_temperature}°{"c" if units == "metric" else "f"}'
        )
        description_label.config(text=weather_description)
    else:
        description_label.config(text="未知")
    image = Image.open("weather_forecast.png")
    img = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.create_image(image.width // 2, image.height // 2, image=img)
    canvas.image = img


def on_switch_change():
    global units, current_temperature
    units = "metric" if check_type.get() == True else "imperial"
    if temperature_label["text"] != "溫度：":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
        else:
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
        temperature_label.config(
            text=f'{current_temperature}°{"c" if units == "metric" else "f"}'
        )


#######################建立視窗########################
window = tk.Tk()
window.title("weather app")
#######################設定字型########################
font_size = 20
window.option_add("*Font", ("Helvetica", font_size))
canvas = tk.Canvas(window, width=0, height=0, bg="white")
canvas.grid(row=0, column=5, padx=10, pady=10)
#######################設定主題########################
style = Style(theme="superhero")
style.configure("my.TButton", font=("Helvetica", font_size))
style.configure("my.TCheckbutton", font=("Helvetica", font_size))
#######################建立變數########################
check_type = BooleanVar()
check_type.set(True)
#######################建立標籤########################
city_name_label = Label(window, text="請輸入城市名稱：")
city_name_label.grid(row=0, column=0)
icon_label = Label(window, text="圖示：")
icon_label.grid(row=1, column=0)
description_label = Label(window, text="描述：")
description_label.grid(row=1, column=2)
temperature_label = Label(window, text="溫度：")
temperature_label.grid(row=1, column=1)
#######################建立輸入框########################
city_name_entry = Entry(window)
city_name_entry.grid(row=0, column=1)
#######################建立按鈕########################

check_button = Checkbutton(
    window,
    variable=check_type,
    onvalue=True,
    offvalue=False,
    command=on_switch_change,
    style="my.TCheckbutton",
    text="溫度單位(C/F)",
)
check_button.grid(row=2, column=1, padx=10, pady=10)
buttonget = Button(window, text="get", command=get_weather_info, style="my.TButton")
buttonget.grid(row=0, column=2)
#######################運行應用程式########################
window.mainloop()
