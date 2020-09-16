import discord
from discord.ext import commands
import asyncio
import random
import base64


client = commands.Bot(command_prefix = '.')
client.remove_command("help")

# clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
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

# base64
async def b64(ctx, *, message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    embed = discord.Embed(title=message, description="decoding using base64...", color=8388736)
    embed.add_field(name=random.choice(base64_message), value="done!", inline=False)
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
        "Very doubtful."]
    embed = discord.Embed(title=question, description="    🎱🎱🎱", color=8388736)
    embed.add_field(name=random.choice(responses), value="🎱🎱🎱🎱", inline=False)
    await ctx.send(embed=embed)

client.run('')