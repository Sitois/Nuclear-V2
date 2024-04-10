import discord
from discord.ext import commands
import asyncio
import random
import string

import config_selfbot
import fr_en


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum*100000,maximum*100000) / 100000
    return cooldown

class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_spamming = False

    @commands.command()
    async def kickall(self, ctx):
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
            await ctx.message.edit(fr_en.raid_in_process[config_selfbot.lang])

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.kick(reason=f"ezzed by Nuclear lol. {generate_random_string(6)}")
                    await asyncio.sleep(random_cooldown(0.5, 2))
            
            await ctx.message.edit(fr_en.raid_kick_all_success[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(fr_en.raid_error_permisssion[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def banall(self, ctx):
        if ctx.author.guild_permissions.ban_members:
            members = ctx.guild.members

            await ctx.message.edit(fr_en.raid_in_process[config_selfbot.lang])
            
            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.ban(reason=f"ezzed by Nuclear lol. {generate_random_string(6)}")
                    await asyncio.sleep(random_cooldown(0.5, 2))
            
            await ctx.message.edit(fr_en.raid_ban_all_success[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(fr_en.raid_error_permisssion[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def dmall(self, ctx):
        message_split = ctx.message.content.split()
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        friends = self.bot.friends
        print(f"Message: {dmall_content}")

        await ctx.message.edit(fr_en.raid_dm_all[config_selfbot.lang])

        for friend in friends:
            try:
                await friend.user.send(dmall_content)
                print(f"[+] @{friend.user.name}({friend.user.id})")
                await asyncio.sleep(random_cooldown(0.5, 2))
            except discord.Forbidden:
                print(f"[-] @{friend.user.name}({friend.user.id})")

        await ctx.message.edit(fr_en.raid_dm_all_success[config_selfbot.lang])
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def spam(self, ctx):
        message_split = ctx.message.content.split()
        content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

        try:
            count = int(message_split[1]) - 1
        except Exception:
            await ctx.message.edit(f"{fr_en.spam_invalid[config_selfbot.lang]}!")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return
        
        if count >= 100:
            await ctx.message.edit(fr_en.spam_too_much[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        if not self.is_spamming:
            self.is_spamming = True

            await ctx.message.edit(content)

            for i in range(count):
                await ctx.channel.send(content)
                await asyncio.sleep(random_cooldown(0.5, 2))
            self.is_spamming = False
        else:
            await ctx.message.edit(fr_en.spam_cooldown[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def flood(self, ctx):
        flood_spam = """_ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _"""
        await ctx.message.edit(flood_spam)
        for i in range(2):
            await ctx.channel.send(flood_spam)
            await asyncio.sleep(0.5)