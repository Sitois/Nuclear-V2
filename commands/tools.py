import discord
from discord.ext import commands, tasks
import asyncio
from colorama import Fore, Style, Back

from utils import log, random_cooldown
import config_selfbot
import langs


class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_bump_task = None
        self.auto_bump_channel = None
        self.auto_bump_count = 0


    @commands.command()
    async def bump(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
            await ctx.message.edit(langs.tool_bump_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            await ctx.guild.fetch_member(302050872383242240)
        except discord.NotFound:
            await ctx.message.edit(langs.tool_bump_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            count = int(message_split[1])
        except Exception:
            await ctx.message.edit(f"{langs.spam_invalid[config_selfbot.lang]}!", delete_after=config_selfbot.deltime)
            return

        if count >= 100:
            await ctx.message.edit(langs.spam_too_much[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(f"{langs.tool_bump[config_selfbot.lang]} {count} {langs.tool_bump_two[config_selfbot.lang]}", delete_after=config_selfbot.deltime)

        command = [_ for _ in await ctx.channel.application_commands() if _.name == 'bump' and _.application_id == 302050872383242240][0]

        for i in range(count):
            await command.__call__(channel=ctx.channel)
            log.success(f"""Bumped {ctx.guild.name}({ctx.guild.id}) for the {i + 1} time.
Still need to bump {count - i - 1} time in {ctx.channel.name}({ctx.channel.id}).""")
            await asyncio.sleep(random_cooldown(7200, 7387))



    @commands.command()
    async def autobump(self, ctx: commands.Context):
        if self.auto_bump_task is not None and self.auto_bump_task.is_running():
            await ctx.message.edit("~~On auto bump ça !~~ C'est pas bon", delete_after=config_selfbot.deltime)
            return

        self.auto_bump_channel = ctx.channel
        self.auto_bump_task = self.auto_bump.start()
        await ctx.message.edit("On auto bump ça !", delete_after=config_selfbot.deltime)

    @tasks.loop(hours=2)
    async def auto_bump(self):
        if self.auto_bump_channel is not None:
            command = next((cmd for cmd in await self.auto_bump_channel.application_commands() if cmd.name == 'bump' and cmd.application_id == 302050872383242240), None)
            
            if command is not None:
                await command(self.auto_bump_channel)
                self.auto_bump_count += 1
                log.success(f"Auto-bumped {self.auto_bump_channel.guild.name}({self.auto_bump_channel.guild.id}) for the {self.auto_bump_count} time in {self.auto_bump_channel.name}({self.auto_bump_channel.id}).")

    @commands.command()
    async def stopautobump(self, ctx: commands.Context):
        if self.auto_bump_task is not None and self.auto_bump_task.is_running():
            self.auto_bump_task.cancel()
            self.auto_bump_task = None
            self.auto_bump_channel = None
            self.auto_bump_count = 0
            await ctx.message.edit("on stop tout !", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit("y'as rien a stopé...", delete_after=config_selfbot.deltime)




    @commands.command()
    async def dmall(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        try:
            message_split[1]
        except Exception:
            await ctx.message.edit(langs.raid_dm_all_fail[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        friends = self.bot.friends

        log.separate_text("DM ALL")

        print(f"{Fore.BLUE}Friends Counter: {len(friends)} | Message:\n{dmall_content}{Style.RESET_ALL}")

        await ctx.message.edit(langs.raid_dm_all[config_selfbot.lang])

        for friend in friends:
            try:
                await friend.user.send(dmall_content)
                log.success(f"@{friend.user.name}({friend.user.id})")
                await asyncio.sleep(random_cooldown(0.5, 2))
            except discord.Forbidden:
                log.fail(f"@{friend.user.name}({friend.user.id})")
            except discord.CaptchaRequired:
                log.important("Captcha Required!")
                log.separate("DM ALL")
                await ctx.message.edit(langs.raid_dm_all_captcha[config_selfbot.lang], delete_after=config_selfbot.deltime)
                return

        log.separate("DM ALL")


        await ctx.message.edit(langs.raid_dm_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def closealldm(self, ctx: commands.Context):

        await ctx.message.edit(langs.tool_close_dms[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.me.id == self.bot.user.id:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))
        
        await ctx.message.edit(langs.tool_close_dms_success[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def botclosedm(self, ctx: commands.Context):
        
        await ctx.message.edit(langs.tool_close_dms_bots[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.recipient.bot:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))

        await ctx.message.edit(langs.tool_close_dms_bots_success[config_selfbot.lang], delete_after=config_selfbot.deltime)
