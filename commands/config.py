import discord
from discord.ext import commands
from colorama import Fore, Style, Back

from utils import log, lang
import config_selfbot


class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        # fr: Initialise la classe avec une instance du bot et l'état du Nitro Sniper.
        self.bot: commands.Bot = bot
        self.nitro_sniper: bool = config_selfbot.nitro_sniper

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # fr: Écoute les messages pour détecter les liens Discord Nitro et tenter de les réclamer.
        if self.nitro_sniper and not message.author.id == self.bot.user.id:
            # fr: Vérifie la présence d'un lien Discord Nitro dans le message.
            if "discord.gift/" in message.content:
                try:
                    # fr: Extrait le code Nitro du message.
                    gift_code = message.content.split("discord.gift/")[1].split()[0]

                    # fr: Empêche de réclamer certains liens inaccessibles.
                    if "-" in gift_code: 
                        # fr: Empêche de réclamer un code promotionnel.
                        return

                    if gift_code == "Udzwm3hrQECQBnEEFFCEwdSq":
                        # fr: Empêche de réclamer le code Nitro personnalisé "Nerd".
                        return

                    if gift_code == "vhnuzE2YkNCZ7sfYHHKebKXB":
                        # fr: Empêche de réclamer le code Nitro personnalisé "No Nitro ?".
                        return

                    if gift_code == "BMHmv4FWEM5WVGnHUHCYFKMx":
                        # fr: Empêche de réclamer le code Nitro personnalisé "Does he know ?".
                        return

                    # fr: Affiche le code Nitro dans la console.
                    if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code} | Channel: {message.channel.name}({message.channel.id}) | Guild: {message.guild.name}({message.guild.id}){Style.RESET_ALL}")
                    
                    # fr: Tente de réclamer le code Nitro.
                    gift = await self.bot.fetch_gift(gift_code)
                    await gift.redeem(channel=message.channel)
                    log.success(f"discord.gift/{gift_code} {lang.text('nitro_sniper_valid')}")
                
                except discord.NotFound:
                    # fr: Le code Nitro est invalide ou déjà réclamé.
                    log.alert(f"discord.gift/{gift_code} {lang.text('nitro_sniper_invalid_code')}")
                
                except discord.HTTPException:
                    # fr: Le code Nitro a déjà été réclamé.
                    log.alert(f"discord.gift/{gift_code} {lang.text('nitro_sniper_claimed')}")

    @commands.command()
    async def nitrosniper(self, ctx: commands.Context):
        # fr: Commande pour activer ou désactiver le Nitro Sniper.
        if not self.nitro_sniper:
            # fr: Active le Nitro Sniper.
            self.nitro_sniper = True
            await ctx.message.edit("🟢 Nitro Sniper **On**.", delete_after=config_selfbot.deltime)
        else:
            # fr: Désactive le Nitro Sniper.
            self.nitro_sniper = False
            await ctx.message.edit("🔴 Nitro Sniper **Off**.", delete_after=config_selfbot.deltime)

    @commands.command()
    async def lang(self, ctx: commands.Context):
        # fr: Commande pour changer la langue du Selfbot.
        try:
            # fr: Récupère le choix de la langue dans le message.
            choice = ctx.message.content.split()[1]
        except Exception:
            # fr: Envoie un message d'erreur si aucune langue n'est spécifiée.
            message = f"**{lang.text('config_lang_invalid')}**\n"
            message += '\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()])
            await ctx.message.edit(message, delete_after=config_selfbot.deltime)
            return

        # fr: Vérifie si la langue choisie est disponible.
        available_languages = [f"{list(item.values())[0]}" for item in lang.languages()]
        if choice in available_languages:
            # fr: Modifie la langue par défaut et recharge les fichiers de langue.
            config_selfbot.lang = choice[:2]
            lang.reload_all_lang_files()
            await ctx.message.edit(f"🟢 **{choice}**.", delete_after=config_selfbot.deltime)
        else:
            # fr: Affiche un message d'erreur si la langue n'est pas disponible.
            message = f"**{lang.text('config_lang_invalid')}**\n"
            message += '\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()])
            await ctx.message.edit(message, delete_after=config_selfbot.deltime)
