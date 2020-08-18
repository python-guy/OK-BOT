# CONFIG
# ---------
token = open("token.txt", "r") # To find this, it's harder than it used to be. Please Google the process.
prefix = "~" # This will be used at the start of commands.
# ----------

import discord
from discord.ext import commands

print ("Loading..")

bot = commands.Bot(command_prefix = prefix)

prev_ok = None
cnt_num = 0

@bot.event
async def on_ready():
    print ("Ready to be innocent.")
# Prints when the bot is ready to be used.

@bot.command()
async def count(ctx):
    global cnt_num
    embed = discord.Embed(
        title='Current number: ' + str(cnt_num),
        colour=discord.Colour.blue()
    )
    embed.set_footer(text="Vote for me at nowhere today!")
    await ctx.channel.send(embed=embed)
    await ctx.message.add_reaction('✅')
    return

bot.run(token.readline())
