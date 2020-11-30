
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('!도움')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!문상') or message.content.startswith('빈센아 문상'):
        a = random.randint(2100, 3800)
        b = random.randint(1000, 9999)
        b2 = random.randint(1000, 9999)
        c = random.randint(100000,999999)
        TICKETembed = discord.Embed(title='문상 생성기', description=str(a) + '-' + str(b) + '-' + str(b2) + '-' + str(c))
        await message.channel.send(embed=TICKETembed)


client.run(os.environ['token'])
