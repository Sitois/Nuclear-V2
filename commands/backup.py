import discord
from discord.ext import commands
import os, json, asyncio

from utils import log, save_guild, load_guild, random_cooldown
import config_selfbot
import langs


class BackupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def save(self, ctx: commands.Context):
        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[1]), with_counts=False)
            guild_channels = await guild.fetch_channel(int(ctx.message.content.split()[1]))
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_roles = await guild.fetch_roles(int(ctx.message.content.split()[1]))
            await asyncio.sleep(random_cooldown(0.4, 2))
        except Exception:
            guild = ctx.guild
            guild_channels = guild.channels
            guild_roles = guild.roles

        backup_file = f"./backups/{guild.id}.json"

        if os.path.exists(backup_file):
            await ctx.message.edit(f"{langs.backup_save_already_exist[config_selfbot.lang]} {guild.name} {langs.backup_save_already_exist_two[config_selfbot.lang]}", delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(langs.backup_saving[config_selfbot.lang])

        await save_guild(guild,
                         guild_channels,
                         guild_roles)

        await ctx.message.edit(f"{langs.backup_success_save[config_selfbot.lang]}: {guild.name}", delete_after=config_selfbot.deltime)

    @commands.command()
    async def backups(self, ctx: commands.Context):
        backups_list = os.listdir("backups")
        if not backups_list:
            await ctx.message.edit(langs.no_backup_error[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        response = f"__**🗒️| {langs.backup_list[config_selfbot.lang]}**__"
        for backup_file in backups_list:
            with open(f"./backups/{backup_file}", "r") as f:
                guild_info = json.load(f)
                response += f"{guild_info['name']} (ID: `{guild_info['id']}`)\n"

        await ctx.message.edit(response, delete_after=config_selfbot.deltime)

    @commands.command()
    async def load(self, ctx: commands.Context):
        try:
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(langs.backup_id_required[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        if not os.path.exists(f"./backups/{backup_id}.json"):
            await ctx.message.edit(langs.backup_invalid[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[2]), with_counts=False)
            guild_channels = await guild.fetch_channel(int(ctx.message.content.split()[1]))
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_roles = await guild.fetch_roles(int(ctx.message.content.split()[1]))
            await asyncio.sleep(random_cooldown(0.4, 2))
        except Exception:
            guild = ctx.guild
            guild_channels = guild.channels
            guild_roles = guild.roles

        if not guild.me.guild_permissions.administrator:
            await ctx.message.edit(langs.backup_no_permissions[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        with open(f"./backups/{backup_id}.json", "r") as f:
            backup = json.load(f)

        await load_guild(guild,
                         guild_channels,
                         guild_roles,
                         backup,
                         0.8, 25.6)

        log.success(f"./backups/{backup_id}.json: {langs.backup_done[config_selfbot.lang]}")

    @commands.command()
    async def delete(self, ctx: commands.Context):
        try:
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(langs.backup_id_required[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        backup_file = f"./backups/{backup_id}.json"
        if not os.path.exists(backup_file):
            await ctx.message.edit(langs.backup_invalid[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return
        
        with open(f"./backups/{backup_file}", "r") as f:
            guild_info = json.load(f)

        await ctx.message.edit(f"{guild_info['name']}: {langs.backup_delete_done[config_selfbot.lang]}", delete_after=config_selfbot.deltime)

        os.remove(backup_file)