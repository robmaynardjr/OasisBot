from discord.ext.commands import Bot
from configparser import SafeConfigParser
import codecs
import subprocess as sp
import shodan
import asyncio

parser = SafeConfigParser()
with codecs.open('./config.cfg', 'r', encoding='utf-8') as conf:
    parser.readfp(conf)
    
bot = Bot(command_prefix="$")
token = parser.get('AUTH', 'discord')
searchTerm = str()
numResults = int()

@bot.async_event
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.async_event
def on_message(message):
    if 'WHY' in message.content.upper():
        yield from bot.send_file(message.channel, "images/bytyan.jpg")
    elif 'LOL' in message.content.upper():
        yield from bot.send_message(message.channel, content=":laughing:")
    elif 'CHEF' in message.content.upper():
        yield from bot.send_file(message.channel, "images/chef.jpg")
    yield from bot.process_commands(message)


@bot.command(name='log')
@asyncio.coroutine
def log():
    yield from bot.logout()

@bot.command(name='r2d2')
@asyncio.coroutine
def r2d2():
    yield from bot.say("https://www.youtube.com/watch?v=Uj1ykZWtPYI")


@bot.command(name = 'sayshit')
@asyncio.coroutine
def sayshit():
    yield from bot.say("Shit!")

@bot.command(name='clear')
@asyncio.coroutine
def clear():
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")


@bot.command(name='shodansearch')
@asyncio.coroutine
def shodansearch(searchTerm):
    SHODAN_API_KEY = parser.get('AUTH', 'shodan')
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.search(searchTerm)
    i = 0

    yield from bot.upload("images/logo.png")

    for result in results['matches'][:5]:
        i = i + 1
        ipInfo = result['ip_str']
        osData = result['os']
        hostnames = result['hostnames']
        hostinfo = api.host(result['ip_str'])

        yield from bot.say("Result %s of 5" % i)
        yield from bot.say("IPinfo: %s" % ipInfo)
        yield from bot.say("Hostname: %s" % hostnames)
        yield from bot.say("OS: %s" % osData)
        yield from bot.say(("Open Ports: %s" % str(hostinfo['ports'])))
        yield from bot.say("-------------\n")
        
bot.run(token)