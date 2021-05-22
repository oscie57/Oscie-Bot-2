import sys

print('-----------------------------------------------')
print('Module Path')
print(sys.path)

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import random
import datetime
import sys
import typing
from dotenv import load_dotenv
import os

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()

bot = commands.Bot(case_insensitive=True, command_prefix='o.', description=description, intents=intents)

bot.remove_command('help')

slash = SlashCommand(bot, sync_commands=True)

def owner(ctx):  # Check if it is me
    return ctx.author.id == 729135459405529118

@slash.slash(name="setup", guild_ids=[804449200921509913], description="Reset commands list")
@commands.check(owner)
async def _setup(ctx: SlashContext):
    await ctx.send('Commands list reset.')
    print('Command list reset')


'''Bot Start - Logging Begins'''


@bot.event  # When the bot starts up
async def on_ready():
    currentDT = datetime.datetime.now()
    print('-----------------------------------------------')
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print(f'Log started at: {currentDT}')
    print('-----------------------------------------------')
    print('To avoid most errors, make sure the bot has')
    print('the required permissions in all Guilds')
    print('-----------------------------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the beat"))
    '''lavalink.initialize(
        bot, host='localhost', password='password',
        rest_port=2332, ws_port=2333
    )'''


'''Invite updates'''

@bot.event  # When an invite is created
async def on_invite_create(invite):
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {invite.guild} | Invite created - {invite.code}')
@bot.event  # When an invite is deleted
async def on_invite_delete(invite):
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {invite.guild} | Invite deleted - {invite.code}')

'''Error responses'''

@bot.event
async def on_slash_command_error(ctx: SlashContext, error):
    if isinstance(error, commands.MissingPermissions):
        embed1 = discord.Embed(color=0xFF6259)
        embed1.set_author(name="error reporter", icon_url="https://oscie.tk/assets/logo.png")
        embed1.add_field(name="Error Handler", value="Whoopsies, seems you do not have the permissions to run this command! Sorry about that.\n\nIf you believe this is an error, [make an issue here](https://github.com/Oscie57/Oscie-Bot-Issues)", inline=False)
        await ctx.send(embed=embed1)
    if isinstance(error, commands.MissingRequiredArgument):
        embed2 = discord.Embed(color=0xFF6259)
        embed2.set_author(name="error reporter", icon_url="https://oscie.tk/assets/logo.png")
        embed2.add_field(name="Error Handler", value="Whoopsies, seems you missed out some very important information needed to run this command! Sorry about that.\n\nIf you believe this is an error, [make an issue here](https://github.com/Oscie57/Oscie-Bot-Issues)", inline=False)
        await ctx.send(embed=embed2)
    if isinstance(error, commands.CommandNotFound):
        embed3 = discord.Embed(color=0xFF6259)
        embed3.set_author(name="error reporter", icon_url="https://oscie.tk/assets/logo.png")
        embed3.add_field(name="Error Handler", value="Whoopsies, seems this command doesn't exist! (how the hell did you trigger this) Sorry about that.\n\nIf you believe this is an error, [make an issue here](https://github.com/Oscie57/Oscie-Bot-Issues)", inline=False)
        await ctx.send(embed=embed3)

@slash.slash(name="suggest", guild_ids=[804449200921509913], description="Suggest changes to the server, bot or Twitch channel", options=[
    create_option(name="suggestion", description="The actual suggestion", option_type=3, required=True),
])
async def _suggest(ctx: SlashContext, suggestion: str):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="server suggestions", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Suggestion", value=suggestion, inline=False)
    embed.add_field(name="Date Suggested", value=datetime.datetime.today().strftime("%d/%m/%Y"), inline=False)
    await ctx.channel.purge(limit=1)
    await ctx.send("<@729135459405529118>", embed=embed)

'''Recreational Commands'''
@slash.slash(name="streams", guild_ids=[804449200921509913], description="Upload stream archive info", options=[
    create_option(name="title", description="Stream Title", option_type=3, required=True),
    create_option(name="desc", description="YouTube Description", option_type=3, required=True),
    create_option(name="link", description="YouTube VOD Link", option_type=3,  required=True),
    create_option(name="number", description="Stream Number", option_type=4, required=True),
    create_option(name="date", description="Date of Stream", option_type=3, required=True),
    create_option(name="thumb", description="VOD Thumbnail", option_type=3, required=True),
])
@commands.check(owner)
async def _streams(ctx: SlashContext, title: str, desc: str, link: str, number: int, date: str, thumb: str):
    embed = discord.Embed(color=0x6441A5, description=f"Streamed Live at {date} - Stream #{number}")
    embed.set_author(name="https://twitch.tv/0scie", icon_url="https://oscie.tk/assets/logo.png")
    embed.set_thumbnail(url="https://cdn.oscie.tk/files/square.png")
    embed.set_image(url=thumb)
    embed.add_field(name="Stream Title", value=title, inline=False)
    embed.add_field(name="Description", value=desc, inline=False)
    embed.add_field(name="VOD Link", value=f"[Click here to go to VOD!]({link})", inline=False)
    await ctx.send(f"<@&822160446545985556> Stream Archive #{number}", embed=embed)
#ecdpguides
#projects
#repeat
#add
#projects
#time
#choose
#ping
#say
#rubbish

@bot.command()
async def o(ctx):
    '''o.o'''
    await ctx.send('o.o')

'''Maintenence Commands'''
#status
#shutdown
@slash.slash(name="invite", guild_ids=[804449200921509913], description="Invite the bot to your own server")
async def _invite(ctx: SlashContext):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="oscie bot 2", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Invitation", value="Would you like to invite the bot to your server? Honestly, there's no point, since the guild IDs are hard-coded in and IDK how to make it work for multiple servers, welp if you really want it:\n\n[Bot invite 1: Has Slash Command usage enabled](https://discord.com/oauth2/authorize?client_id=776246244297146418&scope=bot&permissions=2147483648)\n[Bot invite 2: Has main permissions](https://discord.com/oauth2/authorize?client_id=776246244297146418&scope=bot&permissions=8)\n[Bot invite 3: Slash Command creation permission](https://discord.com/oauth2/authorize?client_id=776246244297146418&scope=applications.commands)\n\nLike I said, no commands would work, so, gl ig.")
    await ctx.send(embed=embed)

@slash.slash(name="help", guild_ids=[804449200921509913], description="Get help with the bot!")
async def _help(ctx: SlashContext):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="oscie bot 2", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Help info", value="This bot no longer requires a help command, since Discord handles Slash Commands.\n\nIf you ever have issues with the bot, make an issue at https://github.com/Oscie57/Oscie-Bot-Issues", inline=False)
    await ctx.send(embed=embed)

@slash.slash(name="shutdown", guild_ids=[804449200921509913], description="Shuts down the bot (Owner Only)")
@commands.check(owner)
async def _shutdown(ctx: SlashContext):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="bot maintenance", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Shutting down!", value="Don't forget to restart in the terminal!")
    await ctx.send(embed=embed)
    currentDT = datetime.datetime.now()
    print('-----------------------------------------------')
    print(f'Shutdown triggered - {ctx.guild}')
    print(f'Log ended at: {currentDT}')
    print('-----------------------------------------------')
    await bot.change_presence(status=discord.Status.invisible)
    exit()

@slash.slash(name="status", guild_ids=[804449200921509913], description="A command to control the status/activity of the bot (Owner only)", options=[
    create_option(name="status", description="Change the status of the bot", option_type=3, required=True, choices=[
        create_choice(name="Do Not Disturb", value="dnd"),
        create_choice(name="Idle", value="idle"),
        create_choice(name="Online", value="online"),
        create_choice( name="Invisible", value="invisible"),
    ]),
    create_option(name="activitytype", description="Change the Activity Type of the bot", option_type=3, required=False, choices=[
        create_choice(name="Listening", value="listening"),
        create_choice(name="Streaming", value="streaming"),
        create_choice(name="Playing", value="playing"),
        create_choice(name="Watching", value="watching"),
    ])
])
@commands.check(owner)
async def _status(ctx, status: str, activitytype: str):
    if status == "idle":
        await bot.change_presence(activity=discord.Activity(status=discord.Status.idle))
        embed2 = discord.Embed(color=0xFEE75C)
        embed2.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed2.add_field(name="Status", value=status, inline=False)
        await ctx.send(embed=embed2)
    elif status == "online":
        await bot.change_presence(activity=discord.Activity(status=discord.Status.online))
        embed1 = discord.Embed(color=0x57F287)
        embed1.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed1.add_field(name="Status", value=status, inline=False)
        await ctx.send(embed=embed1)
    elif status == "invisible":
        await bot.change_presence(activity=discord.Activity(status=discord.Status.invisible))
        embed3 = discord.Embed(color=0xA6A6A6)
        embed3.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed3.add_field(name="Status", value=status, inline=False)
        await ctx.send(embed=embed3)
    elif status == "dnd":
        await bot.change_presence(activity=discord.Activity(status=discord.Status.dnd))
        embed4 = discord.Embed(color=0xED4245)
        embed4.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed4.add_field(name="Status", value=status, inline=False)
        embed4.add_field(name="Activity Type", value=activitytype, inline=False)
        await ctx.send(embed=embed4)
    else:
            return
    if activitytype == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the beat"))
        embed1 = discord.Embed(color=0x17FF56)
        embed1.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed1.add_field(name="Activity Type", value=activitytype, inline=False)
        await ctx.send(embed=embed1)
    elif activitytype == "streaming":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="nothingness"))
        embed2 = discord.Embed(color=0xA200FF)
        embed2.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed2.add_field(name="Status", value=status, inline=False)
        embed2.add_field(name="Activity Type", value=activitytype, inline=False)
        await ctx.send(embed=embed2)
    elif activitytype == "playing":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="alone"))
        embed3 = discord.Embed(color=0x7289DA)
        embed3.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed3.add_field(name="Status", value=status, inline=False)
        embed3.add_field(name="Activity Type", value=activitytype, inline=False)
        await ctx.send(embed=embed3)
    elif activitytype == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="little witch academia"))
        embed4 = discord.Embed(color=0xFF2E3C)
        embed4.set_author(name="status update", icon_url="https://oscie.tk/assets/logo.png")
        embed4.add_field(name="Status", value=status, inline=False)
        embed4.add_field(name="Activity Type", value=activitytype, inline=False)
        await ctx.send(embed=embed4)
    else:
        return

'''Moderation Commands'''
@slash.slash(name="clear", guild_ids=[804449200921509913], description="Clears an amount of messages", options=[
    create_option(name="limit", description="Amount of messages you would like to delete", option_type=4, required=True)
])
@commands.has_permissions(manage_messages=True)
async def _clear(ctx: SlashContext, limit: int):
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(color=0x7289DA, description=f"{limit} messages deleted")
    embed.set_author(name="moderation", icon_url="https://oscie.tk/assets/Logo.png")
    await ctx.send(embed=embed)
#clearuser
#kick
#mute
#unmute
#ban
#unban

'''Store Commands'''

'''Server Specific Commands'''
@slash.slash(name="servers", guild_ids=[804449200921509913], description="Server Specific Commands", options=[
    create_option(name="lnh", description="Legacy Nintendo Homebrew commands", option_type=3, required=True, choices=[
        create_choice(name="Server Invite", value="lnhinvite"),
        create_choice(name="Link Guide", value="lnhlink"),
        create_choice(name="NKit Tools", value="lnhnkit"),
    ]),
])
async def _servers(ctx: SlashContext, lnh: str):
    if lnh == "lnhinvite":
        await ctx.send('discord.gg/XQnNR9N')
    elif lnh == "lnhlink":
        await ctx.send('https://cdn.discordapp.com/attachments/546727695547891712/822805639990083637/2021-03-20_12-15-19.mp4')
    elif lnh == "lnhnkit":
        await ctx.send('https://gbatemp.net/download/nkit.36157/')
    else:
        return
    

'''Bot Token'''
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))

'''Special Thanks:'''
# @Hentai#8349 - Help with Clear command