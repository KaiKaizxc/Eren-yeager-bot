import discord 
import os 
from discord.ext import commands
import random

client= discord.Client()
client = commands.Bot(command_prefix="%")

#get quotes

quotes= ["If you win, you live. If you lose, you die. If you don't fight, you can't win!", "What is the point if those with the means and power do not fight?", "We’re born free. All of us. Free. Some don’t believe it, some try to take it away. To hell with them!", "There’s no time to figure out if this the right thing to do! Just move - Don’t try to keep your hands clean. That’s right, the world is cruel.", "I want to see and understand the world outside. I don't want to die inside these walls without knowing what's out there!", "If you think reality is just living comfortably and following your own whims, can you seriously dare to call yourself a soldier?", "Nothing can suppress a human's curiosity.", "On that day, mankind received a grim reminder. We lived in fear of the Titans, and were disgraced to live in these cages we called walls.", "I disposed of some dangerous beasts. Mere animals that just happened to resemble humans.", "Yeah, I know. We might not get out, but we’ll live as long as we can eat and sleep. But… We’re living like… Like livestock…", "Stupid? People who are content living like livestock are more stupid!" ]


len_quotes= len(quotes)

#when the bot is ready to be used
@client.event
async def on_ready():
  print("Rock and roll {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author ==client.user:
    return

#Commands of the eren yeager bot 
  if message.content.startswith("!commands"):
    await message.channel.send("Idiot, have you forgotten? Let me remind you the commands again: \n Type !stop and I will shout Fight! \n F words and I will shut you up \n To access commands: \n -Type %motivation and I will shout a random quote \n -Type %sugarbrownsugarpearl @(tag someone) is bobo \n -Type %hello (whatever you want me to say also)") 
  if message.content.startswith("!stop"):
    await message.channel.send("Fight!")
    
  if str(message.content).lower() =="lk":
    await message.channel.send("Captain lk is the best.")
    
  if message.content =="fuck":
    try: 
      await message.channel.purge(limit=1)
      await message.channel.send("That is not very nice")
    except:
      await message.channel.send("You are lucky you have a higher authority..")
  
  if "agree" in str(message.content).lower():
    await message.channel.send("Of course.")

  if str(message.content).lower() =="gen":
    await message.channel.send("gone?")

  if "gen" and "annoying" in message.content:
    await message.channel.send("Gen is annoying.")

  if "prof" in message.content:
    await message.channel.send("Kek")
    
  await client.process_commands(message)


  if "." in message.content:
    await message.channel.send("I know right.")
@client.command()
async def hello(ctx, *args):
  await ctx.send('{}'.format(' '.join(args)))

@client.command()
async def sugarbrownsugarpearl(ctx, arg2):
    await ctx.send("{} is bobo" .format(arg2))

@client.command()
async def motivation(ctx):
  await ctx.send(random.choice(quotes))
  
@client.command()
async def scouts(ctx):
  await ctx.send(f"There are currently {ctx.guild.member_count} scouts!")


#to run the bot

client.run(os.environ['Token'])

