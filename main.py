import discord
import asyncio
from discord.ext import commands

token = 'LOL'

client = commands.Bot(command_prefix = '++')
client.remove_command('help')

@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(0.5)    
            await user.send(message)
            await ctx.send(f'Sent "{message}" To {user}')
        except:
            pass

    
client.run(ODM1ODc2MTI5MTQ3MTkxMzM1.YIV0Tw.VIq-t-GWGj-O4G5f_xWP016PniQ)
