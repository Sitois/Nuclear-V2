from discord.ext import commands
import asyncio

from utils import log, lang, generate_random_string, random_cooldown
import config_selfbot


class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.is_spamming: bool = False

    @commands.command()
    async def kickall(self, ctx: commands.Context):
        # Vérifie si l'auteur du message a la permission de kick des membres
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
            # Indique que le processus de kick est en cours
            await ctx.message.edit(lang.text('raid_in_process'))

            log.separate_text("KICK ALL")

            # Boucle à travers tous les membres du serveur
            for member in members:
                # Vérifie que le rôle du bot est supérieur au rôle du membre
                if ctx.guild.me.top_role > member.top_role:
                    # Kick le membre avec une raison générée aléatoirement
                    await member.kick(reason=f"{config_selfbot.kick_reason} {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id})")
                    await asyncio.sleep(random_cooldown(0.4, 1.1))

            log.separate("KICK ALL")

            # Indique que tous les kicks ont réussi
            await ctx.message.edit(lang.text('raid_kick_all_success'), delete_after=config_selfbot.deltime)
        else:
            # Affiche un message d'erreur si l'auteur n'a pas la permission
            await ctx.message.edit(lang.text('raid_error_permisssion'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def banall(self, ctx: commands.Context):
        # Vérifie si l'auteur du message a la permission de ban des membres
        if ctx.author.guild_permissions.ban_members:
            members = ctx.guild.members

            # Indique que le processus de ban est en cours
            await ctx.message.edit(lang.text('raid_in_process'))

            log.separate_text("BAN ALL")

            # Boucle à travers tous les membres du serveur
            for member in members:
                # Vérifie que le rôle du bot est supérieur au rôle du membre
                if ctx.guild.me.top_role > member.top_role:
                    # Ban le membre avec une raison générée aléatoirement
                    await member.ban(reason=f"{config_selfbot.ban_reason}. {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id})")
                    await asyncio.sleep(random_cooldown(0.4, 1.1))

            log.separate("BAN ALL")

            # Indique que tous les bans ont réussi
            await ctx.message.edit(lang.text('raid_ban_all_success'), delete_after=config_selfbot.deltime)
        else:
            # Affiche un message d'erreur si l'auteur n'a pas la permission
            await ctx.message.edit(lang.text('raid_error_permisssion'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def spam(self, ctx: commands.Context):
        # Récupère le contenu du message et le divise
        message_split = ctx.message.content.split()
        content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

        try:
            count = int(message_split[1]) - 1  # Récupère le nombre de messages à envoyer
        except Exception:
            # Affiche un message d'erreur si le nombre n'est pas valide
            await ctx.message.edit(f"{lang.text('spam_invalid')}!", delete_after=config_selfbot.deltime)
            return
        
        if count >= 100:
            # Vérifie que le nombre de messages est raisonnable
            await ctx.message.edit(lang.text('spam_too_much'), delete_after=config_selfbot.deltime)
            return

        try:
            message_split[2]  # Vérifie si un contenu de message a été fourni
        except Exception:
            # Affiche un message d'erreur si le contenu est manquant
            await ctx.message.edit(lang.text('raid_dm_all_fail'), delete_after=config_selfbot.deltime)
            return

        if not self.is_spamming:
            self.is_spamming = True  # Indique que le spam est en cours

            # Envoie le message initial
            await ctx.message.edit(content)

            for i in range(count):
                await ctx.channel.send(content)  # Envoie le contenu spécifié
                await asyncio.sleep(random_cooldown(0.4, 1.2))  # Pause aléatoire entre les messages
            self.is_spamming = False  # Indique que le spam est terminé
        else:
            # Affiche un message d'erreur si un spam est déjà en cours
            await ctx.message.edit(lang.text('spam_cooldown'), delete_after=config_selfbot.deltime)

    @commands.command()
    async def flood(self, ctx: commands.Context):
        # Crée un message de flood
        flood_spam = '_ _\n' * 44
        await ctx.message.edit(flood_spam)  # Modifie le message avec le contenu de flood
        for i in range(2):
            await ctx.channel.send(flood_spam)  # Envoie le flood dans le canal
            await asyncio.sleep(0.5)  # Pause entre les envois

    # TODO:
    # Ajouter la commande `nuke` qui supprimera tous les canaux et tous les rôles.
