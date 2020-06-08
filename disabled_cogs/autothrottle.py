import asyncio
import random
import time

import discord
from discord.ext import commands, tasks

timeout = 10
message_limit = 7

class AutoThrottle(commands.Cog):
    
    def __init__ (self, client):
        print("cog was called!")
        self.client = client

        self.timer.start()

        self.msg_cnt = 0

    @tasks.loop(seconds=timeout)
    async def timer(self):
        await self.client.wait_until_ready()
        await asyncio.sleep(0.5)

        print(f"{self.msg_cnt} messages where sent in {timeout} seconds")

        if self.msg_cnt > message_limit:
            print("slowmo applied\n")

        self.msg_cnt = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True: return
        elif str(message.channel) == "Terminal": 
            self.msg_cnt += 1


def setup(client):
    
    client.add_cog(AutoThrottle(client))
