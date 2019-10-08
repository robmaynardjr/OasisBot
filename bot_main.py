import immunio.start
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from configparser import ConfigParser
import codecs
import subprocess as sp
import shodan
import flippy
import asyncio #probably unnecessary

parser = ConfigParser()
f = flippy.Flippy()
with codecs.open('./config.cfg', 'r', encoding='utf-8') as conf: 
    parser.read_file('./config.cfg')

oasisbot = Bot(command_prefix="$")
token = parser.get('AUTH', 'discord')
searchTerm = str()
numResults = int()

@oasisbot.event
async def on_ready(oasisbot):
    print('Logged in as')
    print(oasisbot.user.name)
    print(oasisbot.user.id)
    print('------')

@oasisbot.command()
async def makeMeme(oasisbot, template, text0, text1):
    imgflipUser = parser.get('AUTH', 'imgflipUser')
    imgflipPass = parser.get('AUTH', 'imgflipPass')
    memeIds = {'mocking':102156234, 'doesnotsimply':61579, 'leo':5496396}
    meme = f.genMeme(memeIds[template], imgflipUser, imgflipPass, text0, text1)
    await oasisbot.send(meme)
    #genMeme(template_id, username, password, text0, text1, font="impact"):

@oasisbot.command()
async def clear(oasisbot):
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")


@oasisbot.command()
async def shodansearch(oasisbot, searchTerm):
    SHODAN_API_KEY = parser.get('AUTH', 'shodan')
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.search(searchTerm)
    i = 0

    
    await oasisbot.send(file=discord.File('images/logo.png'))

    for result in results['matches'][:5]:
        i = i + 1
        ipInfo = result['ip_str']
        osData = result['os']
        hostnames = result['hostnames']
        hostinfo = api.host(result['ip_str'])

        await oasisbot.send("Result %s of 5\nIPinfo: %s\nHostname: %s\nOS: %s\nOpen Ports: %s\n-------------\n" % (i, ipInfo, hostnames, osData, (str(hostinfo['ports']))))


oasisbot.run(token)
