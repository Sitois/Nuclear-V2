import discord
from discord.ext import commands
import os, json
import asyncio

from utils import log, save_guild_info, random_cooldown
import config_selfbot
import langs


class BackupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def save(self, ctx: commands.Context):
        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[1]), with_counts=False)
        except Exception:
            guild = ctx.guild

        backup_file = f"./backups/{guild.id}.json"

        if os.path.exists(backup_file):
            await ctx.message.edit(f"{langs.backup_save_already_exist[config_selfbot.lang]} {guild.name} {langs.backup_save_already_exist_two[config_selfbot.lang]}", delete_after=config_selfbot.deltime)
            return

        await save_guild_info(guild)

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
        if not ctx.author.guild_permissions.administrator:
            await ctx.message.edit(langs.no_admin_error[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(langs.backup_id_required[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        backup_file = f"./backups/{backup_id}.json"

        if not os.path.exists(backup_file):
            await ctx.message.edit(langs.backup_invalid[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        with open(backup_file, "r") as f:
            guild_info = json.load(f)

        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[2]), with_counts=False)
        except Exception:
            guild = ctx.guild

        # Delete old channels
        for channel in guild.channels:
            try:
                await channel.delete()
                await asyncio.sleep(random_cooldown(0.7, 1.7))  # Wait to avoid rate limit
            except Exception as e:
                log.fail(f"Error while trying to delete channel: {channel.name}({channel.id}): {e}")

        # Delete old roles (not @everyone, not bot roles)
        for role in guild.roles:
            if role.name != "@everyone" and not role.is_integration():
                try:
                    await role.delete()
                    await asyncio.sleep(random_cooldown(0.7, 2.1))  # Wait to avoid rate limit
                except Exception as e:
                    log.fail(f"Error while trying to delete role: {role.name}: {e}")

        # Add backup's roles
        for role_info in guild_info["roles"]:
            await guild.create_role(
                name=role_info["name"],
                permissions=discord.Permissions(role_info["permissions"]),
                color=discord.Color(role_info["color"]),
                mentionable=role_info["mentionable"],
                hoist=role_info["hoist"]
            )
            await asyncio.sleep(random_cooldown(0.8, 1.4))  # Pause d'une seconde pour éviter le rate limit

        # Add backup's channels
        for channel_info in guild_info["channels"]:
            overwrites = {}
            for perm in channel_info["permissions"]:
                target = guild.get_role(perm["id"]) if perm["type"] == "role" else guild.get_member(perm["id"])
                if target:
                    overwrites[target] = discord.PermissionOverwrite.from_pair(
                        discord.Permissions(perm["allow"]),
                        discord.Permissions(perm["deny"])
                    )

            channel_type = discord.ChannelType.text if channel_info["type"] == "text" else discord.ChannelType.voice
            await guild.create_text_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites
            ) if channel_type == discord.ChannelType.text else await guild.create_voice_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites
            )
            await asyncio.sleep(random_cooldown(0.8, 1.4))  # Wait, to avoid rate limits

        # Set backup's @everyone permissions
        await guild.default_role.edit(permissions=discord.Permissions(guild_info["default_role"]["permissions"]))

        log.success(f"{backup_id}: {langs.backup_done[config_selfbot.lang]}")

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

        os.remove(backup_file)

        await ctx.message.edit(f"{backup_id}: {langs.backup_delete_done[config_selfbot.lang]}", delete_after=config_selfbot.deltime)