from discord.ext import commands
import asyncio
import os
import urllib.request
from utils import log, lang, generate_random_string, random_cooldown
import config_selfbot


class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.is_spamming: bool = False

    @commands.command()
    async def kickall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
            await ctx.message.edit(lang.text('raid_in_process'))

            log.separate_text("KICK ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.kick(reason=f"{config_selfbot.kick_reason} {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id}")
                    await asyncio.sleep(random_cooldown(0.4, 1.1))

            log.separate("KICK ALL")

            await ctx.message.edit(lang.text('raid_kick_all_success'), delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(lang.text('raid_error_permisssion'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def banall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.ban_members:
            members = ctx.guild.members

            await ctx.message.edit(lang.text('raid_in_process'))

            log.separate_text("BAN ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.ban(reason=f"{config_selfbot.ban_reason}. {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id}")
                    await asyncio.sleep(random_cooldown(0.4, 1.1))

            log.separate("BAN ALL")

            await ctx.message.edit(lang.text('raid_ban_all_success'), delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(lang.text('raid_error_permisssion'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def spam(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

        try:
            count = int(message_split[1]) - 1
        except Exception:
            await ctx.message.edit(f"{lang.text('spam_invalid')}!", delete_after=config_selfbot.deltime)
            return
        
        if count >= 100:
            await ctx.message.edit(lang.text('spam_too_much'), delete_after=config_selfbot.deltime)
            return

        try:
            message_split[2]
        except Exception:
            await ctx.message.edit(lang.text('raid_dm_all_fail'), delete_after=config_selfbot.deltime)
            return

        if not self.is_spamming:
            self.is_spamming = True

            await ctx.message.edit(content)

            for i in range(count):
                await ctx.channel.send(content)
                await asyncio.sleep(random_cooldown(0.4, 1.2))
            self.is_spamming = False
        else:
            await ctx.message.edit(lang.text('spam_cooldown'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def flood(self, ctx: commands.Context):
        flood_spam = '_ _\n' * 44
        await ctx.message.edit(flood_spam)
        for i in range(2):
            await ctx.channel.send(flood_spam)
            await asyncio.sleep(0.5)
    @commands.command()
    async def nuke(self, ctx: commands.Context):
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        for role in guild.roles:
            if role.name != "@everyone":
                await role.delete()
	
