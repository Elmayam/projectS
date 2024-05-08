import discord
import datetime

from discord.ext import commands

day2= datetime.date(2025, 11, 3)
diff = day2 - datetime.date.today()
diff = str(diff).replace(' days', '일')


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    await bot.change_presence(activity=discord.Game("전역까지 "+diff.split(",")[0]))
    
    
bot.run("MTIzNzYxMzMxOTIwOTA5NTE2OQ.GOeTBh.PCa6xH0Z28gOj_XcJci8gEb0TwiHpproljAm1E")