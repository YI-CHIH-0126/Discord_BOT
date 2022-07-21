import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='~',intents=intents) #建置BOT，並傳入前綴的參數

@bot.event
async def on_ready(): #協成函式
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(999708638660792321)
    await channel.send(f'{member} join') #在頻道傳送訊息


@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(999708638660792321)
    await channel.send(f'{member} leave')



bot.run("") #傳入bot 的token