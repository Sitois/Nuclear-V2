from discord.ext import commands
import os, json, asyncio

from utils import log, lang, save_guild, load_guild, random_cooldown
import config_selfbot


class BackupCommands(commands.Cog):
    def __init__(self, bot):
        # fr: Initialise la classe avec une instance du bot.
        self.bot: commands.Bot = bot

    @commands.command()
    async def save(self, ctx: commands.Context):
        # fr: Commande pour sauvegarder les informations de la guilde dans un fichier de sauvegarde.
        try:
            # fr: Tente de récupérer l'ID de la guilde et de ses salons.
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[1]), with_counts=False)
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_channels = await guild.fetch_channels()
        except Exception:
            # fr: Si une erreur survient, utilise la guilde du contexte actuel.
            guild = ctx.guild
            guild_channels = guild.channels

        # fr: Définit le chemin du fichier de sauvegarde.
        backup_file = f"./backups/{guild.id}.json"

        # fr: Vérifie si la sauvegarde existe déjà.
        if os.path.exists(backup_file):
            await ctx.message.edit(f"{lang.text('backup_save_already_exist')} {guild.name} {lang.text('backup_save_already_exist_two')}", delete_after=config_selfbot.deltime)
            return

        # fr: Informe l'utilisateur que la sauvegarde est en cours.
        await ctx.message.edit(lang.text('backup_saving'))

        # fr: Appelle la fonction pour sauvegarder les informations de la guilde.
        await save_guild(guild, guild_channels)

        # fr: Confirme la sauvegarde réussie.
        await ctx.message.edit(f"{lang.text('backup_success_save')}: {guild.name}", delete_after=config_selfbot.deltime)

    @commands.command()
    async def backups(self, ctx: commands.Context):
        # fr: Commande pour lister toutes les sauvegardes disponibles.
        backups_list = os.listdir("backups")
        if not backups_list:
            # fr: Si aucune sauvegarde n'est trouvée, envoie un message d'erreur.
            await ctx.message.edit(lang.text('no_backup_error'), delete_after=config_selfbot.deltime)
            return

        # fr: Construit le message de réponse avec la liste des sauvegardes.
        response = f"__**🗒️| {lang.text('backup_list')}**__"
        for backup_file in backups_list:
            with open(f"./backups/{backup_file}", "r") as f:
                guild_info = json.load(f)
                response += f"👥{guild_info['name']} (🪪ID: `{guild_info['id']}`)\n"

        # fr: Envoie la liste des sauvegardes en réponse.
        await ctx.message.edit(response, delete_after=config_selfbot.deltime)

    @commands.command()
    async def load(self, ctx: commands.Context):
        # fr: Commande pour charger une sauvegarde dans la guilde actuelle.
        try:
            # fr: Récupère l'ID de la sauvegarde à partir du message.
            backup_id = ctx.message.content.split()[1]
        except Exception:
            # fr: Si aucun ID n'est spécifié, envoie un message d'erreur.
            await ctx.message.edit(lang.text('backup_id_required'), delete_after=config_selfbot.deltime)
            return

        # fr: Vérifie si le fichier de sauvegarde existe.
        if not os.path.exists(f"./backups/{backup_id}.json"):
            await ctx.message.edit(lang.text('backup_invalid'), delete_after=config_selfbot.deltime)
            return

        try:
            # fr: Tente de récupérer la guilde et ses salons.
            guild = await self.bot.fetch_guild(int(ctx.message.content.split()[2]), with_counts=False)
            await asyncio.sleep(random_cooldown(0.4, 2))
            guild_channels = await guild.fetch_channels()
        except Exception:
            guild = ctx.guild
            guild_channels = guild.channels

        # fr: Vérifie si le bot a les permissions administratives nécessaires.
        if not guild.me.guild_permissions.administrator:
            await ctx.message.edit(lang.text('backup_no_permissions'), delete_after=config_selfbot.deltime)
            return

        # fr: Charge les données de sauvegarde à partir du fichier.
        with open(f"./backups/{backup_id}.json", "r") as f:
            backup = json.load(f)

        # fr: Indique que le chargement de la sauvegarde est en cours.
        await ctx.message.edit(lang.text('backup_loading'))

        # fr: Charge la sauvegarde dans la guilde.
        await load_guild(guild, guild_channels, backup, 0.8, 25.6)

        # fr: Confirme que la sauvegarde a été chargée avec succès.
        await ctx.message.edit(lang.text('backup_done'))

        # fr: Enregistre un message de succès dans les logs.
        log.success(f"./backups/{backup_id}.json: {lang.text('backup_done')}")

    @commands.command()
    async def delete(self, ctx: commands.Context):
        # fr: Commande pour supprimer un fichier de sauvegarde.
        try:
            # fr: Récupère l'ID de la sauvegarde à supprimer.
            backup_id = ctx.message.content.split()[1]
        except Exception:
            await ctx.message.edit(lang.text('backup_id_required'), delete_after=config_selfbot.deltime)
            return

        # fr: Définit le chemin du fichier de sauvegarde.
        backup_file = f"./backups/{backup_id}.json"
        if not os.path.exists(backup_file):
            # fr: Vérifie si le fichier existe, sinon envoie un message d'erreur.
            await ctx.message.edit(lang.text('backup_invalid'), delete_after=config_selfbot.deltime)
            return

        # fr: Ouvre le fichier pour obtenir les informations de la guilde.
        with open(f"./backups/{backup_file}", "r") as f:
            guild_info = json.load(f)

        # fr: Envoie un message confirmant la suppression de la sauvegarde.
        await ctx.message.edit(f"{guild_info['name']}: {lang.text('backup_delete_done')}", delete_after=config_selfbot.deltime)

        # fr: Supprime le fichier de sauvegarde.
        os.remove(backup_file)
