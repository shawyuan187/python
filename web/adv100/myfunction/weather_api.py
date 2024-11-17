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

    def get_current_weather(self, city_name):
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
                title=f"{city}",
                description=f"氣溫：{current_temperature}{unit_symbol}\n氣壓：{weather_info['main']['pressure']}hPa\n風力：{weather_info['wind']['speed']}m/s\n風向：{weather_info['wind']['deg']}°",
                color=0x00FFFF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="最高溫度",
                value=f"{current_weather}{unit_symbol}",
                inline=False,
            )
            return embed
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
                embed = discord.Embed(
                    title=f"{city} {dt_txt}",
                    description=f"{description}",
                    color=0x00FFFF,
                )
                embed.set_thumbnail(url=icon_url)
                embed.add_field(
                    name="溫度",
                    value=f"{temp}{unit_symbol}",
                    inline=False,
                )
                embeds.append(embed)
            return embeds

    async def analyze_weather(self, city_name, forecast_data, open_client: openai):
        try:
            response = open_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "你是一位專業的氣象分析師，為使用者提供詳細的天氣分析和建議",
                    },
                    {
                        "role": "user",
                        "content": f"以下是 {city_name}的未來天氣預報，請根據這些數據提供詳細的天氣分析和建議:\n{forecast_data}",
                    },
                ],
                temperature=0.2,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"該城市的天氣預報失敗: {e}")
