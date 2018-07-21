import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
# import traceback
import platform
import sys
import os
import random
import requests
import urllib.request
import json
import time
import datetime
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

now = datetime.datetime.now()
diff = datetime.datetime(now.year, 12, 25) - \
    datetime.datetime.today()  # Days until Christmas

import logging
from pyfiglet import figlet_format, FontNotFound


# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' Bulunamadı Tekrar Deneyin.")

else:
    import config  # config.py is required to run; found in the same directory.
##################################################################################


# This code logs all events including chat to discord.log. This file will be overwritten when the bot is restarted - rename the file if you want to keep it.

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# IMPORTANT - DO NOT TOUCH! Setup bot as "client", with description and prefix from config.py
client = Bot(description=config.des, command_prefix=config.pref)


# This message lets us know that the script is running correctly
print("Connecting...")


# Start bot and print status to console

@client.event
async def on_ready():
    print("Bot Hazır!")
    f = open('logo.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    print("Discord.py API version:", discord.__version__)
    print("Python versionu:", platform.python_version())
    print("Çalışıyor:", platform.system(),
          platform.release(), "(" + os.name + ")")
    print("Ad : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))
    print("Aktif Olan Server Sayısı " + str(len(client.servers)) + " servers.")
    print("")
    logger.info("Bot Başlatıldı.")

    # Set "playing" status
    if diff.days < 2:
        print('Mutlu Noeller!')
        await client.change_presence(game=discord.Game(name="Mutlu Noeller! <3"))
    else:
        await client.change_presence(game=discord.Game(name="Red-BOT By ZZMare | " + config.pref + "help |"))


# Default BlazeBot commands

#Bitiş

@client.command(pass_context=True, aliases=['remove', 'delete'])
async def sil(ctx, number):
    """Kanaldan Mesaj Siler"""
    try:
        if ctx.message.author.server_permissions.administrator:
            mgs = []  # Empty list to put all the messages in the log
            # Converting the amount of messages to delete to an integer
            number = int(number)
            async for x in client.logs_from(ctx.message.channel, limit=number):
                mgs.append(x)
            await client.delete_messages(mgs)
            print("Silindi {} mesaj.".format(number))
            logger.info("{} mesaj silindi".format(number))
        else:
            await client.say(config.err_mesg_permission)
    except:
        await client.say(config.err_mesg)


@client.command(pass_context=True)
async def roller(context):
    """Sunucundaki Rol(Yetki) Listesi."""

    roles = context.message.server.roles
    result = "**Sunucundaki Roller: **"
    for role in roles:
        result += role.name + ", "
    await client.say(result)

@client.command(pass_context=True)
async def saril(ctx, *, member: discord.Member = None):
    """Ona Kocaman Bir Sarıl <3"""
    try:
        if member is None:
            await client.say(ctx.message.author.mention + " Sarınıldı!")
        else:
            if member.id == ctx.message.author.id:
                await client.say(ctx.message.author.mention + " Kendine SArıldı!")
            else:
                await client.say(ctx.message.author.mention + " " +member.mention + "'a sarıldı ")

    except:
        await client.say(config.err_mesg)
#https://www.youtube.com/watch?v=6vdWciD304g
@client.command(pass_context=True, aliases=['ytdl_options, url, **kwargs'])
async def disko(url, *, ytdl_options=None, **kwargs):
    """Test"""
    try:
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
        await client.join_voice_channel(channel)
        player.start()
    except:
        await client.say(config.err_mesg)

@client.command(pass_context=True, aliases=['say'])
async def yazdir(ctx, *msg):
    """Botu Konuşturur"""
    try:
        say = ''.join(msg)
        await client.delete_message(ctx.message)
        return await client.say(say)
    except:
        await client.say(config.err_mesg)


@client.command(pass_context=True, aliases=['saytts'])
async def yazdirtts(ctx, *msg):
    """Botu TTS ile Konuşturur."""
    try:
        say = ' '.join(msg)
        await client.delete_message(ctx.message)
        return await client.say(say, tts=True)
    except:
        await client.say(config.err_mesg)


@client.command(aliases=["fancy"])
async def sekilli(*, text):
    """Şekilli Yazı Yazdırır Bota!"""
    try:

        def strip_non_ascii(string):
            """ASCII Karakterlerini Düzeltir."""
            stripped = (c for c in string if 0 < ord(c) < 127)
            return ''.join(stripped)

        text = strip_non_ascii(text)
        if len(text.strip()) < 1:
            return await self.client.say(":x: ASCII Karakterleri Lütfen!")
        output = ""
        for letter in text:
            if 65 <= ord(letter) <= 90:
                output += chr(ord(letter) + 119951)
            elif 97 <= ord(letter) <= 122:
                output += chr(ord(letter) + 119919)
            elif letter == " ":
                output += " "
        await client.say(output)

    except:
        await client.say(config.err_mesg)


@client.command()
async def buyukyazi(*, text):
    """Yazıları Büyütür."""
    try:
        await client.say("```fix\n" + figlet_format(text, font="big") + "```")
    except:
        await client.say(config.err_mesg)

# Bot Oyun Değiştirme
#@client.command(pass_context=True, aliases=['game', 'presence'])
#async def setgame(ctx, *args):
    #"""Sets the 'Playing' status."""
    #try:
        #if ctx.message.author.server_permissions.administrator:
           # setgame = ' '.join(args)
            #await client.change_presence(game=discord.Game(name=setgame))
           # await client.say(":ballot_box_with_check: Oyun Ayarlandı: `" + setgame + "`")
           # print("Oyun Ayarlandı: `" + setgame + "`")
       # else:
        #    await client.say(config.err_mesg_permission)
    #except:
    #    await client.say(config.err_mesg)


@client.command()
async def serverler():
    """Aktif Sunucu Sayısı."""
    try:
        await client.say("Currently active on " + str(len(client.servers)) + " servers.")
        print("Currently active on " + str(len(client.servers)) + " servers.")
    except:
        await client.say(config.err_mesg)


#@client.command()
#async def botplatform():
    #"""Shows what OS the bot is running on."""
   # try:
        #await client.say("The bot is currently running on: ```" + str(platform.platform()) + "```")
    #except:
        #await client.say(config.err_mesg)



#@client.command(pass_context=True)
#async def serverlist(ctx):
    #"""List the servers that the bot is active on."""
    #x = ', '.join([str(server) for server in client.servers])
    #y = len(client.servers)
    #print("Server list: " + x)
    #if y > 40:
        #embed = discord.Embed(title="Suan Aktif Olduğu Sunucu sayısı " + str(y) + " Gosteriliyor:", description=config.err_mesg + "```json\n40 Sunucudan Fazla Gösterilemez!```", color=0xFFFFF)
        r#eturn await client.say(embed=embed)
    #elif y < 40:
        #embed = discord.Embed(title="Suan Aktif Olduğu Sunucu sayısı " + str(y) + " Gosteriliyor:", description="```json\n" + x + "```", color=0xFFFFF)
        #return await client.say(embed=embed)


@client.command(pass_context=True)
async def banlananlar(ctx):
    """Banlananları Gösterir."""
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title="Banlanan Kişiler", description=x, colour=0xFFFFF)
    return await client.say(embed=embed)


@client.command(pass_context=True, aliases=['user'])
async def bilgi(ctx, user: discord.Member):
    """Bilgilerini Gösterir."""
    try:
        await client.say("`Kullanıcı Adın: {}`".format(user.name))
        await client.say("`The user's status is: {}`".format(user.status))
        await client.say("`The user's highest role is: {}`".format(user.top_role))
        await client.say("`The user joined at: {}`".format(user.joined_at))

    except:
        await client.say(config.err_mesg)



@client.command(pass_context=True)
async def ping(ctx):
    """Gecikmeni Kontrol Ede."""
    try:
        pingtime = time.time()
        pingms = await client.say("*P I N G L E N D I N...*")
        ping = (time.time() - pingtime) * 1000
        await client.edit_message(pingms, "**Bam!** :ping_pong: Pingin `%dms`" % ping)
        print("Bot Pinglendi %dms." % ping)
        logger.info("Bot Pinglendi %dms." % ping)
    except:
        await client.say(config.err_mesg)


# Choose a random insult from the list in config.py
@client.command(pass_context=True)
async def acikla(ctx):
    """Senin Hakkında Birşeyler Söyler."""
    await client.say(ctx.message.author.mention + " " + random.choice(config.answers))  #Konsoldan Ayarlanılabilir


#@client.command(aliases=['ud'])
#async def urban(*msg):
   # """Searches on the Urban Dictionary."""
   # try:
     #   word = ' '.join(msg)
     #   api = "http://api.urbandictionary.com/v0/define"
     #   # Send request to the Urban Dictionary API and grab info
      #  response = requests.get(api, params=[("term", word)]).json()
      #  embed = discord.Embed(description="No results found!", colour=0xFF0000)
      #  if len(response["list"]) == 0:
      #      return await client.say(embed=embed)
        # Add results to the embed
      #  embed = discord.Embed(title="Word", description=word, colour=embed.colour)
      #  embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
      #  embed.add_field(name="Examples:", value=response['list'][0]["example"])
      #  embed.set_footer(text="Tags: " + ', '.join(response['tags']))

     #   await client.say(embed=embed)

   # except:
        #await client.say(config.err_mesg)


@client.command(pass_context=True, aliases=['ytid'])
async def youtubeid(ctx, *, channelid):
    """Kanalın ID sinden Kanalın Bilgilerini Gösterir."""
    try:
        # Make requests to YouTube API and grab info
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelid + "&key=" + config.key).read()
        logger.info("Making request to " + "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelid + "&key=" + config.key)
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        views = json.loads(data)["items"][0]["statistics"]["viewCount"]
        vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

        # Generate embed and say
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Abone:", value="{:,d}".format(int(subs)), inline=False)
        embed.add_field(name="İzlenme:", value="{:,d}".format(int(views)), inline=False)
        embed.add_field(name="Toplam Video:", value="{:,d}".format(int(vids)), inline=False)
        embed.set_thumbnail(url="https://s.ytimg.com/yts/mobile/img/apple-touch-icon-144x144-precomposed-vflopw1IA.png")
        embed.set_footer(text="Powered By ZZMare")
        await client.say(embed=embed)
    except:
        await client.say(config.err_mesg)



@client.command(pass_context=True, aliases=['ytstats'])
async def youtube(ctx, *, name):
    """Bir Kanalın Youtube Bilgilerini Gösterir."""
    try:
        # Make requests to YouTube API and grab info
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+config.key).read()
        logger.info("Making request to " + "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+config.key)
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        views = json.loads(data)["items"][0]["statistics"]["viewCount"]
        vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

        # Generate embed and say
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="Abone:", value="{:,d}".format(int(subs)), inline=False)
        embed.add_field(name="Izlenme:", value="{:,d}".format(int(views)), inline=False)
        embed.add_field(name="Toplam Video:", value="{:,d}".format(int(vids)), inline=False)
        embed.set_thumbnail(url="https://s.ytimg.com/yts/mobile/img/apple-touch-icon-144x144-precomposed-vflopw1IA.png")
        embed.set_footer(text="Powered by ZZMare")
        await client.say(embed=embed)
    except:
        await client.say(config.err_mesg)


#@client.command(pass_context=True)
#async def yukle():
    #"""Başlangıç Eklentilerini Başlatır."""
    #if __name__ == "__main__":  # Load startup extensions, specified in config.py
        #for extension in config.startup_extensions:
            #try:
               # client.load_extension(extension)
               # await client.say("Loaded extension: '" + extension + "'")
               # logger.info("Loaded extension '" + extension + "'")
           # except Exception as e:
              #  exc = '{}: {}'.format(type(e).__name__, e)
               # print('Failed to load extension {}\n{}'.format(extension, exc))
               # logger.info('Failed to load extension {}\n{}'.format(extension, exc))


#@client.command()
#async def devredisi(extension_name: str):
    #"""Eklentileri Devredışı bırakır."""
   # client.unload_extension(extension_name)
    #await client.say("{} unloaded.".format(extension_name))


@client.command(pass_context=True, aliases=['cls'])
async def temizle(ctx):
    """Discord Konsolunu Temizler"""
    if ctx.message.author.server_permissions.administrator:
        await client.say(":ballot_box_with_check: **Konsol Temizlendi!**")
        # checks if the script running on Windows or Unix
        os.system('cls' if os.name == 'nt' else 'clear')
        print("== Konsol Temizlendi! ==")
        print("")
    else:
        await client.say(err_mesg_permission)


# Christmas countdown!
@client.command(pass_context=True, aliases=['xmas', 'chrimbo'])
async def noel(ctx):
    """Yılbaşına Ne Kadar Var!"""
    await client.say("**" + str(diff.days) + "**" + " Kadar Gün Kaldı Az Kalmış! :christmas_tree:")  # Convert the 'diff' integer into a string and say the message



# It's reccommended that you keep the logout command disabled, especially running on multiple servers.

# @client.command(pass_context = True)
# async def logout(ctx):
##    """Disconnects the bot from all servers."""
# if ctx.message.author.server_permissions.administrator:
# await client.say("**Goodbye!** :zzz:")
##        print("Exiting bot...")
# await client.logout()
# else:
# await client.say(config.err_mesg_permission)


if __name__ == "__main__":  # Load startup extensions, specified in config.py
    for extension in config.startup_extensions:
        try:
            client.load_extension(extension)
            print("Eklenti Yüklendi '" + extension + "'")
            logger.info("Eklenti baslatildi '" + extension + "'")
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Eklenti Baslatilamadi {}\n{}'.format(extension, exc))
            logger.info('basarısız {}\n{}'.format(extension, exc))


# Read client token from "config.py" (which should be in the same directory as this file)
client.run(config.bbtoken)
