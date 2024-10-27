#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from myfunction.myfunction import weatherapi

#######################初始化#######################
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
weather_api = weatherapi(os.getenv("weather_api_key"))


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is onlineeeeeeeeeeeeeeeeee")
    await tree.sync()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # 忽略自己發的消息
    if message.content == "hello":  # 回覆
        await message.channel.send("hello")  # 回覆


#######################指令#######################
@tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")


# 取得天氣
@tree.command(name="weather", description="取得天氣")
async def weather(interaction: discord.Interaction, city: str, forecast: bool = False):
    await interaction.response.defer()
    unit_symbol = "C" if weather_api.units == "metric" else "F"
    if not forecast:
        info = weather_api.get_weather(city)
        if "weather" in info and "main" in info:
            current_weather = info["weather"][0]["description"]
            icon_code = info["weather"][0]["icon"]
            icon_url = weather_api.get_icon_url(icon_code)
            embed = discord.Embed(
                title=f"{city} {current_weather}",
                description=f"氣溫：{info['main']['temp']}{unit_symbol}\n氣壓：{info['main']['pressure']}hPa\n風力：{info['wind']['speed']}m/s\n風向：{info['wind']['deg']}°",
                color=0x00FFFF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="最高溫度",
                value=f"{current_weather}{unit_symbol}",
                inline=False,
            )
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"找不到{city}的天氣信息")
    else:
        info = weather_api.get_forecast(city)
        if "list" in info:
            forecast_list = info["list"][:10]
            embeds = []
            for forecast in forecast_list:
                dt_txt = forecast["dt_txt"]
                temp = forecast["main"]["temp"]
                description = forecast["weather"][0]["description"]
                icon_code = forecast["weather"][0]["icon"]
                icon_url = weather_api.get_icon_url(icon_code)

                embed = discord.Embed(
                    title=f"{city} {dt_txt}",
                    description=f"氣溫：{temp}{unit_symbol}\n氣壓：{forecast['main']['pressure']}hPa\n風力：{forecast['wind']['speed']}m/s\n風向：{forecast['wind']['deg']}°",
                    color=0x00FFFF,
                )
                embed.set_thumbnail(url=icon_url)
                embed.add_field(
                    name="最高溫度",
                    value=f"{temp}{unit_symbol}",
                    inline=False,
                )
                embeds.append(embed)
                await interaction.followup.send(embeds=embeds)
            else:
                await interaction.followup.send(f"找不到{city}的天氣信息")


#######################啟動#######################
def main():
    bot.run(os.getenv("dc_bot_token"))


if __name__ == "__main__":
    main()  # 啟動
