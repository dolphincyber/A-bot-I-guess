import discord
from discord.ext import commands
import asyncio
import random
import base64
from youtube_search import YoutubeSearch
import os
import json

client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name='.help'))

#help
@client.command(pass_context=True)
async def help(ctx, page=0):
    if page == 0:
        embed = discord.Embed(title="Cury Bot Help Page", description="Go to the page you need by typing the command with the page number after it. (e.g. .help 1)", color=3447003)
        embed.add_field(name="`1` Server Utilities.", value="****", inline=False)
        embed.add_field(name="`2` Fun.", value="****", inline=False)
        embed.set_footer(text="home page")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/626633106803392513/755532296903196852/Curry.jpg')
        await ctx.send(embed=embed)
    if page == 1:
        embed = discord.Embed(title="Server Utilities", description="some server utils", inline=False)
        embed.add_field(name="clear", value="Clear mesages", inline=False)
        # embed.add_field(name="ban", value="use the ban hammer", inline=False)
        # embed.add_field(name="unban", value="uno reverse card the ban hammer", inline=False)
        # embed.add_field(name="kick", value="u know, just boot someone out of the server", inline=False)
        # embed.add_field(name="mute", value="shut someone up. thats it.", inline=False)
        # embed.add_field(name="unmute", value="UN-shut someone up. idek why you would use this smh", inline=False)
        embed.set_footer(text=f"page 1 of 2")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/626633106803392513/755532296903196852/Curry.jpg')
        await ctx.send(embed=embed)
    if page == 2:
        embed = discord.Embed(title="Fun", description="", inline=False)
        embed.add_field(name="watch", value="look for a youtube video", inline = False)
        embed.add_field(name="google", value="search google for something", inline = False)
        embed.add_field(name="spotify", value="look for a song on spotify", inline = False)
        embed.add_field(name="eightball", value="ask the so called 'mAgIC' eight ball a question", inline = False)
        embed.set_footer(text=f"page 2 of 2")
        await ctx.send(embed=embed)

#info
@client.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Info", description="Bot by NIHԀ˥Op#2625")
    embed.add_field(name="**Bot version**", value="`V.0.1.0                 `", inline=True)
    embed.add_field(name="**Built with**", value="`Python3.8                `", inline=True)
    embed.add_field(name="**contributors**", value="`ALoneParadox#8583, Frostt#1324`")
    embed.add_field(name="**This bot was made on**", value="`September 15th, 2020     `", inline=False)
    await ctx.send(embed=embed)
    
# clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit = amount + 1)

@client.command()
async def botannounce(ctx, *, code):
    verfied="jKI8ncOKTQ5dBf"
    if code == verfied:
        await ctx.send("check your cmd line")
        announcement=input("what do you want to announce?\n")
        await ctx.channel.purge(limit = 2 + 1)
        await ctx.send(announcement)
    if code != verfied:
        await ctx.send("you aren't the bot creator or an admin!!!")

# # Kick
# @client.command()
# @commands.has_permissions(kick_members=True)
# async def kick(ctx, member : discord.Member, *,reason=None):
#     await member.kick(reason=reason)
#     embed = discord.Embed(title=f"{member} has been kicked", description=str(reason), color=0)
#     await ctx.send(embed=embed)

# # Ban
# @client.command()
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, member : discord.Member, *,reason=None):
#     await member.ban(reason=reason)
#     embed = discord.Embed(title=f"{member} has been banned", description=str(reason), color=0)
#     await ctx.send(embed=embed)

# # Unban
# @client.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split("#")

#     for ban_entry in banned_users:
#         user = ban_entry.user

#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'{user.name}#{user.discriminator} has been unbanned.')
#             return

# # Mute
# @client.command()
# async def mute(ctx, *, member : discord.Member):
#     guild = ctx.guild

#     for role in guild.roles:
#         if role.name == "Muted":
#             await member.add_roles(role)
#             await ctx.send("{} has {} been muted" .format(member.mention,ctx.author.mention))
#             return

#             overwrite = discord.PermissionOverwrite(send_messages=False)
#             newRole = await guild.create_role(name="Muted")

#             for channel in guild.text_channels:
#                 await guild.channel.set_permissions(newRole,overwrite=overwrite)

#             await member.add_roles(newRole)
#             await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))

# # Unmute
# @client.command()
# async def unmute(ctx, *, member : discord.Member):
#     guild = ctx.guild

#     for role in guild.roles:
#         if role.name == "Muted":
#             await member.remove_roles(role)
#             await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
#             return

# base64
# @client.command()

# events
@client.event
async def on_member_join(member):
    await member.send(f"Welcome {member}!")
@client.event
async def on_member_leave(member):
    await member.send(f"Goodbye {member} :(")

# google
@client.command()
async def google(ctx, *, search):
    refinesearch=search.replace(" ", "+")
    await ctx.send('https://www.google.com/search?q=' + refinesearch)

# spotify
@client.command()
async def spotify(ctx, *, search):
    refinesearch=search.replace(" ", "%20")
    await ctx.send('https://open.spotify.com/search/' + refinesearch)

# Watch
@client.command()   
async def watch(ctx, *, search):
     results = YoutubeSearch(search, max_results=1).to_dict()
     x = results[0]
     await ctx.send('https://www.youtube.com' + x['url_suffix'])

# 8ball
@client.command()
async def eightball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
        "No. Just plain no.",
        "NO DEFINITELY NOT. DON'T EVEN THINK ABOUT IT."
        ]
    embed = discord.Embed(title=question, description="    🎱🎱🎱", color=8388736)
    embed.add_field(name=random.choice(responses), value="🎱🎱🎱🎱", inline=False)
    await ctx.send(embed=embed)

### Currency???
# Check for file
if os.path.exists('amounts.json'):
   with open('amounts.json', 'r') as file:
       amounts = json.load(file)
else:
   amounts = {}
# Save file
def _save():
    with open('amounts.json', 'w+') as f:
       json.dump(amounts, f)

#start
@client.command(pass_context=True)
async def start(ctx):
   id = str(ctx.message.author.id)
   if id not in amounts.keys():
       amounts[id]=0
       await ctx.send("You are now registered")
       _save()
   else:
       await ctx.send("You already have an account")

#bal
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def bal(ctx):
    id = str(ctx.message.author.id)
    if id in amounts:
        embed = discord.Embed(
           colour = discord.Colour.green()
        )
        embed.add_field(name='Your balance:', value=amounts[id])
        embed.set_footer(text="look at all that curry")
        await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have an account")
    await asyncio.sleep(15)
@bal.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error

# cook
@client.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def cook(ctx):
    amount=random.randint(0, 300)
    amount=int(amount)
    await ctx.send("you cooked some curry for your friends and they gave you " + str(amount) + " coins.")
    id = str(ctx.message.author.id)
    if id in amounts:
        amounts[id]
        amounts[id] += amount
        with open('amounts.json', 'w+') as f:
            json.dump(amounts, f)
@cook.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error

# daily
@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    id = str(ctx.message.author.id)
    embed=discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name='Daily bonus for ', value="2500 coins")
    embed.set_footer(text="come back tommorow for another bonus!")
    await ctx.send(embed=embed)
    if id in amounts:
        amounts[id]
        amounts[id] += 2500
        with open('amounts.json', 'w+') as f:
            json.dump(amounts, f)
@daily.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error


client.run('')