# CONFIG
# ---------
token = open("token.txt", "r") # To find this, it's harder than it used to be. Please Google the process.
prefix = "!" # This will be used at the start of commands.
# ----------

import discord
from discord.ext import commands

print ("Loading..")

bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")

prev_ok = None
cnt_num = 0

@bot.event
async def on_ready():
    print ("Ready to be innocent.")
# Prints when the bot is ready to be used.

@bot.event
async def on_message(message):
    global prev_ok
    global cnt_num
    if message.channel.id == 741513007896461343:
        if 'ok' in message.content:
            if message.author == prev_ok: #if the previous guy is saying ok again
                await message.add_reaction('❌')
                embed = discord.Embed(
                    title='<@' + str(message.author.id) + '> ruined at ' + str(cnt_num) + '!!!',
                    description="What a disappointment\n(You cant type 2 ok in a row.)",
                    colour=discord.Colour.red()
                )
                embed.set_footer(text="Vote for me at nowhere today!")
                await message.channel.send(embed=embed)
                cnt_num = 0
            else:
                await message.add_reaction('🆗')
                prev_ok = message.author
                cnt_num += 1
        else:
            if message.author.id == 741519044124868679: #if bot, return
                return
            else:
                await message.add_reaction('❌')
                embed = discord.Embed(
                    title='<@' + str(message.author.id) + '> ruined at ' + str(cnt_num) + '!!!',
                    description="What a disappointment\n(This channel called #ok for a reason)",
                    colour=discord.Colour.red()
                )
                embed.set_footer(text="Vote for me at nowhere today!")
                await message.channel.send(embed=embed)
                cnt_num = 0

@bot.command()
async def count(ctx):
    global cnt_num
    embed = discord.Embed(
        title='Current number: ' + str(cnt_num),
        colour=discord.Colour.green()
    )
    embed.set_footer(text="Vote for me at nowhere today!")
    await ctx.channel.send(embed=embed)
    await ctx.message.add_reaction('✅')
    return

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=discord.Colour.blue()
    )
    embed.set_footer(text="Vote for me at nowhere today!")
    await ctx.channel.send(embed=embed)
    await ctx.message.add_reaction('✅')
    return

bot.run(token.readline())