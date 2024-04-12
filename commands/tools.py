import discord
from discord.ext import commands
import random
import asyncio
from colorama import Fore, Style, Back

import config_selfbot
import fr_en

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum*100000,maximum*100000) / 100000
    return cooldown

class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dmall(self, ctx):
        message_split = ctx.message.content.split()
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        try:
            message_split[1]
        except Exception:
            await ctx.message.edit(fr_en.raid_dm_all_fail[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        friends = self.bot.friends

        print(Fore.YELLOW + "=========DM ALL=========", Style.RESET_ALL)
        print(Fore.BLUE + f"Friends Counter: {len(friends)} | Message:\n{dmall_content}", Style.RESET_ALL)

        await ctx.message.edit(fr_en.raid_dm_all[config_selfbot.lang])

        for friend in friends:
            try:
                await friend.user.send(dmall_content)
                print(Fore.GREEN + "[+]", Fore.LIGHTGREEN_EX + "@{friend.user.name}({friend.user.id})", Style.RESET_ALL)
                await asyncio.sleep(random_cooldown(0.5, 2))
            except discord.Forbidden:
                print(Fore.RED + "[-]", Fore.LIGHTRED_EX + "@{friend.user.name}({friend.user.id})", Style.RESET_ALL)
            except discord.CaptchaRequired:
                print(Fore.RED + "[!]", Fore.LIGHTRED_EX + "Captcha Required!", Style.RESET_ALL)
                print("========================")
                await ctx.message.edit(fr_en.raid_dm_all_captcha[config_selfbot.lang])
                await asyncio.sleep(config_selfbot.deltime)
                await ctx.message.delete()
                return
        
        print(Fore.YELLOW + "========================", Style.RESET_ALL)


        await ctx.message.edit(fr_en.raid_dm_all_success[config_selfbot.lang])
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

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