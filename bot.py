import discord, boto3
from datetime import datetime

client = discord.Client()
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0e6ff57556852d6c2')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')
    channel_admin = client.get_channel(959872101869826079)
    await channel_admin.send(str(datetime.now())+": Bot Online [AWS]")


@client.event
async def on_message(message):
    if message.content.lower() == "stop":
        if turnOffInstance():
            await message.channel.send('AWS Instance stopping')
        else:
            await message.channel.send('Error stopping AWS Instance')
    elif message.content.lower() == "start":
        if turnOnInstance():
            await message.channel.send('AWS Instance starting')
        else:
            await message.channel.send('Error starting AWS Instance')
    elif message.content.lower() == "state":
        if getInstanceState():
            await message.channel.send('AWS Instance state is: ' + getInstanceState())
    elif message.content.lower() == "reboot":
        if rebootInstance():
            await message.channel.send('AWS Instance rebooting')
        else:
            await message.channel.send('Error rebooting AWS Instance')
    elif message.content.lower() == "test":
        await message.channel.send('Thanks, Jace. Helps alot.')

def turnOffInstance():
    try:
        instance.stop()
        return True
    except:
        return False

def turnOnInstance():
    try:
        instance.start()
        return True
    except:
        return False

def getInstanceState():
        return instance.state['Name']

def rebootInstance():
    try:
        instance.reboot()
        return True
    except:
        return False

client.run('OTQzOTY5ODQ1MDM5NDg0OTc4.Yg6ybQ.L2I_Gh7T-4SWFUK4dwfWSdCeoes')