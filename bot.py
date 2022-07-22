import discord
from discord.ext import commands
import json

with open("setting.json",mode="r",encoding="utf-8") as jfile: #開啟外部的json檔案
    jdata=json.load(jfile)


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='~',intents=intents) #建置BOT，並傳入前綴的參數

@bot.event
async def on_ready(): #協成函式
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'welcome {member} join') #在頻道傳送訊息


@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'{member} leave')



bot.run(jdata["TOKEN"]) #傳入bot 的token