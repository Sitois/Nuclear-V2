import discord
from discord.ext import commands
from colorama import Fore, Style, Back

import asyncio

import config_selfbot
from utils import log, Lang, random_cooldown

lang = Lang(path=r".\translations",
            default_language='en_US')

class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def bump(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
            await ctx.message.edit(lang.text('tool_bump_not_found'), delete_after=config_selfbot.deltime)
            return

        try:
            await ctx.guild.fetch_member(302050872383242240)
        except discord.NotFound:
            await ctx.message.edit(lang.text('tool_bump_not_found'), delete_after=config_selfbot.deltime)
            return

        try:
            count = int(message_split[1])
        except Exception:
            await ctx.message.edit(f"{lang.text('spam_invalid')}!", delete_after=config_selfbot.deltime)
            return

        if count >= 100:
            await ctx.message.edit(lang.text('spam_too_much'), delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(f"{lang.text('tool_bump')} {count} {lang.text('tool_bump_two')}", delete_after=config_selfbot.deltime)

        # Get the /bump object, to trigger it in the loop.
        command = [_ for _ in await ctx.channel.application_commands() if _.name == 'bump' and _.application_id == 302050872383242240][0]

        for i in range(count):
            # Trigger /bump command
            await command.__call__(channel=ctx.channel)
            # Log it
            log.success(f"""{lang.text('tool_auto_bump')} {ctx.guild.name}({ctx.guild.id}) {lang.text('tool_auto_bump_two')} {i + 1} {lang.text('tool_auto_bump_three')}.
{lang.text('tool_auto_bump_four')} {count - i - 1} {lang.text('tool_auto_bump_five')} {ctx.channel.name}({ctx.channel.id}).""")
            # Wait for the next /bump trigger
            await asyncio.sleep(random_cooldown(7200, 7387))

    @commands.command()
    async def dmall(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        try:
            message_split[1]
        except Exception:
            await ctx.message.edit(lang.text('raid_dm_all_fail'), delete_after=config_selfbot.deltime)
            return

        friends = self.bot.friends

        log.separate_text("DM ALL")

        print(f"{Fore.BLUE}Friends Counter: {len(friends)} | Message:\n{dmall_content}{Style.RESET_ALL}")

        await ctx.message.edit(lang.text('raid_dm_all'))

        for friend in friends:
            try:
                await friend.user.send(dmall_content)
                log.success(f"@{friend.user.name}({friend.user.id})")
                await asyncio.sleep(random_cooldown(0.5, 2))
            except discord.Forbidden:
                log.fail(f"@{friend.user.name}({friend.user.id})")
            except discord.CaptchaRequired:
                log.alert("Captcha Required!")
                log.separate("DM ALL")
                await ctx.message.edit(lang.text('raid_dm_all_captcha'), delete_after=config_selfbot.deltime)
                return

        log.separate("DM ALL")


        await ctx.message.edit(lang.text('raid_dm_all_success'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def closealldm(self, ctx: commands.Context):

        await ctx.message.edit(lang.text('tool_close_dms'))

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.me.id == self.bot.user.id:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))
        
        await ctx.message.edit(lang.text('tool_close_dms_success'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def botclosedm(self, ctx: commands.Context):
        
        await ctx.message.edit(lang.text('tool_close_dms_bots'))

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.recipient.bot:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))

        await ctx.message.edit(lang.text('tool_close_dms_bots_success'), delete_after=config_selfbot.deltime)