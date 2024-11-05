import discord
from discord.ext import commands
from colorama import Fore, Style, Back

import asyncio

import config_selfbot
from utils import log, lang, random_cooldown


class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot  # Initialisation du bot

    @commands.command()
    async def bump(self, ctx: commands.Context):
        message_split = ctx.message.content.split()  # Sépare le message pour obtenir les arguments
        # Vérifie si la commande est dans un DM ou un groupe
        if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
            await ctx.message.edit(lang.text('tool_bump_not_found'), delete_after=config_selfbot.deltime)
            return

        try:
            await ctx.guild.fetch_member(302050872383242240)  # Vérifie si le membre avec l'ID spécifique est dans le serveur
        except discord.NotFound:
            await ctx.message.edit(lang.text('tool_bump_not_found'), delete_after=config_selfbot.deltime)
            return

        try:
            count = int(message_split[1])  # Tente de convertir le deuxième argument en entier
        except Exception:
            await ctx.message.edit(f"{lang.text('spam_invalid')}!", delete_after=config_selfbot.deltime)
            return

        if count >= 100:  # Vérifie si le nombre de bumps est supérieur à 100
            await ctx.message.edit(lang.text('spam_too_much'), delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(f"{lang.text('tool_bump')} {count} {lang.text('tool_bump_two')}", delete_after=config_selfbot.deltime)

        # Récupère l'objet /bump pour le déclencher dans la boucle.
        command = [_ for _ in await ctx.channel.application_commands() if _.name == 'bump' and _.application_id == 302050872383242240][0]

        for i in range(count):
            # Déclenche la commande /bump
            await command.__call__(channel=ctx.channel)
            # Journalise l'action
            log.success(f"""{lang.text('tool_auto_bump')} {ctx.guild.name}({ctx.guild.id}) {lang.text('tool_auto_bump_two')} {i + 1} {lang.text('tool_auto_bump_three')}.
{lang.text('tool_auto_bump_four')} {count - i - 1} {lang.text('tool_auto_bump_five')} {ctx.channel.name}({ctx.channel.id}).""")
            # Attend avant de déclencher la prochaine commande /bump
            await asyncio.sleep(random_cooldown(7200, 7387))

    @commands.command()
    async def dmall(self, ctx: commands.Context):
        message_split = ctx.message.content.split()  # Sépare le message pour obtenir les arguments
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")  # Récupère le contenu du message pour DM
        try:
            message_split[1]  # Vérifie si le deuxième argument est présent
        except Exception:
            await ctx.message.edit(lang.text('raid_dm_all_fail'), delete_after=config_selfbot.deltime)
            return

        friends = self.bot.friends  # Récupère la liste des amis du bot

        log.separate_text("DM ALL")  # Journalise le début de l'opération DM

        print(f"{Fore.BLUE}Friends Counter: {len(friends)} | Message:\n{dmall_content}{Style.RESET_ALL}")  # Affiche le compteur d'amis et le message

        await ctx.message.edit(lang.text('raid_dm_all'))  # Informe l'utilisateur que le DM est en cours

        for friend in friends:  # Parcourt la liste des amis
            try:
                await friend.user.send(dmall_content)  # Envoie le message DM à chaque ami
                log.success(f"@{friend.user.name}({friend.user.id})")  # Journalise le succès
                await asyncio.sleep(random_cooldown(0.5, 2))  # Pause aléatoire pour éviter d'être bloqué
            except discord.Forbidden:
                log.fail(f"@{friend.user.name}({friend.user.id})")  # Journalise l'échec si le DM est interdit
            except discord.CaptchaRequired:
                log.alert("Captcha Required!")  # Alerte si un captcha est requis
                log.separate("DM ALL")  # Sépare le journal
                await ctx.message.edit(lang.text('raid_dm_all_captcha'), delete_after=config_selfbot.deltime)
                return

        log.separate("DM ALL")  # Sépare le journal à la fin de l'opération

        await ctx.message.edit(lang.text('raid_dm_all_success'), delete_after=config_selfbot.deltime)  # Confirme que l'opération a réussi

    @commands.command()
    async def closealldm(self, ctx: commands.Context):
        await ctx.message.edit(lang.text('tool_close_dms'))  # Informe que les DMs seront fermés

        for dm_channel in self.bot.private_channels:  # Parcourt les canaux privés du bot
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.me.id == self.bot.user.id:
                await dm_channel.close()  # Ferme le canal DM si c'est un DM du bot
                await asyncio.sleep(random_cooldown(0.5, 2))  # Pause aléatoire après chaque fermeture

        await ctx.message.edit(lang.text('tool_close_dms_success'), delete_after=config_selfbot.deltime)  # Confirme que les DMs ont été fermés avec succès

    @commands.command()
    async def botclosedm(self, ctx: commands.Context):
        await ctx.message.edit(lang.text('tool_close_dms_bots'))  # Informe que les DMs des bots seront fermés

        for dm_channel in self.bot.private_channels:  # Parcourt les canaux privés du bot
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.recipient.bot:  # Vérifie si le canal est un DM d'un bot
                await dm_channel.close()  # Ferme le canal DM du bot
                await asyncio.sleep(random_cooldown(0.5, 2))  # Pause aléatoire après chaque fermeture

        await ctx.message.edit(lang.text('tool_close_dms_bots_success'), delete_after=config_selfbot.deltime)  # Confirme que les DMs des bots ont été fermés avec succès
