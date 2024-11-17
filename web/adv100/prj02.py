#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from myfunction.weather_api import weatherapi
import openai
from myfunction import TurtleSoupGame

#######################初始化#######################
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
weather_api = weatherapi(os.getenv("weather_api_key"))
openai.api_key = os.getenv("openai_api_key")
game_manager = TurtleSoupGame(openai)


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is onlineeeeeeeeeeeeeeeeee")
    await tree.sync()


@bot.event
async def on_message(message):
    channel_id = message.channel.id
    if message.author == bot.user:
        return  # 忽略自己發的消息
    if message.content == "hello":  # 回覆
        await message.channel.send("hello")  # 回覆
    elif game_manager.is_active_game(channel_id):
        user_input = message.content.strip()
        if user_input == "結束遊戲":
            game_manager.end_game(channel_id)
            await message.channel.send("遊戲結束")
        else:
            solved, response = await game_manager.process_answer(channel_id, user_input)
            if solved:
                await message.channel.send("🫵結束遊戲，我要去睡覺了")
            else:
                await message.channel.send(response)


#######################指令#######################
@tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")


@tree.command(name="turtle_soup", description="吃龜蛋")
async def turtle_soup(interaction: discord.Interaction):
    success, response = game_manager.start_game(interaction.channel.id)
    if success:
        await interaction.response.send_message(
            f"""
遊戲開始!
題目:{response}
請大家開始提問,輸入'結束遊戲'可結束遊戲
我的回應只會是[是]、[不是]或者[無可奉告]
"""
        )
    else:
        await interaction.response.send_message(response, ephemeral=True)


# 取得天氣
@tree.command(name="weather", description="取得天氣")
async def weather(
    interaction: discord.Interaction,
    city: str,
    forecast: bool = False,
    ai: bool = False,
):
    await interaction.response.defer()
    if not forecast:
        info = weather_api.get_current_weather(city)
        embed = await weather_api.get_weather_embed(city, info)
        if embed:
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"找不到**{city}**的天氣信息")
    else:
        info = weather_api.get_forecast(city)
        if "list" in info:
            if not ai:
                embeds = await weather_api.create_forecast_embeds(city, info)
                if embeds:
                    await interaction.followup.send(embeds=embeds)
            else:
                try:
                    analysis = await weather_api.analyze_weather(city, info, openai)
                    await interaction.followup.send(f"**{city}的天氣情況**\n{analysis}")
                except Exception as e:
                    await interaction.followup.send(f"eror: {e}")
        else:
            await interaction.followup.send(f"找不到**{city}**的天氣信息")


#######################啟動#######################
def main():
    bot.run(os.getenv("dc_bot_token"))


if __name__ == "__main__":
    main()  # 啟動
