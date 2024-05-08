import discord
import datetime
import os

from discord.ext import commands

day2= datetime.date(2025, 11, 3)
diff = day2 - datetime.date.today()
diff = str(diff).replace(' days', '일')


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    await bot.change_presence(activity=discord.Game("전역까지 "+diff.split(",")[0]))
    

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
