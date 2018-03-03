from discord.ext.commands import Bot
import subprocess as sp
import shodan
import asyncio

bot = Bot(command_prefix="$")
token = 'INSERT KEY HERE' #THIS SHOULD PROBABLY JUST READ FROM A CONFIG FILE
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
    if message.content.upper().startswith(('WHY ')):
        yield from bot.send_file(message.channel, "images/bytyan.jpg")
    elif message.content.upper().startswith(('LOL ', 'HAHA ','ROFL ')):
        yield from bot.send_message(message.channel, content=":laughing:")
    elif 'CHEF' in message.content.upper():
        yield from bot.send_file(message.channel, "images/chef.jpg")
    yield from bot.process_commands(message)


@bot.command
@asyncio.coroutine
def log():
    yield from bot.logout()

@bot.command
@asyncio.coroutine
def r2d2():
    yield from bot.say("https://www.youtube.com/watch?v=Uj1ykZWtPYI")


@bot.command(name = 'sayshit')
@asyncio.coroutine
def sayshit():
    yield from bot.say("Shit!")

@bot.command
@asyncio.coroutine
def clear():
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")
    yield from bot.say("CLEARING")
    yield from bot.upload("images/project.jpg")


@bot.command
@asyncio.coroutine
def shodansearch(searchTerm):
    SHODAN_API_KEY = 'INSERT KEY HERE' #THIS SHOULD PROBABLY JUST READ FROM A CONFIG FILE
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
