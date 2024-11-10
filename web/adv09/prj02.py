#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from adv09.myfunction.weather_api import weatherapi
import openai

#######################初始化#######################
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
weather_api = weatherapi(os.getenv("weather_api_key"))
openai.api_key = os.getenv("openai_api_key")


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is onlineeeeeeeeeeeeeeeeee")
    await tree.sync()


# 頻道違建key,遊戲狀態為value,這是一個痊癒變數,所有指令都可以讀取
# 如果把字典當作痊癒變數就不需要宣告global就可以直鳩修改字典裡的值
channel_games = {}


@bot.event
async def on_message(message):
    channel_id = message.channel.id
    if message.author == bot.user:
        return  # 忽略自己發的消息
    if message.content == "hello":  # 回覆
        await message.channel.send("hello")  # 回覆
    elif channel_id in channel_games:
        user_input = message.content.strip()
        if user_input == "結束遊戲":
            channel_games.pop(channel_id)
            await message.channel.send("遊戲結束")
        else:
            game_data = channel_games[channel_id]["game_data"]
            print(user_input)
            if "history" not in channel_games[channel_id]:
                channel_games[channel_id]["history"] = []

            history = channel_games[channel_id]["history"]
            history.append({"role": "user", "content": user_input})
            messages = (
                [
                    {
                        "role": "system",
                        "content": f"""
你是這個遊戲的主持人，你會回答我的問題。
題目:{channel_games[channel_id]['game_data']['question']}
請大家開始提問,輸入'結束遊戲'可結束遊戲
我的回應只會是[是]、[不是]或者[無可奉告]，不會回答其他內容
當玩家要求提示的時候，你可以提供'關鍵字'當作提示。
謎題:{game_data['question']}
解答:{game_data['answer']}""",
                    },
                ]
                + history
            )
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=0.5,
                )
                answer = response.choices[0].message.content
                if answer == "恭喜答對!":
                    game_data["solved"] = True
                    await message.channel.send("🫵結束遊戲，我要去睡覺了")
                    channel_games.pop(channel_id)
                else:
                    history.append({"role": "assistant", "content": answer})
                    channel_games[channel_id]["history"] = history
                    await message.channel.send(answer)  # debug
                    print(messages)
            except Exception as e:
                await message.channel.send(f"eror: {e}")


#######################指令#######################
@tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")


@tree.command(name="turtle_soup", description="吃龜蛋")
async def turtle_soup(interaction: discord.Interaction):
    channel_id = interaction.channel.id
    if channel_id in channel_games:
        await interaction.response.send_message("正在游戏中，请勿重复发起游戏looool")
    else:  # 如果没有在游戏中
        channel_games[channel_id] = {
            "game_data": {
                "question": "一位女士每天早上都會去檢查家門口的郵箱，但郵箱裡從來沒有信。日復一日，她依然堅持這個習慣，從不間斷。某天，她終於在郵箱中發現了一封信。看完信後，她立刻決定搬離這個城市，甚至連夜離開，神情緊張而驚慌。",
                "answer": "這位女士過去曾牽涉到一件敏感事件，並改名換姓遠走他鄉，希望徹底擺脫過去的陰影。這封信中揭露了她的真實身份，並暗示她的過去可能已被人發現。信的內容讓她意識到，無論她逃到哪裡，那段過去都始終在追隨著她。為了躲避未知的威脅，她不得不再次搬離。",
                "solved": False,
            },
            "history": [],
        }
        await interaction.response.send_message(
            f"""
遊戲開始!
題目:{channel_games[channel_id]['game_data']['question']}
請大家開始提問,輸入'結束遊戲'可結束遊戲
我的回應只會是[是]、[不是]或者[無可奉告]，不會回答其他內容
        """
        )


# 取得天氣
@tree.command(name="weather", description="取得天氣")
async def weather(
    interaction: discord.Interaction,
    city: str,
    forecast: bool = False,
    ai: bool = False,
):
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
            if not ai:
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
            else:
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {
                                "role": "system",
                                "content": "你是一位專業的氣象分析師，為使用者提供詳細的天氣資訊。",
                            },
                            {
                                "role": "user",
                                "content": f"以下是{city}的天氣情況，請根據這些數據回答我的問題。\n{info}",
                            },
                        ],
                        temperature=0.2,
                    )
                    analysis = response.choices[0].message.content
                    await interaction.followup.send(f"**{city}的天氣情況**\n{analysis}")
                except Exception as e:
                    await interaction.followup.send(f"eror: {e}")


#######################啟動#######################
def main():
    bot.run(os.getenv("dc_bot_token"))


if __name__ == "__main__":
    main()  # 啟動
