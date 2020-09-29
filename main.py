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
        embed = discord.Embed(title="Nebula Help Page", description="Go to the page you need by typing the command with the page number after it. (e.g. .help 1)", color=3447003)
        embed.add_field(name="`1` Server Utilities", value="****", inline=False)
        embed.add_field(name="`2` Fun", value="****", inline=False)
        embed.add_field(name="`3` Currency", value="****", inline=False)
        embed.set_footer(text="home page")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/643685845953675307/760220420916903996/Untitled.jpg')
        await ctx.send(embed=embed)
    if page == 1:
        embed = discord.Embed(title="Server Utilities", description="some server utils", inline=False)
        embed.add_field(name="clear", value="Clear mesages", inline=False)
        # embed.add_field(name="ban", value="use the ban hammer", inline=False)
        # embed.add_field(name="unban", value="uno reverse card the ban hammer", inline=False)
        # embed.add_field(name="kick", value="u know, just boot someone out of the server", inline=False)
        # embed.add_field(name="mute", value="shut someone up. thats it.", inline=False)
        # embed.add_field(name="unmute", value="UN-shut someone up. idek why you would use this smh", inline=False)
        embed.set_footer(text=f"page 1 of 3")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/643685845953675307/760220420916903996/Untitled.jpg')
        await ctx.send(embed=embed)
    if page == 2:
        embed = discord.Embed(title="Fun", description="", inline=False)
        embed.add_field(name="watch", value="look for a youtube video", inline = False)
        embed.add_field(name="google", value="search google for something", inline = False)
        embed.add_field(name="spotify", value="look for a song on spotify", inline = False)
        embed.add_field(name="eightball", value="ask the so called 'mAgIC' eight ball a question", inline = False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/643685845953675307/760220420916903996/Untitled.jpg')
        embed.set_footer(text=f"page 2 of 3")
        await ctx.send(embed=embed)
    if page == 3:
        embed = discord.Embed(title="currency", description="", inline=False)
        embed.add_field(name="start", value="Register for the currency feature", inline=False)
        embed.add_field(name="bal", value="Check how many coins you have", inline=False)
        embed.add_field(name="collect", value="go collect some coins :)", inline=False)
        embed.add_field(name="beg", value="beg some people for coins", inline=False)
        embed.add_field(name="daily", value="get your daily boost of coins", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/643685845953675307/760220420916903996/Untitled.jpg')
        embed.set_footer(text=f"page 3 of 3")
        await ctx.send(embed=embed)

# rulemake
@client.command()
@commands.has_permissions(administrator=True)
async def rulemake(ctx, *, rule):
    await ctx.channel.purge(limit = 1 + 1)
    await ctx.send("" + rule)

#info
@client.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Info", description="Bot by NIHԀ˥Op#2625")
    embed.add_field(name="**Bot version**", value="`V.0.1.2                 `", inline=True)
    embed.add_field(name="**Built with**", value="`Python3.8                `", inline=True)
    embed.add_field(name="**contributors**", value="`ALoneParadox#8583, Frostt#1324`")
    embed.add_field(name="**This bot was made on**", value="`September 15th, 2020     `", inline=False)
    await ctx.send(embed=embed)
    
# clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    amount=int(amount)
    await ctx.channel.purge(limit = amount + 1)

# bug
@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def bug(ctx, *, report):
    embed = discord.Embed(title="bug report", description="filed by " + str(ctx.message.author))
    embed.add_field(name=report, value="🛑🛑🛑", inline=True)
    user = client.get_user(600076125556965376)
    await user.send(embed=embed)
    await ctx.send("Thanks for reporting this bug!")
@bug.error
async def bug_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error

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
    try:
        results = YoutubeSearch(search, max_results=1).to_dict()
        x = results[0]
        await ctx.send('https://www.youtube.com' + x['url_suffix'])
    except IndexError:
        embed = discord.Embed(title='🚫 No results found for', description=f'"{search}"', color=15158332)
        await ctx.send(embed=embed)

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

# shop
@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def shop(ctx, *,page=0):
    id = str(ctx.message.author.id)
    if id in amounts:
        if page == 0:
            embed = discord.Embed(title='Shop', description="buy some EPIC stuff here", colour = discord.Colour.blurple())
            embed.add_field(name='Pages', value="`1` __Tools__\n`2` __Collectables__\n`3` __Special__\n**** - ____ -", inline=False)
            embed.set_footer(text="Page 0 of 3\ndo shop page_number to go to the page you want")
            await ctx.send(embed=embed)
        if page == 1:
            embed = discord.Embed(title='Shop', description="buy some EPIC stuff here", colour = discord.Colour.blurple())
            embed.add_field(name='Tools', value="idek yet...", inline=False)
            embed.set_footer(text="Page 1 of 3\ndo shop page_number to go to the page you want")
            await ctx.send(embed=embed)
        if page == 2:
            embed = discord.Embed(title='Shop', description="buy some EPIC stuff here", colour = discord.Colour.blurple())
            embed.add_field(name='Collectables', value="🍬 **Breath Mint** - __5__ - i guess if your breath smells...\n\n🧀 **cheese slices** - __10__ - because why not?\n\n🍪 **cookies** - __15__ - just a collectable\n\n🎻 **violin** - __2,000__ because everyone knows that orchesthra > band\n\n🌌 **galaxy badge** - __100,000__ - badge for very comited members!\n\n🎖️ **galaxy medal** - __1,000,000__ - an extremely rare medal for the richest people\n\n🏆 **galaxy trophy** - __10,000,000__ - extremely rare trophy for the richest people\n\n", inline=False)
            embed.set_footer(text="Page 2 of 3\ndo shop page_number to go to the page you want")
            await ctx.send(embed=embed)
        if page == 3:
            embed = discord.Embed(title='Shop', description="buy some EPIC stuff here", colour = discord.Colour.blurple())
            embed.add_field(name='Special', value="nothing yet...", inline=False)
            embed.set_footer(text="Page 3 of 3\ndo shop page_number to go to the page you want")
            await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have an account")
@shop.error
async def shop_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error

#bal
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def bal(ctx):
    id = str(ctx.message.author.id)
    if id in amounts:
        if amounts[id] == 69420:
            embed = discord.Embed(
                colour = discord.Colour.green()
            )
            embed.add_field(name='Your balance:', value=amounts[id])
            embed.set_footer(text="LMAO WAS THAT ON PURPOSE??")
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(
               colour = discord.Colour.green()
            )
            embed.add_field(name='Your balance:', value=amounts[id])
            embed.set_footer(text="look at all those beans")
            await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have an account")
@bal.error
async def bal_error(ctx, error):
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
@commands.cooldown(1, 30, commands.BucketType.user)
async def collect(ctx):
    amount=random.randint(0, 300)
    amount=int(amount)
    chance=random.randint(0,100)
    if chance > 70 and chance < 80:
        await ctx.send("You collected " + str(amount) + " coins, AND a 🍬 **Breath Mint**!!!")
        return
    if chance > 80 and chance < 90:
        await ctx.send("You collected " + str(amount) + " coins, AND a 🧀 **cheese slices**!!!")
        return
    if chance > 90 and chance < 95:
        await ctx.send("You collected " + str(amount) + " coins, AND a 🎻 **violin**!!!")
        return
    if chance > 95 and chance < 95:
        await ctx.send("You collected " + str(amount*2) + " coins. If you didn't know, you got DOUBLE THE COINS!")
        return
    if chance > 99:
        await ctx.send("You collected " + str(amount) + " coins, AND a 🌌 **galaxy badge**!!!!!!!!! LUCKY!!!")
        return
    else:
        await ctx.send("You collected " + str(amount) + " coins.")
        return
    id = str(ctx.message.author.id)
    if id in amounts:
        amounts[id]
        amounts[id] += amount
        with open('amounts.json', 'w+') as f:
            json.dump(amounts, f)
@collect.error
async def collect_error(ctx, error):
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
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '{:.2f}s'.format(error.retry_after)
        embed=discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name='You already ran this command! Please try again in ', value=msg)
        await ctx.send(embed=embed)
    else:
        raise error

# beg
@client.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def beg(ctx):
    id = str(ctx.message.author.id)
    await ctx.send("Where do you want to beg at?\n`S` Street\n`H` Hospital\n`R`That random guys house\n`A` In the middle of an airport")
    ans = await ctx.bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if ans.content.lower() == "s":
        poss=random.randint(0,100)
        if poss > 85:
            await ctx.send("You wernt being careful and got a little too close to the cars. Needless to say, you were ran over and died.")
            if id in amounts:
                amounts[id]
                amounts[id]=0
                with open('amounts.json', 'w+') as f:
                    json.dump(amounts, f)
                return
        num=random.randint(0, 329)
        chance=random.randint(0,100)
        if chance > 70 and chance < 80:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num) + " coins, AND a 🍬 **Breath Mint**!!!")
            return
        if chance > 80 and chance < 90:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num) + " coins, AND a 🧀 **cheese slices**!!!")
            return
        if chance > 90 and chance < 95:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num) + " coins, AND a 🎻 **violin**!!!")
            return
        if chance > 95 and chance < 95:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num*2) + " coins. If you didn't know, you got DOUBLE THE COINS!")
            return
        if chance > 99:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num) + " coins, AND a 🌌 **galaxy badge**!!!!!!!!! LUCKY!!!")
            return
        else:
            await ctx.send("So you didn't get run over by a car, and managed to get " + str(num) + " coins from people who liked your stories.")
            return
        if id in amounts:
            amounts[id]
            amounts[id] += num
            with open('amounts.json', 'w+') as f:
                json.dump(amounts, f)
    if ans.content.lower() == "h":
        poss=random.randint(0,100)
        if poss > 80:
            await ctx.send('Famous last words: "i wont get covid here lol".')
            if id in amounts:
                amounts[id]
                amounts[id]=0
                with open('amounts.json', 'w+') as f:
                    json.dump(amounts, f)
                return
        num=random.randint(0,250)
        chance=random.randint(0,100)
        if chance > 70 and chance < 80:
            await ctx.send("You didnt get covid... and got " + str(num) + " coins, AND a 🍬 **Breath Mint**!!!")
            return
        if chance > 80 and chance < 90:
            await ctx.send("You didnt get covid... and got " + str(num) + " coins, AND a 🧀 **cheese slices**!!!")
            return
        if chance > 90 and chance < 95:
            await ctx.send("You didnt get covid... and got " + str(num) + " coins, AND a 🎻 **violin**!!!")
            return
        if chance > 95 and chance < 95:
            await ctx.send("You didnt get covid... and got " + str(num*2) + " coins. If you didn't know, you got DOUBLE THE COINS!")
            return
        if chance > 99:
            await ctx.send("You didnt get covid... and got " + str(num) + " coins, AND a 🌌 **galaxy badge**!!!!!!!!! LUCKY!!!")
            return
        else:
            await ctx.send("You didnt get covid... and got " + str(num) + " coins as a prize!")
            return
        if id in amounts:
            amounts[id]
            amounts[id] += num
            with open('amounts.json', 'w+') as f:
                json.dump(amounts, f)
    if ans.content.lower() == "r":
        num=random.randint(0,1)
        await ctx.send("bruh. You serious? well at least you managed to find " + str(num) + " coins lying arround the couch")
        if id in amounts:
            amounts[id]
            amounts[id] += num
            with open('amounts.json', 'w+') as f:
                json.dump(amounts, f)
    if ans.content.lower() == "a":
        poss=random.randint(0,100)
        if poss > 75:
            await ctx.send('dude I told you to not get close to the airplanes.')
            if id in amounts:
                amounts[id]
                amounts[id]=0
                with open('amounts.json', 'w+') as f:
                    json.dump(amounts, f)
                return
        num=random.randint(0,999)
        chance=random.randint(0,100)
        if chance > 70 and chance < 80:
            await ctx.send("Noice. you manged to steal " + str(num) + " coins, AND a 🍬 **Breath Mint**!!!")
            return
        if chance > 80 and chance < 90:
            await ctx.send("Noice. you manged to steal " + str(num) + " coins, AND a 🧀 **cheese slices**!!!")
            return
        if chance > 90 and chance < 95:
            await ctx.send("Noice. you manged to steal " + str(num) + " coins, AND a 🎻 **violin**!!!")
            return
        if chance > 95 and chance < 95:
            await ctx.send("Noice. you manged to steal " + str(num*2) + " coins. If you didn't know, you got DOUBLE THE COINS!")
            return
        if chance > 99:
            await ctx.send("Noice. you manged to steal " + str(num) + " coins, AND a 🌌 **galaxy badge**!!!!!!!!! LUCKY!!!")
            return
        else:
            await ctx.send("Noice. you manged to steal " + str(num) + "  coins from under the pilot's noses.")
            return
        if id in amounts:
            amounts[id]
            amounts[id] += num
            with open('amounts.json', 'w+') as f:
                json.dump(amounts, f)
@beg.error
async def beg_error(ctx, error):
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