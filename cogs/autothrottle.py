import asyncio
import random
import time

import discord
from discord.ext import commands, tasks

slowmode_delay = 10

timeout = 600
releaseTime = 60

message_limit = 100

class AutoThrottle(commands.Cog):
    
    def __init__ (self, client):
        self.client = client

        self.timer.start() # pylint: disable=no-member

        self.msg_cnt = 0
        self.messageChannel = None

    @tasks.loop(seconds=timeout)
    async def timer(self):
        if self.msg_cnt > message_limit:
            await self.messageChannel.send(":warning: **Slowmode has been enabeled!**")
            await self.messageChannel.edit(reason="Auto Throttled", slowmode_delay=slowmode_delay)

            await asyncio.sleep(releaseTime)

            await self.messageChannel.edit(reason="Auto Throttled", slowmode_delay=0)

        self.msg_cnt = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True: return
        
        elif str(message.channel) == "test-bot-here": 
            self.messageChannel = message.channel

            self.msg_cnt += 1


def setup(client):
    
    client.add_cog(AutoThrottle(client))
