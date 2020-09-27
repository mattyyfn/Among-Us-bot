import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import logging
import random
import datetime
import time


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    (f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')
    

    await client.change_presence(activity=discord.Game(name='Among Us', type=1, url='https://twitch.tv/mattyyfn'))
    print(f'Ready to go.')
  
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")

    await channel.send(f"<:3843_green_blue_arrow:759377418317201428>{member.mention} is a new crewmate.")
                 





@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(client.latency * 1000)}ms`')


@client.command()
async def join(ctx, member: discord.Member = None):

    if not member:
         member = ctx.message.author
         await ctx.message.delete()
         commands.cooldown(1, 30, commands.BucketType.user)

    embed = discord.Embed(
        colour=discord.Colour.red(),
        title='Matchmaking',
        description=f"Direct message {member.mention} to play.",
       
    )

    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=f" {ctx.author} is looking for players.")  
    
  

    await ctx.send(embed=embed)


@client.command()
async def avatar(ctx, member: discord.Member):
    await ctx.message.delete()
    show_avatar = discord.Embed(

        colour = discord.Colour.red(),
        
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@client.command(pass_context = 1)
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, args : str = None):
    await ctx.message.delete()
    await ctx.send(args)

@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    total_text_channels = len(ctx.guild.text_channels)
    total_voice_channels = len(ctx.guild.voice_channels)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    
    embed.add_field(name="Region", value=region, inline=True)
    
    embed.add_field(name="Members", value=memberCount, inline=True)
    
    embed.add_field(name="Text Channels", value=total_text_channels, inline=True)
    
    embed.add_field(name="Voice Channels", value=total_voice_channels, inline=True)

    await ctx.send(embed=embed)


@client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


@client.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    colour=discord.Colour.red()
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)


@client.command()
async def create(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(1):
        try:
            await ctx.guild.create_voice_channel(name="Lobby"),
        except:
            return
        







client.run('TOKEN')
