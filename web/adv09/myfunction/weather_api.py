import requests
import openai
import discord


class weatherapi:
    def __init__(self, api_key, units="metric", lang="zh_tw"):
        self.api_key = api_key
        self.units = units
        self.lang = lang
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast?"
        self.icon_url = "https://openweathermap.org/img/wn/"

    def get_weather(self, city_name):
        url = f"{self.base_url}appid={self.api_key}&q={city_name}&units={self.units}&lang={self.lang}"
        response = requests.get(url)
        return response.json()

    def get_forecast(self, city_name):
        url = f"{self.forecast_url}appid={self.api_key}&q={city_name}&units={self.units}&lang={self.lang}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_icon_url(self, icon_name):
        return f"{self.icon_url}{icon_name}@2x.png"

    def get_icon(self, icon_code):
        icon_url = self.get_icon_url(icon_code)
        response = requests.get(icon_url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    async def get_weather_embed(self, city, weather_info):
        unit_symbol = "C" if self.units == "metric" else "F"
        if "weather" in weather_info and "main" in weather_info:
            current_temperature = weather_info["main"]["temp"]
            current_weather = weather_info["weather"][0]["description"]
            icon_code = weather_info["weather"][0]["icon"]
            icon_url = self.get_icon_url(icon_code)
            embed = discord.Embed(
                title=f"{city} {current_weather}",
                description=f"氣溫：{weather_info['main']['temp']}{unit_symbol}\n氣壓：{weather_info['main']['pressure']}hPa\n風力：{weather_info['wind']['speed']}m/s\n風向：{weather_info['wind']['deg']}°",
                color=0x00FFFF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="最高溫度",
                value=f"{current_weather}{unit_symbol}",
                inline=False,
            )
            return None
        return None

    async def create_forecast_embeds(self, city, forecast_info):
        unit_symbol = "C" if self.units == "metric" else "F"
        embeds = []
        if "list" in forecast_info:
            forecast_list = forecast_info["list"][:10]
            for forecast in forecast_list:
                dt_txt = forecast["dt_txt"]
                temp = forecast["main"]["temp"]
                description = forecast["weather"][0]["description"]
                icon_code = forecast["weather"][0]["icon"]
                icon_url = self.get_icon_url(icon_code)
