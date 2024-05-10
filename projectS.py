import discord
import datetime
import time

from discord.ext import commands

day2= datetime.date(2025, 11, 3)
diff = day2 - datetime.date.today()
diff = str(diff).replace(' days', '일')


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    while True:
        print(f'Login bot: {bot.user}')
        await bot.change_presence(activity=discord.Game("전역까지 "+diff.split(",")[0]))
        time.sleep(10800)
    
bot.run("MTIzNzYxMzMxOTIwOTA5NTE2OQ.GjQP5L.gqROLqoE-LHzrGp3FOIekHSUCo_mNsRCnQEYCw")

