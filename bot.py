import random
import discord
from links import *

from datetime import datetime


intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

gender = {'male':[415028718910832652,'boyfriend'], 
          'female':[876888734690320445,'girlfriend'],
          'any':[415028718910832652,876888734690320445]}

sex = {
"Cute" : ['kiss_lips','kiss_face','kiss_neck','grope_boob','grope_ass','hug','cuddle'],
"Foreplay" : ['suck_dick','rub_pussy','jerk_dick'],
"Fuck" : ['fuck_doggy','fuck_stand','fuck_bed','ride_dick'],
"BDSM" : ['handcuff','deepthroat','whipping','choking'],
"Climax":['cum_mouth','cum_face','cum_boobs','cum_pussy','creampiee']
}


result = ""
for i in sex:
    result+="---"+i+"---"+"\n"
    for x in sex[i]:
        result+="!"+x+"\n"
    result+="\n"
@client.event
async def on_ready():
    now = datetime.now()
    print(str(now)+": Bot online")
    channel_genral = client.get_channel(959872101869826079)
    await channel_genral.send(str(now)+": Bot Online")
# Setting `Playing ` status
    await client.change_presence(activity=discord.Game(name="with your heart ❤️"))

# Setting `Streaming ` status
    #await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def on_message(message):
  def inter (gender,interaction,gif,body):
    if message.author.id in gender:
      arr = message.content.split()
      user = client.get_user(int(arr[1][-19:-1]))
      embed= discord.Embed(title=f"{message.author.name} "+interaction+f" {user.name} "+body+" 👩‍❤️‍💋‍👨")
      g = random.choice(gif)
      print (g)
      embed.set_image(url=g)
      return embed
    else:
      embed= discord.Embed(title=f"Only your "+gender[1]+" can do that to you silly!")
      return embed
  if message.channel.id == 960251737602658305:
      channel_genral = client.get_channel(954059340006965320)
      await channel_genral.send(message.content)
  if message.content.startswith("!list"):
    embed= discord.Embed(title="Sex List", description=result)
    await message.channel.send(embed=embed)
  if message.content.startswith("!"+sex['Cute'][0]):
    await message.channel.send(embed=inter(gender['any'],'kissed',kiss_lips,''''s lips'''))
  if message.content.startswith("!"+sex['Cute'][1]):
    await message.channel.send(embed=inter(gender['any'],'kissed',kiss_face,''''s face'''))
  if message.content.startswith("!"+sex['Cute'][2]):
    await message.channel.send(embed=inter(gender['any'],'kissed',kiss_neck,''''s neck'''))
  if message.content.startswith("!"+sex['Cute'][3]):
    await message.channel.send(embed=inter(gender['male'],'groped',grope_boob,''''s boobs'''))
  if message.content.startswith("!"+sex['Cute'][4]):
    await message.channel.send(embed=inter(gender['male'],'groped',grope_ass,''''s ass'''))
  if message.content.startswith("!"+sex['Cute'][5]):
    await message.channel.send(embed=inter(gender['any'],'hugged',hug,''))
  if message.content.startswith("!"+sex['Cute'][6]):
    await message.channel.send(embed=inter(gender['any'],'cuddled',cuddle,''))
  if message.content.startswith("!"+sex['Foreplay'][0]):
    await message.channel.send(embed=inter(gender['female'],'sucked',suck_dick,''''s dick'''))
  if message.content.startswith("!"+sex['Foreplay'][1]):
    await message.channel.send(embed=inter(gender['male'],'rubed/fingered',rub_pussy,''''s pussy'''))
  if message.content.startswith("!"+sex['Foreplay'][2]):
    await message.channel.send(embed=inter(gender['female'],'jerked',jerk_dick,''''s dick'''))
  if message.content.startswith("!"+sex['Fuck'][0]):
    await message.channel.send(embed=inter(gender['male'],'fucked',fuck_doggy,'like a dog!'))
  if message.content.startswith("!"+sex['Fuck'][1]):
    await message.channel.send(embed=inter(gender['male'],'fucked',fuck_stand,''))
  if message.content.startswith("!"+sex['Fuck'][2]):
    await message.channel.send(embed=inter(gender['male'],'fucked',fuck_bed,'passionately on bed'))
  if message.content.startswith("!"+sex['Fuck'][3]):
    await message.channel.send(embed=inter(gender['female'],'riding',ride_dick,''''s dick'''))
  if message.content.startswith("!"+sex['BDSM'][0]):
    await message.channel.send(embed=inter(gender['male'],'cuffed and fucked',handcuff,''))
  if message.content.startswith("!"+sex['BDSM'][1]):
    await message.channel.send(embed=inter(gender['female'],'deepthroating',deepthroat,''''s dick'''))
  if message.content.startswith("!"+sex['BDSM'][2]):
    await message.channel.send(embed=inter(gender['male'],'whipped',whipping,''''s ass'''))
  if message.content.startswith("!"+sex['BDSM'][3]):
    await message.channel.send(embed=inter(gender['male'],'choked',choking,''))
  if message.content.startswith("!"+sex['Climax'][0]):
    await message.channel.send(embed=inter(gender['male'],'came in',cum_mouth,''''s mouth'''))
  if message.content.startswith("!"+sex['Climax'][1]):
    await message.channel.send(embed=inter(gender['male'],'came on',cum_face,''''s face'''))
  if message.content.startswith("!"+sex['Climax'][2]):
    await message.channel.send(embed=inter(gender['male'],'came on',cum_boobs,''''s boobs'''))
  if message.content.startswith("!"+sex['Climax'][3]):
    await message.channel.send(embed=inter(gender['male'],'came inside',cum_pussy,''''s pussy'''))
  if message.content.startswith("!"+sex['Climax'][4]):
    await message.channel.send(embed=inter(gender['female'],'creampied on',creampie,''''s dick'''))
    

  
  
client.run('OTQzOTY5ODQ1MDM5NDg0OTc4.Yg6ybQ.L2I_Gh7T-4SWFUK4dwfWSdCeoes')
