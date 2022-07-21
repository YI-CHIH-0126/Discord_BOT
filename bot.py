import discord
from discord.ext import commands


bot=commands.Bot(command_prefix='~') #建置BOT，並傳入前綴的參數

@bot.event
async def on_ready(): #協成函式
    print(">>Bot is online<<")

bot.run("OTk5NzAwMzQ5MjM1NTA3MjYy.G_8JRT.D3ecUW7pwn1hl7s8JDJiuflCPGxHQkzyugP4QI") #傳入bot 的token