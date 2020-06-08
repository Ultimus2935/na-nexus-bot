import discord
from discord.ext import commands

class CommandTesting(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog: CommandTesting, is online")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "~slowmode add":
            message.channel.slowmode_delay = 10
            await message.channel.send(f":ballot_box_with_check: Slowmode of 10s seconds has been added to #{message.channel.name} on_message relpy")

        elif message.content == "~slowmode remove":
            message.channel.slowmode_delay = 0
            await message.channel.send(f":ballot_box_with_check: Slowmode has been removed from #{message.channel.name}")

    @commands.command()
    async def testbot(self, ctx):
        await ctx.send("BOT IS ONLINE AND WORKING!!")

    # @commands.command()
    # async def slowmode(self, ctx, type, amount=None):
    #     if type == "add":
    #         ctx.message.channel.slowmode_delay = amount
    #         await ctx.send(f":ballot_box_with_check: Slowmode of {amount} seconds has been added to #{ctx.channel.name}")

    #     elif type == "remove":
    #         ctx.message.channel.slowmode_delay = 0
    #         await ctx.send(f":ballot_box_with_check: Slowmode has been removed from #{ctx.channel.name}")


def setup(client):
    client.add_cog(CommandTesting(client))