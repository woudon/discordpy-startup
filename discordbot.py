from discord.ext import commands
import discord
import os
import traceback


client = MyClient()
client.run('my token goes here')

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def js(ctx):
    await ctx.send('jkじゃい')
    
@bot.command()
async def jk(ctx):
    await ctx.send('jkじゃい')

@client.event
async def on_ready():
    await ctx.send('Ready!')

bot.run(token)
