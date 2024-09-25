from discord.ext import commands
import os, json, asyncio

from utils import log, lang, save_guild, load_guild, random_cooldown
import config_selfbot


class BackupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def save(self, ctx: commands.Context):
        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[1]), with_counts=False)
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_channels = await guild.fetch_channels()
        except Exception:
            guild = ctx.guild
            guild_channels = guild.channels

        backup_file = f"./backups/{guild.id}.json"

        if os.path.exists(backup_file):
            await ctx.message.edit(f"{lang.text('backup_save_already_exist')} {guild.name} {lang.text('backup_save_already_exist_two')}", delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(lang.text('backup_saving'))

        await save_guild(guild,
                         guild_channels)

        await ctx.message.edit(f"{lang.text('backup_success_save')}: {guild.name}", delete_after=config_selfbot.deltime)

    @commands.command()
    async def backups(self, ctx: commands.Context):
        backups_list = os.listdir("backups")
        if not backups_list:
            await ctx.message.edit(lang.text('no_backup_error'), delete_after=config_selfbot.deltime)
            return

        response = f"__**🗒️| {lang.text('backup_list')}**__"
        for backup_file in backups_list:
            with open(f"./backups/{backup_file}", "r") as f:
                guild_info = json.load(f)
                response += f"👥{guild_info['name']} (🪪ID: `{guild_info['id']}`)\n"

        await ctx.message.edit(response, delete_after=config_selfbot.deltime)

    @commands.command()
    async def load(self, ctx: commands.Context):
        try:
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(lang.text('backup_id_required'), delete_after=config_selfbot.deltime)
            return

        if not os.path.exists(f"./backups/{backup_id}.json"):
            await ctx.message.edit(lang.text('backup_invalid'), delete_after=config_selfbot.deltime)
            return

        try:
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[2]), with_counts=False)
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_channels = await guild.fetch_channels()
        except Exception:
            guild = ctx.guild
            guild_channels = guild.channels

        if not guild.me.guild_permissions.administrator:
            await ctx.message.edit(lang.text('backup_no_permissions'), delete_after=config_selfbot.deltime)
            return

        with open(f"./backups/{backup_id}.json", "r") as f:
            backup = json.load(f)

        await ctx.message.edit(lang.text('backup_loading'))

        await load_guild(guild,
                         guild_channels,
                         backup,
                         0.8, 25.6)

        await ctx.message.edit(lang.text('backup_done'))

        log.success(f"./backups/{backup_id}.json: {lang.text('backup_done')}")

    @commands.command()
    async def delete(self, ctx: commands.Context):
        try:
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(lang.text('backup_id_required'), delete_after=config_selfbot.deltime)
            return

        backup_file = f"./backups/{backup_id}.json"
        if not os.path.exists(backup_file):
            await ctx.message.edit(lang.text('backup_invalid'), delete_after=config_selfbot.deltime)
            return

        with open(f"./backups/{backup_file}", "r") as f:
            guild_info = json.load(f)

        await ctx.message.edit(f"{guild_info['name']}: {lang.text('backup_delete_done')}", delete_after=config_selfbot.deltime)

        os.remove(backup_file)