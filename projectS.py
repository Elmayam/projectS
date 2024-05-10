import discord
import datetime
import asyncio

from discord.ext import commands

day2= datetime.date(2025, 11, 3)
diff = day2 - datetime.date.today()
diff = str(diff).replace(' days', '일')


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    while True:
        print(f'updated bot: {bot.user} /'+diff.split(",")[0])
        await bot.change_presence(activity=discord.Game("전역까지 "+diff.split(",")[0]))
        await asyncio.sleep(10800)
       
        
    
bot.run("botToken")

