import discord, boto3, time
from datetime import datetime


client = discord.Client()
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0e6ff57556852d6c2')

def get_ip():
    Myec2=boto3.client('ec2').describe_instances()
    for pythonins in Myec2['Reservations']:
        for printout in pythonins['Instances']:
            return str(printout['PublicIpAddress'])
            
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')
    channel_admin = client.get_channel(959872101869826079)
    await channel_admin.send(str(datetime.now())+": Bot Online [AWS]")


@client.event
async def on_message(message):
    if message.content.lower() == "!stop":
        channel_admin = client.get_channel(959872101869826079)
        await channel_admin.send('stop')
        time.sleep(10)
        if turnOffInstance():
            await message.channel.send('AWS Instance stopping')
        else:
            await message.channel.send('Error stopping AWS Instance')
    elif message.content.lower() == "!start":
        if turnOnInstance():
            embed= discord.Embed(title="Server Starting!", description="Minecraft Server will start in 2 mins\nIP: "+get_ip())
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('Error starting Minecraft Server')
    elif message.content.lower() == "!state":
        if getInstanceState():
            await message.channel.send('AWS Instance state is: ' + getInstanceState())
    elif message.content.lower() == "!reboot":
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

client.run('NzkyNDI2NTkyNDY1ODQ2Mjky.X-dixg.H4islCpSibQF9VrYbGI93gQRJEE')