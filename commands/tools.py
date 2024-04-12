import discord
from discord.ext import commands
import random
import asyncio

import config_selfbot
import fr_en

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum*100000,maximum*100000) / 100000
    return cooldown

class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def closealldm(self, ctx):

        await ctx.message.edit(fr_en.tool_close_dms[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.me.id == self.bot.user.id:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))
        
        await ctx.message.edit(fr_en.tool_close_dms_success[config_selfbot.lang])
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def botclosedm(self, ctx):
        
        await ctx.message.edit(fr_en.tool_close_dms_bots[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.recipient.bot:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))

        await ctx.message.edit(fr_en.tool_close_dms_bots_success[config_selfbot.lang])
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()