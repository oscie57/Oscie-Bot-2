import random
import datetime
import sys
import typing

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext


print('-----------------------------------------------')
print('Module Path')
print(sys.path)

# import lavalink
# import requests

'''Bot Description'''

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

'''Bot Intents'''

intents = discord.Intents.all()
# intents.members = True

'''Extra Information'''

bot = commands.Bot(case_insensitive=True, command_prefix='o.', description=description, intents=intents)
bot.remove_command('help')
slash = SlashCommand(bot)

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


@bot.event  # When there is a discordpy error (not all)
async def on_command_error(ctx, error):
    currentDT = datetime.datetime.now()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
        print(f'({currentDT}) {ctx.guild} | Error: MissingRequiredArgument')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command. Use `o.help` for valid commands.')
        print(f'({currentDT}) {ctx.guild} | Error: CommandNotFound')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')
        print(f'({currentDT}) {ctx.guild} | Error: MissingPermissions')


'''Personal check'''


def is_it_me(ctx):  # Check if it is me
    return ctx.author.id == 729135459405529118


'''Status commands'''


@bot.group(invoke_without_command=True)
async def status(ctx):
    '''Change the bot status with a subcommand'''
    await ctx.send('Either you didnt include a subcommand or you used an incorrect one. Please do `o.help status` to see all subcommands.')


@status.command(description="Testing Description")
@commands.check(is_it_me)
async def idle(ctx):
    '''Sets bot status to Idle'''
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the beat"), status=discord.Status.idle)
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | Status Changed - Idle')


@status.command()
@commands.check(is_it_me)
async def online(ctx):
    '''Sets bot status to Online'''
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the beat"), status=discord.Status.online)
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | Status Changed - Online')


@status.command()
@commands.check(is_it_me)
async def dnd(ctx):
    '''Sets bot status to Do not Disturb'''
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the beat"), status=discord.Status.dnd)
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | Status Changed - Do not Disturb')


@status.command()
@commands.check(is_it_me)
async def invisible(ctx):
    '''Sets bot status to Invisible'''
    await bot.change_presence(activity=discord.Game('Brrrrrrr ● o.help'), status=discord.Status.invisible)
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | Status Changed - Invisible')


'''Bot Info Commands'''

@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(color=0x7289DA, title="embed slash", title_url="https://oscie.tk/")
    embed.add_field(name="lol name", value="pfft", inline=False)

@bot.command()
async def help(ctx):
    '''Testing'''
    await ctx.send('Coming Soon!')
    embed1 = discord.Embed(color=0x7289DA)
    embed1.set_author(name="oscie bot 2 - info", icon_url="https://oscie.tk/assets/logo.png")
    embed1.add_field(name="Temporary", value="Plans:\n```- Add database\n- Add commands group to said DB\n- Add commands to each group\n- Add commands to cogs```", inline=False)
    embed1.add_field(name="Urgency", value="**Major**", inline=False)
    embed2 = discord.Embed(color=0x7289DA)
    embed2.set_author(name="oscie bot 2 - commands", icon_url="https://oscie.tk/assets/logo.png")
    embed2.add_field(name="Testing", value="Testing", inline=False)
    embed3 = discord.Embed(color=0x7289DA)
    embed3.set_author(name="oscie bot 2 - updates", icon_url="https://oscie.tk/assets/logo.png")
    embed3.add_field(name="Added Things", value="```yaml\n+ Confession Commands```", inline=False)
    embed3.add_field(name="Changed Things", value="```fix\n* Help command\n* Adding embeds slowly```", inline=False)
    embed3.add_field(name="Removed Things", value="```diff\n- Nothing```", inline=False)
    embed3.add_field(name="Planned Things", value="```Audio commands\neCDP Guide commands```")
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)


@bot.group(invoke_without_command=True)
async def info(ctx):
    '''Bot Information Commands'''
    await ctx.send('Please invoke a subcommand or use `o.help info`')


@info.command()
async def invite(ctx):
    '''Gives the bot invite information'''
    currentDT = datetime.datetime.now()
    permission = 8
    inviteLink = f'https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions={permission}'
    print(f'({currentDT}) {ctx.guild} | Invite Link sent - {ctx.author}')
    await ctx.send(inviteLink)
@info.command()
async def site(ctx):
    '''Info for the bot'''
    await ctx.send('https://oscie.tk/bot')
@info.command()
@commands.check(is_it_me)
async def test(ctx):
    '''Testing Command'''
@info.command()
@commands.check(is_it_me)
async def getupdate(ctx):
    '''Get update'''
    await ctx.send('```diff\n+Update DATE - Oscie Bot 2\n-------------------------\n-Thing One\n-Thing Two```')
@info.command()
async def issue(ctx):
    await ctx.send(
        'Having an issue or want to suggest a command? Report it here!\nhttps://github.com/Oscie57/Oscie-Bot-Issues/issues')


'''Shitpost commands'''


@bot.command(aliases=["spam"])  # Repeat a message many times (one word)
@commands.has_permissions(manage_messages=True)
async def repeat(ctx, times: int, *args):
    '''Repeat a single word to annoy people'''
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | Command "repeat" triggered {times} times - {ctx.author}')
    for i in range(times):
        await ctx.send(" ".join(args))


'''Store Links'''


@bot.group(aliases=["shop"], invoke_without_command=True)
async def store(ctx):
    '''Shows store links'''
    await ctx.send('This is the Discord store for free and paid games, and stickers. (More added soon)')
    await ctx.send('For more info, and for subcommands, please run `o.help store`')


@store.group(invoke_without_command=True)
async def stickers(ctx):
    '''Shows Sticker store pages
    Usage: "o.store stickers [stickerpack]"'''
    await ctx.send(
        'To find the stickers currently avaliable in this store, type `o.help store stickers`. Please note: These pages will only work if you are in one of these following countries, `Canada`, `Brazil` or `Japan`.')


@store.group(aliases=["servers"], invoke_without_command=True)
async def invites(ctx):
    '''Shows Game store invites
    Usage: "o.store invites|servers [servername]"'''
    await ctx.send(
        'These are games that do not have specific (linkable) store pages, so you will have to join the developers server to obtain the game. Use `o.help store invites` to see the applicable games.')


@store.group(aliases=["games"], invoke_without_command=True)
async def sku(ctx):
    '''Shows Game store pages (SKU)
    Usage: "o.store sku|games [gamename]"'''
    await ctx.send(
        'These are games that have store pages that can be directly installed or visited. Most are free, but there are a few paid in the mix. Use `o.help store sku` for a list of games and price.')


@store.group(invoke_without_command=True)
async def extras(ctx):
    '''Shows extra store pages
    Usage: "o.store extras [extra]"'''
    await ctx.send(
        'These are store pages that are either for jokes or do nothing. Use `o.help store extras` for a full list')


@store.group(invoke_without_command=True)
async def dlc(ctx):
    '''Shows DLC pages (needs Base Game)
    Usage: "o.store dlc [game]"'''
    await ctx.send(
        'These are store pages that are DLC (downloadable content) that are avaliable for discord games that we have in the other store commands. Use `o.help store dlc` for the list of games with DLC')


@stickers.command()
async def whatsupwumpus(ctx):
    '''What's Up Wumpus - £2.99'''
    await ctx.send('https://ptb.discord.com/store/skus/748286108348973106/what-s-up-wumpus-sticker-pack')


@stickers.command()
async def hellowumpus(ctx):
    '''Hello Wumpus - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/749043407997108384/hello-wumpus-sticker-pack')


@invites.command()
async def patchquest(ctx):
    '''Patch Quest server invite'''
    await ctx.send('Patch Quest (Public Beta) - Free')
    await ctx.send('https://discord.com/invite/pyF5jmP')


@invites.command()
async def cookiedragon(ctx):
    '''Two Kinds Online server invite'''
    await ctx.send('Two Kinds Online (Alpha) - Free')
    await ctx.send('https://discord.gg/cookiedragon')


@invites.command()
async def cycle28(ctx):
    '''Cycle 28 Invite'''
    await ctx.send('Cycle 28 - £0.99 (-50%)')
    await ctx.send('https://discord.gg/FpD4SuYeCm')


@invites.command()
async def staysafe(ctx):
    '''Yellowcake Games Invite'''
    await ctx.send('Stay Safe - £2.99')
    await ctx.send('https://discord.gg/yellowcakegames')


@invites.command()
async def hexrunpro(ctx):
    '''Hex! Run Pro Invite'''
    await ctx.send('Hex! Run Pro - £19.99')
    await ctx.send('https://discord.gg/S9yAhrJrDg')


@extras.command()
async def poggers(ctx):
    '''Poggers'''
    await ctx.send('https://canary.discord.com/store/skus/692146322924372089/poggers')


@extras.command()
async def yoshi(ctx):
    '''Yoshi game'''
    await ctx.send('https://ptb.discord.com/store/skus/710797635388178462/yoshi')


@extras.command()
async def wiilink24(ctx):
    '''Installing WiiLink24'''
    await ctx.send('https://ptb.discord.com/store/skus/806878609302093866/installing-wiilink24')


@extras.command()
async def nitro(ctx):
    '''Discord Nitro Classic'''
    await ctx.send('https://ptb.discord.com/store/skus/715629060331405382/nitro-classic')


@extras.command()
async def bge(ctx):
    '''Best Game Ever'''
    await ctx.send('https://ptb.discord.com/store/skus/461618159171141643/best-game-ever')


@sku.command()
async def koth(ctx):
    '''King of the Hat - £14.99'''
    await ctx.send('https://ptb.discord.com/store/skus/486981988109254667/king-of-the-hat')


@sku.command()
async def minionmasters(ctx):
    '''Minion Masters - Free (DLC)'''
    await ctx.send('https://ptb.discord.com/store/skus/488607666231443456/minion-masters')


@dlc.command()
async def minionmasters(ctx):
    '''Minion Masters DLC - `o.store sku minionmasters`'''
    await ctx.send(
        'https://ptb.discord.com/store/skus/742277397105213440/nightmares\nhttps://canary.discord.com/store/skus/515467071924994048/all-masters\nhttps://canary.discord.com/store/skus/491564667983101953/premium-upgrade\nhttps://canary.discord.com/store/skus/548071645265264650/voidborne-onslaught\nhttps://canary.discord.com/store/skus/639095281668849664/crystal-conquest')
    await ctx.send(
        'https://canary.discord.com/store/skus/565546081975533578/accursed-army-pack\nhttps://canary.discord.com/store/skus/607929247578849283/might-of-the-slither-lords\nhttps://canary.discord.com/store/skus/678878135697145866/zealous-inferno\nhttps://canary.discord.com/store/skus/707885099101847622/charging-into-darkness')


@sku.command()
async def cdreboot(ctx):
    '''Cerpe Diem: Reboot - £4.99'''
    await ctx.send('https://canary.discord.com/store/skus/568922402390671360/carpe-diem-reboot')


@sku.command()
async def forsakenr(ctx):
    '''Forsaken Remastered - £16.98'''
    await ctx.send('https://ptb.discord.com/store/skus/494870847777931268/forsaken-remastered')


@sku.command()
async def forager(ctx):
    '''Forager - £14.99'''
    await ctx.send('https://ptb.discord.com/store/skus/530541618504269875/forager')


@sku.command()
async def staysafe(ctx):
    '''Stay Safe - £2.99'''
    await ctx.send('https://ptb.discord.com/store/skus/431807599860514817/stay-safe')


@sku.command()
async def steelseraph(ctx):
    '''Steel Seraph - £1.99 (-33%)'''
    await ctx.send('https://ptb.discord.com/store/skus/555820631007035413/steel-seraph')


@sku.command()
async def tanglewood(ctx):
    '''TANGLEWOOD® - £7.99 (-43%)'''
    await ctx.send('https://ptb.discord.com/store/skus/378315252749565952/tanglewood-r')


@sku.command()
async def temtem(ctx):
    '''Temtem - £30.99'''
    await ctx.send('https://ptb.discord.com/store/skus/558547388583772201/temtem')


@sku.command()
async def thevagrant(ctx):
    '''The Vagrant - £1.99 (-50%)'''
    await ctx.send('https://ptb.discord.com/store/skus/562121024993230868/the-vagrant')


@sku.command()
async def underonewing(ctx):
    '''Under One Wing - £28.99'''
    await ctx.send('https://ptb.discord.com/store/skus/555856535327342592/under-one-wing')


@sku.command()
async def newtontree(ctx):
    '''Newton and the Apple Tree - £38.99'''
    await ctx.send('https://ptb.discord.com/store/skus/555867662442430483/newton-and-the-apple-tree')


@sku.command()
async def zombsroyaleio(ctx):
    '''ZombsRoyale.io - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/519338998791929866/zombsroyale-io')


@sku.command()
async def realmroyale(ctx):
    '''Realm Royale - Free (DLC)'''
    await ctx.send('https://ptb.discord.com/store/skus/518088627234930688/realm-royale')


@dlc.command()
async def realmroyale(ctx):
    '''Realm Royale DLC - `o.store sku realmroyale`'''
    await ctx.send(
        'https://canary.discord.com/store/skus/564916655285600266/realm-royale-bass-drop-bundle\nhttps://canary.discord.com/store/skus/595360871472168991/realm-royale-cute-but-deadly-pack')


@sku.command()
async def paladins(ctx):
    '''Paladins - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/528145079819436043/paladins')


@sku.command()
async def heartwoods(ctx):
    '''Heart of the Woods - £10.25 (-32%)'''
    await ctx.send('https://ptb.discord.com/store/skus/555830991168733204/heart-of-the-woods')


@sku.command()
async def amagicalgirl(ctx):
    '''A Magical High School Girl - £4.67 (-53%)'''
    await ctx.send('https://ptb.discord.com/store/skus/555812072969994260/a-magical-high-school-girl')


@sku.command()
async def warframe(ctx):
    '''Warframe - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/494959992483348480/warframe')


@sku.command()
async def pickcrafter(ctx):
    '''Pickcrafter - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/560643262424285194/pickcrafter')


@sku.command()
async def assitd(ctx):
    '''AT SUNDOWN: Shots in the Dark - £11.24'''
    await ctx.send('https://ptb.discord.com/store/skus/487031053454802946/at-sundown-shots-in-the-dark')


@sku.command()
async def madmachines(ctx):
    '''MAD MACHINES - £9.99'''
    await ctx.send('https://ptb.discord.com/store/skus/487272772393762826/mad-machines')


@sku.command()
async def avoidplus(ctx):
    '''Avoid Premium - £5.99'''
    await ctx.send('https://ptb.discord.com/store/skus/586603437299597333/avoid-premium')


@sku.command()
async def scpsl(ctx):
    '''SCP: Secret Laboratory - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/420676877766623232/scp-secret-laboratory')


@sku.command()
async def sandboxes(ctx):
    '''SandBoxes - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/519249930611589141/sandboxes')


@sku.command()
async def forestir(ctx):
    '''Forestir - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/554072621000556584/forestir')


@sku.command()
async def ihbad(ctx):
    '''Its Hard Being A Dog - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/565994833953554432/it-s-hard-being-a-dog')


@sku.command()
async def avoid(ctx):
    '''Avoid - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/601864041731719189/avoid')


@sku.command()
async def hagwwii(ctx):
    '''Heroes & Generals WWII - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/550277544025522176/heroes-generals-wwii')


@dlc.command()
async def hagwwii(ctx):
    '''Heroes & Generals WWII DLC - `o.store sku hagwwii`'''
    await ctx.send(
        'https://ptb.discord.com/store/skus/558205987434266625/1200-gold\nhttps://ptb.discord.com/store/skus/565438968167137280/2200-gold\nhttps://ptb.discord.com/store/skus/557535890285658122/4800-gold\nhttps://ptb.discord.com/store/skus/565441415270629376/13000-gold\nhttps://ptb.discord.com/store/skus/565460799355617289/30000-gold')


@sku.command()
async def soma(ctx):
    '''SOMA - £28.99'''
    await ctx.send('https://ptb.discord.com/store/skus/489230107093893120/soma')


@sku.command()
async def bannersaga(ctx):
    '''Banner Saga 3 - £23.99'''
    await ctx.send('https://ptb.discord.com/store/skus/472483394085715979/banner-saga-3')


@sku.command()
async def starsonata(ctx):
    '''Star Sonata 2 - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/459415040227803141/star-sonata-2')


@sku.command()
async def taopepel(ctx):
    '''The Adventures of PepeL - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/554072366213234729/the-adventures-of-pepel')


@sku.command()
async def jumplats(ctx):
    '''Jumplats - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/618864578545319956/jumplats')


@sku.command()
async def lftb(ctx):
    '''Light From The Butt - Free'''
    await ctx.send('https://ptb.discord.com/store/skus/594073512906588179/light-from-the-butt')


@sku.command()
async def metald(ctx):
    '''Metal's Dungeon - £1.99'''
    await ctx.send('https://ptb.discord.com/store/skus/557494559257526272/metal-s-dungeon')


@sku.command()
async def mofanima(ctx):
    '''Masters of Anima - £19.98'''
    await ctx.send('https://ptb.discord.com/store/skus/492418279717994505/masters-of-anima')


@sku.command()
async def parkasaurus(ctx):
    '''Parkasaurus - £19.99'''
    await ctx.send('https://ptb.discord.com/store/skus/508008071411400724/parkasaurus')


@sku.command()
async def sinnersfr(ctx):
    '''Sinner: Sacrifice for Redemption - £18.99'''
    await ctx.send('https://ptb.discord.com/store/skus/489184797936058380/sinner-sacrifice-for-redemption')


@sku.command()
async def subnautica(ctx):
    '''Subnautica - £24.99'''
    await ctx.send('https://ptb.discord.com/store/skus/489926636943441932/subnautica')


@sku.command()
async def poe2df(ctx):
    '''Pillars of Eternity II: Deadfire - £48.99'''
    await ctx.send('https://ptb.discord.com/store/skus/466696214818193408/pillars-of-eternity-ii-deadfire')


@sku.command()
async def subnautica2(ctx):
    '''Subnautica: Below Zero - £24.99'''
    await ctx.send('https://ptb.discord.com/store/skus/535869836748783616/subnautica-below-zero')


@sku.command()
async def callofc(ctx):
    '''Call of Cthulu - £39.99'''
    await ctx.send('https://ptb.discord.com/store/skus/503982482664849408/call-of-cthulhu-r')


@sku.command()
async def amnesiatdd(ctx):
    '''Amnesia: The Dark Descent - £19.99'''
    await ctx.send('https://ptb.discord.com/store/skus/489229235509002261/amnesia-the-dark-descent')


@sku.command()
async def hexrun(ctx):
    '''Hex! Run - £0.99 (-50%)'''
    await ctx.send('https://ptb.discord.com/store/skus/598419143661846528/hex-run')


@dlc.command()
async def hexrun(ctx):
    '''Hex! Run DLC - `o.store sku hexrun`'''
    await ctx.send(
        'https://ptb.discord.com/store/skus/691033745024614402/hex-run-gold-edition\nhttps://ptb.discord.com/store/skus/691246598532890725/hex-run-through-the-portal')


'''Moderation commands'''


# Guild number
# Mute Command
# Unmute Command

@bot.command(aliases=["clear", "midou", "delete"])  # Bulk deletes messages
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=20):
    '''Purge [amount] of messages'''
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | {amount} messages have been deleted - {ctx.author}')
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages just deleted. :+1:')


@bot.command(aliases=["clearuser"])  # Bulk deletes messages
@commands.has_permissions(manage_messages=True)
async def purgeuser(ctx, user: typing.Optional[discord.User], amount: int):
    '''Purge [amount] of messages'''
    # if amount >= 1000:
    #    return await ctx.send('You can not purge more than 1000 messages!')
    if user != None:
        def check(message):
            return message.author.id == user.id
    else:
        def check(message):
            return True

    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | {amount} messages have been deleted - {ctx.author}')
    await ctx.channel.purge(limit=amount, check=check)
    await ctx.send(f'{amount} messages just deleted. :+1:')


@bot.command()  # Kicks a mentioned member
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    '''Kick a specified member'''
    await member.kick()
    await ctx.send(f'{member} was kicked')
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | {member} has been kicked - {ctx.author}')


@bot.command()  # Bans a mentioned member
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    '''Ban a specified member'''
    await member.ban()
    await ctx.send(f'{member} was banned')
    currentDT = datetime.datetime.now()
    print(f'({currentDT}) {ctx.guild} | {member} has just been banned - {ctx.author}')


@bot.command()  # Unbans a tagged member
@commands.has_permissions(ban_members=True, kick_members=True)
async def unban(ctx, *, member):
    '''Unbans a specified member'''
    currentDT = datetime.datetime.now()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} was unbanned')
            print(f'({currentDT}) {ctx.guild} | {user.name}#{user.discriminator} has been unbanned - {ctx.author}')
            return


@bot.command(aliases=["poweroff", "off", "powerdown"])  # Shuts down the bot
@commands.check(is_it_me)
async def shutdown(ctx):
    '''Shut down the bot'''
    await ctx.send('https://text2image.com/user_images/202102/text2image_J6510767_20210213_81132.png')
    currentDT = datetime.datetime.now()
    print('-----------------------------------------------')
    print(f'Shutdown triggered - {ctx.guild}')
    print(f'Log ended at: {currentDT}')
    print('-----------------------------------------------')
    await bot.change_presence(activity=discord.Game('Brrrrrrr ● o.help'), status=discord.Status.invisible)
    #await lavalink.close()
    sys.exit()


'''Random commands'''

#@bot.command(aliases=["strangerchat", "support", "secret", "anonymous", "anon", "whisper"])
#async def confess(ctx, *args):
#    await ctx.channel.purge(limit=1)
#    await ctx.send(" ".join(args))

# - Needs group and "answer" command
# - Urgencies so group in group
# - response custom colour

#async def say(ctx, *args):
#    await ctx.channel.purge(limit=1)
#    await ctx.send(" ".join(args))

@bot.group(invoke_without_command=True)
async def confess(ctx):
    await ctx.channel.purge(limit=1)
@confess.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(color=0xEB6F59)
    embed.set_author(name="Confession Help Command", icon_url="https://oscie.tk/assets/logo.png", description="Anonymously confess to something or get advice for something, without anyone seeing your name or profile picture")
    embed.add_field(title="Giving Support", value="o.confess support [advice]\n\nThe support command is used to give people advice based on their confession anonymously, no matter the urgency. This exists so if you want to give advice that you dont really feel comfortable giving out normally", inline=False)
    embed.add_field(title="Getting Support: Neutral", value="o.confess neutral [confession]\n\nThis is a command you can use if you don't feel comfortable confessing something under your name, but want people to know it. This doesnt always have to need advice.", inline=False)
    embed.add_field(title="Getting Support: Minor", value="o.confess neutral [confession]\n\nThis is a command you can use if you need advice, but not so bad that its more important than the rest. If its something small, use this. If you dont want advice, consider `o.confess neutral`.", inline=False)
    embed.add_field(title="Getting Support: Urgent", value="o.confess major [confession]\n\nThis is for really important things that you really really need advice on. If you are in danger of any sorts, please contact the right people instead of saying here", inline=False)
    await ctx.channel.send(embed=embed)
@confess.command()
async def major(ctx, *args):
    '''    A major confession, that you really need advice on. Use this to respond to advice or start a chain.'''
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(color=0xEB6F59)
    embed.set_author(name="Anonymous Confession", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Confession", value=(" ".join(args)))
    embed.add_field(name="Urgency", value="**Major**")
    await ctx.channel.send(embed=embed)
@confess.command()
async def minor(ctx, *args):
    '''    A minor confession, that you would like advice on, but not that important. Use this to respond to advice or start a chain.'''
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(color=0x9CE9FF)
    embed.set_author(name="Anonymous Confession", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Confession", value=(" ".join(args)))
    embed.add_field(name="Urgency", value="Minor")
    await ctx.channel.send(embed=embed)
@confess.command()
async def neutral(ctx, *args):
    '''    A neutral confession, that you may or may not want/need advice on. Use this to respond to advice or start a chain.'''
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(color=0x8CFFCF)
    embed.set_author(name="Anonymous Confession", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Confession", value=(" ".join(args)))
    embed.add_field(name="Urgency", value="Neutral")
    await ctx.channel.send(embed=embed)
@confess.command()
async def support(ctx, *args):
    '''    Used to give advice on confessions if needed. Use this to give advice or start a chain.'''
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(color=0xFF00D4)
    embed.set_author(name="Anonymous Advice", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Advice", value=(" ".join(args)))
    await ctx.channel.send(embed=embed)

@bot.command()
async def testembed(ctx, *, user: discord.Member = None):
    await ctx.send('testing embeds')
    embed = discord.Embed(color=0x00FF00)
    embed.set_author(name="test", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="title", value="testy lol", inline=False)
    embed.add_field(name="title 2", value="more testy testing??", inline=False)
    await ctx.channel.send(embed=embed)

@bot.command()
async def o(ctx):
    '''o.o'''
    await ctx.send('o.o')


@bot.command()  # Adds the 2 numbers
async def add(ctx, left: int, right: int):
    '''Add 2 numbers together'''
    await ctx.send(left + right)


@bot.command(aliases=["ryal"])  # Sends Ryaltopia mod link
async def ryaltopia(ctx):
    '''Ryaltopia mod'''
    await ctx.send('https://oscie.tk/ryaltopia')


@bot.command(aliases=["clock"])  # Sends the current time
async def time(ctx):
    '''Check the time'''
    currentDT = datetime.datetime.now()
    await ctx.send(currentDT)


@bot.command()  # Choose between multiple choices
async def choose(ctx, *choices: str):
    '''Chose between any amount of choices'''
    await ctx.send(random.choice(choices))


@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong! {0}s suck on that c#'.format(round(bot.latency, 3)))


@bot.command(aliases=["talk", "text"])
async def say(ctx, *args):
    await ctx.channel.purge(limit=1)
    await ctx.send(" ".join(args))


@bot.command(aliases=["rubbish", "max"])
async def trash(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/750623633151492177/813380044981927976/video0.mp4')


@bot.command(aliases=["akis", "akiswhite", "aches", "akis19", "akis_19"])
async def akisblack(ctx):
    '''Me when akisblack'''
    await ctx.send('<@457110625110327296>')
    await ctx.send('https://cdn.discordapp.com/attachments/718663888714989638/802794779871412294/makesweet2.gif')


'''Legacy Nintendo Homebrew'''


@bot.group(invoke_without_command=True)
async def lnh(ctx):
    await ctx.send(
        'These are commands specifically for the Guild: `Legacy Nintendo Homebrew//546723909081235471` If you are seeing this in LNH, use `o.help lnh` to see the Support commands for LNH. If you are not in LNH, please ignore this.')

@lnh.command()
async def invite(ctx):
    '''Legacy Nintendo Homebrew server invite'''
    await ctx.send('discord.gg/XQnNR9N')
@lnh.command()
async def link(ctx):
    '''How to copy links for idiots'''
    await ctx.send(
        'https://cdn.discordapp.com/attachments/546727695547891712/822805639990083637/2021-03-20_12-15-19.mp4')
@lnh.command()
async def aches(ctx):
    '''Toxicity of the Gaming Community - Aches is Gone | Bloody Blogs'''
    await ctx.send('https://bloodythorn.github.io/2021/02/28/toxicity-of-the-gaming-community.html')
@lnh.command()
async def nkit(ctx):
    '''Nkit Tools link'''
    await ctx.send('https://gbatemp.net/download/nkit.36157/')


'''eCDP Commands'''
@bot.group(invoke_without_command=True)
async def ecdp(ctx):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="ecdp info", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="eCDP Information", value="eCDP Discord Invite: https://discord.gg/3MkYyFnkqG\nGame Archive: https://archive.org/details/mcdonalds-japan-ecdp-rom-training-nintendo-ds-cartridge-dump\nSpeedrun Leaderboard: https://www.speedrun.com/mcdonalds_ecdp")
    embed.add_field(name="Current Guides", value="```o.ecdp foodsafety\no.ecdp fries\no.ecdp hashbrowns```")
    await ctx.send(embed=embed)

@ecdp.command()
async def foodsafety(ctx):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
    embed.add_field(name="Question Contains\n", value="3 Principles of food poisoning prevention\n\nCentimetres from the floor\n\nWhat temp should frozen products be\n\n10:1 Burger\n\nNot necessary to prevent secondary\n\nWhat temp should refrigerated items be\n\nNot correct hand wash\n\nWhat is cross-contamination\n\nWhat causes food safety compromisation\n\nWhat is not standard measure")
    embed.add_field(name="Answer Contains\n", value="Do not increase\n\n15cm\n\n-18°C\n\n69°C\n\nCheck Schedule\n\n4°C\n\nRub with arms crossed\n\nSecondary Pollution\n\nAll display items\n\n\nContact me when late")
    await ctx.send(embed=embed)
@ecdp.command()
async def fries(ctx):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
    embed.add_field(name="Question Contains\n", value="How many seconds do the next baskets\n\nIf potato is on floor, use [] to pick up\n\nWhen sprinkling salt on fries\n\nExpectations for potatoes\n\nUse special gloves, an apron and []\n\nHow many baskets should one bag\n\nHow long does it take to make potato\n\nChoose the six non-enemy oils\n\nWhere to store potato bags\n\nWhat is the temp of the fryer")
    embed.add_field(name="Answer Contains\n", value="30 Seconds\n\nLarge Tongs\n\nTriple Arch\n\nTexture\n\nFace Shield\n\n4\n\n2:55+5\n\nNutrients `(3 Chars)`\n\nPotato Freezer\n\n168°C")
    await ctx.send(embed=embed)
@ecdp.command()
async def hashbrowns(ctx):
    embed = discord.Embed(color=0x7289DA)
    embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
    embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
    embed.add_field(name="Question Contains\n", value="What do you use for packaging\n\nWhat do customers expect\n\nHow long do hashbrowns go in the fryer\n\nHow long do you drain the oil\n\nWhat temperature is the fryer\n\nWhat is the holding time of hashbrowns\n\nChoose the six non-enemy oils\n\nWhat do you use to clean the station\n\nWhat does it mean to remove the fried\n\nHow many can be placed in the basket")
    embed.add_field(name="Answer Contains\n", value="Tongs\n\nGolden Brown\n\n2:45+5\n\n5-10s\n\n182°C\n\n10\n\nSkimming\n\nDry Wiper\n\nSkimming\n\n8 Pieces")
    await ctx.send(embed=embed)
    

'''Bot events'''

'''@bot.event()
async def on_message(message):
    if message.channel.type == "private":
        return message.channel.send('This is a DM. I only work in servers')'''

# Member count command

'''Bot Token'''

'''Special Thanks:'''
# @Hentai#8349 - Help with Clear command
