from ntpath import join
import discord, boto3, time
from datetime import datetime
from discord.ext import tasks

client = discord.Client()
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0e6ff57556852d6c2')

start_time = time.time()
joined = 0
left = 0
started = 0
def get_ip():
    Myec2=boto3.client('ec2').describe_instances()
    while(Myec2['Reservations'][0]['Instances'][0]['State']['Name'] != 'running'):
        Myec2=boto3.client('ec2').describe_instances()
        print(Myec2['Reservations'][0]['Instances'][0]['State']['Name'])
    return str(Myec2['Reservations'][0]['Instances'][0]['PublicIpAddress'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')
    myLoop.start()
    channel_admin = client.get_channel(959872101869826079)
    await channel_admin.send(str(datetime.now())+": Bot Online [AWS]")

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    global started
    Myec2=boto3.client('ec2').describe_instances()
    channel_gen = client.get_channel(954059340006965320)
    if joined==left and time.time()-start_time>200 and Myec2['Reservations'][0]['Instances'][0]['State']['Name'] == 'running' and started ==1:
        channel_admin = client.get_channel(959872101869826079)
        await channel_admin.send('stop')
        time.sleep(10)
        if turnOffInstance():
            joined = 0
            left = 0
            started = 0
            embed= discord.Embed(title="Server Idle!", description="No Players Minecraft.\nServer will stop now.")
            await channel_gen.send(embed=embed)
        else:
            embed= discord.Embed(title="Error!", description="Error stopping the server")
            await channel_gen.send(embed=embed)
    else:
        print("Server not Idle "+str(time.time()-start_time))
        print("joined",joined)
        print("left",left)


@client.event
async def on_message(message):
    global start_time, joined, left, started
    if (message.content.lower().__contains__( "joined the game")):
        joined+=1
        start_time= time.time()
    elif (message.content.lower().__contains__( "left the game")):
        left+=1
        start_time= time.time()
    elif message.content.lower() == "!stop":
        channel_admin = client.get_channel(959872101869826079)
        await channel_admin.send('stop')
        time.sleep(10)
        if turnOffInstance():
            joined = 0
            left = 0
            started = 0
            embed= discord.Embed(title="Server Stopping!", description="Minecraft Server will stop now.")
            await message.channel.send(embed=embed)
        else:
            embed= discord.Embed(title="Error!", description="Error stopping the server")
            await message.channel.send(embed=embed)
    elif message.content.lower() == "!start":
        if turnOnInstance():
            embed= discord.Embed(title="Server Starting!", description="Minecraft Server will start in 2 mins\nIP: "+get_ip())
            start_time= time.time()
            joined = 0
            left = 0
            started = 1
            await message.channel.send(embed=embed)
        else:
            embed= discord.Embed(title="Error!", description="Error. Try again in few seconds.")
            await message.channel.send(embed=embed)
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