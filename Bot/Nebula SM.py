import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import base64
from youtube_search import YoutubeSearch
import os
import json

client = commands.Bot(command_prefix = 'SM.')
client.remove_command("help")

# events
@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name='SM.help'))
@client.event
async def on_member_join(ctx,member):
    role = discord.utils.get(ctx.guild.roles, name = "not verified") 
    await ctx.add_roles(member,role)

# sendrule (temp)
@commands.has_permissions(administrator=True)
@client.command()
async def sendrule(ctx):
    await ctx.channel.purge(limit = 1 + 1)
    embed=discord.Embed(title="Server rules", description="run SM.verify in #verify", inline=True)
    embed.add_field(name="🔐", value="No spaming!!!", inline=False)
    embed.add_field(name="🔐", value="Only do .bug when you REALLY need to, as this sends a DM to the bot owner", inline=False)
    embed.add_field(name="🔐", value="Please only play on the bot in the bot play channels", inline=False)
    embed.add_field(name="🔐", value="Don't beg for permissions, doing so will only result in you getting warned, and muted", inline=False)
    embed.set_footer(text="This bot was made for SERVER MANAGEMENT only and if you want other functions, invite NEBULA to your server.")
    await ctx.send(embed=embed)

# verify
@client.command()
async def verify(ctx):
    user = ctx.author
    role = discord.utils.get(user.guild.roles, name="verified")
    await user.add_roles(role)
    await ctx.send(f'{ctx.author.mention} You have been verified.')

# check
if os.path.exists('fault.json'):
   with open('fault.json', 'r') as file:
       fault = json.load(file)
else:
   fault = {}
if os.path.exists('count.json'):
   with open('count.json', 'r') as file:
       count = json.load(file)
else:
   count = {}

@client.command()
async def rank(ctx):
  id = str(ctx.author.id)
  if id in count:
    if count[id] == 10:
        await ctx.send('Level 1')
    elif count[id] == 20:
        await ctx.send('Level 2')
    elif count[id] == 30:
        await ctx.send('Level 3')
    elif count[id] == 40:
        await ctx.send('Level 4')
    elif count[id] == 50:
        await ctx.send('Level 5')
    elif count[id] == 70:
        await ctx.send('Level 6')
    elif count[id] == 90:
        await ctx.send('Level 7')
    elif count[id] == 110:
        await ctx.send('Level 8')
    elif count[id] == 130:
        await ctx.send('Level 9')
    elif count[id] == 150:
        await ctx.send('Level 10')
    elif count[id] == 180:
        await ctx.send('Level 11')
    elif count[id] == 210:
        await ctx.send('Level 12')
    elif count[id] == 240:
        await ctx.send('Level 13')
    elif count[id] == 270:
        await ctx.send('Level 14')
    elif count[id] == 300:
        await ctx.send('Level 15')
    elif count[id] == 340:
        await ctx.send('Level 16')
    elif count[id] == 380:
        await ctx.send('Level 17')
    elif count[id] == 420:
        await ctx.send('Level 18')
    elif count[id] == 460:
        await ctx.send('Level 19')
    elif count[id] == 500:
        await ctx.send('Level 20')
    elif count[id] == 550:
        await ctx.send('Level 21')
    elif count[id] == 600:
        await ctx.send('Level 22')
    elif count[id] == 650:
        await ctx.send('Level 23')
    elif count[id] == 700:
        await ctx.send('Level 24')
    elif count[id] == 750:
        await ctx.send('Level 25')
    elif count[id] == 810:
        await ctx.send('Level 26')
    elif count[id] == 870:
        await ctx.send('Level 27')
    elif count[id] == 930:
        await ctx.send('Level 28')
    elif count[id] == 990:
        await ctx.send('Level 29')
    elif count[id] == 1100:
        await ctx.send('Level 30')
    else:
        await ctx.send('No Level')

@client.event
async def on_message(message):
    user = str(message.author.id)
    if user in count:
        count[id] += 1
    else:
        count[id] = 1
    with open('count.json','w+') as file:
        json.dump(count, file)

# warn
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.has_permissions(ban_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    id = str(client.get_user(member.id))
    if id not in fault.keys():
        embed = discord.Embed(title=f"{member} has been warned", description="**Reason: **" +str(reason), color=9936031)
        await ctx.send(embed=embed)
        fault[id]=1
        with open('fault.json', 'w+') as i:
            json.dump(fault, i)
    else:
        embed = discord.Embed(title=f"{member} has been warned", description="**Reason: **" +str(reason), color=9936031)
        await ctx.send(embed=embed)
        fault[id]
        fault[id] += 1
        with open('fault.json', 'w+') as i:
            json.dump(fault, i)
    
# infractions
@client.command() 
async def infractions(ctx, member : discord.Member):
        id = str(client.get_user(member.id))
        if id in fault:
            embed = discord.Embed(
               colour = discord.Colour.green()
            )
            embed.add_field(name=f"{member}'s infractions: ", value=fault[id])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member} dosen't have any infractions")

# clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    amount=int(amount)
    await ctx.channel.purge(limit = amount + 1)

# Kick
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f"{member} has been kicked", description=str(reason), color=0)
    await ctx.send(embed=embed)

# Ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f"{member} has been banned", description=str(reason), color=0)
    await ctx.send(embed=embed)

# Unban
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} has been unbanned.')
            return

# Mute
@client.command()
async def mute(ctx, *, member : discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has {} been muted" .format(member.mention,ctx.author.mention))
            return
        else:
            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")
            for channel in guild.text_channels:
                await guild.channel.set_permissions(newRole,overwrite=overwrite)
            await member.add_roles(newRole)
            await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))

# Unmute
@client.command()
async def unmute(ctx, *, member : discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
            return


client.run('NzYwOTQ1MjE5ODEzNzY5Mjg2.X3Tbdg.OEZs7ujHG0itED66mHLhu1YKv6M')