from discord.ext.commands import Bot
import subprocess as sp
import shodan

bot = Bot(command_prefix="$")
token = 'MjgzOTYxMjEwNjcwNDE1ODcz.C48rHQ.xNfyau3G7vbBGTdPN3JnO8nK8WY'
searchTerm = str()
numResults = int()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith(('why', 'Why')):
        await bot.send_file(message.channel, "images/bytyan.jpg")
    elif message.content.startswith(('lol', 'LOL', 'Lol')):
        await bot.send_message(message.channel, content=":laughing:")
    await bot.process_commands(message)

@bot.command()
async def log():
    await bot.logout()

@bot.command()
async def r2d2():
    await bot.say("https://www.youtube.com/watch?v=Uj1ykZWtPYI")

@bot.command()
async def sayshit():
    await bot.say("Shit!")
    
@bot.command()
async def clear():
    await bot.upload("images/project.jpg")
    await bot.say("CLEARING")
    await bot.upload("images/project.jpg")
    await bot.say("CLEARING")
    await bot.upload("images/project.jpg")
    await bot.say("CLEARING")
    await bot.upload("images/project.jpg")

@bot.command()
async def shodansearch(searchTerm):
    SHODAN_API_KEY = 'EVpPLuV9Sa46y1niuQxNU63niDmNB8ne'
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.search(searchTerm)
    i = 0

    await bot.upload("images/logo.png")

    for result in results['matches'][:5]:
        i = i + 1
        ipInfo = result['ip_str']
        osData = result['os']
        hostnames = result['hostnames']
        hostinfo = api.host(result['ip_str'])

        await bot.say("Result %s of 5" % i)
        await bot.say("IPinfo: %s" % ipInfo)
        await bot.say("Hostname: %s" % hostnames)
        await bot.say("OS: %s" % osData)
        await bot.say(("Open Ports: %s" % str(hostinfo['ports'])))
        await bot.say("-------------\n")

bot.run(token)