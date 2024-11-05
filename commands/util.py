
import discord
from discord.ext import commands

import asyncio, time

import config_selfbot
from utils import lang, random_cooldown


class UtilsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot  # Initialisation du bot
        self.sniped_messages: dict = {}  # Dictionnaire pour stocker les messages supprimés

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Écouteur pour capturer les messages supprimés
        if not message.author.id == self.bot.user.id:  # Ignore les messages supprimés par le bot
            try:
                attachments_urls = [attachment.url for attachment in message.attachments]  # Récupère les URLs des pièces jointes
                self.sniped_messages[message.channel.id] = {
                    'author': message.author,  # Auteur du message
                    'content': message.content,  # Contenu du message
                    'images': attachments_urls if message.attachments else None,  # Images si présentes
                    'time': round(time.time())  # Timestamp du message
                }
            except Exception:
                return  # Ignore les erreurs

    @commands.command()
    async def snipe(self, ctx: commands.Context):
        # Commande pour récupérer le dernier message supprimé
        sniped_message = self.sniped_messages.get(ctx.channel.id)  # Récupère le message supprimé pour le canal
        if sniped_message:
            # Récupère les images et formate le message
            images_text = ", ".join(sniped_message['images']) if not sniped_message['images'] is None else lang.text('empty')
            await ctx.message.edit(f"""__**🔫 Sniper:**__

🗣️ {lang.text('author')}: {sniped_message['author']}
📩 Message:
```txt
{sniped_message['content']}
```
🖼️ Images: {images_text}
⌚ {lang.text('time_snipe')}: <t:{sniped_message['time']}:R>""", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(lang.text('error_no_message_snipe'), delete_after=config_selfbot.deltime)  # Alerte si aucun message trouvé

    @commands.command()
    async def clear(self, ctx: commands.Context):
        # Commande pour supprimer un nombre spécifique de messages
        message_split = ctx.message.content.split()  # Sépare le message pour obtenir les arguments
        try:
            str_amount = message_split[1]  # Tente d'obtenir le nombre de messages à supprimer
        except Exception:
            str_amount = "19"  # Valeur par défaut

        try:
            amount = int(str_amount) + 1  # Convertit en entier et ajoute 1
        except Exception:
            await ctx.message.edit(lang.text('spam_invalid'), delete_after=config_selfbot.deltime)  # Alerte si le nombre est invalide
            return

        await ctx.message.edit(f"> 🌌 **{config_selfbot.selfbot_name}**", delete_after=1.7)  # Affiche un message indiquant la suppression

        async for message in ctx.channel.history(limit=amount):  # Récupère l'historique des messages
            if message.author.id == self.bot.user.id:  # Vérifie si le message a été envoyé par le bot
                await message.delete()  # Supprime le message
                await asyncio.sleep(random_cooldown(0.4, 1))  # Pause aléatoire après chaque suppression

    @commands.command()
    async def hype(self, ctx: commands.Context):
        # Commande pour changer la maison HypeSquad
        house = ctx.message.content.split()[1]  # Récupère le nom de la maison
        if house == "balance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.balance)
            await ctx.message.edit(f"🪄 HypeSquad {lang.text('hype_command')} ``{house}``", delete_after=config_selfbot.deltime)
        elif house == "bravery":
            await self.bot.user.edit(house=discord.HypeSquadHouse.bravery)
            await ctx.message.edit(f"🪄 HypeSquad {lang.text('hype_command')} ``{house}``", delete_after=config_selfbot.deltime)
        elif house == "brilliance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.brilliance)
            await ctx.message.edit(f"🪄 HypeSquad {lang.text('hype_command')} ``{house}``", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(lang.text('hype_fail'), delete_after=config_selfbot.deltime)  # Alerte si la maison est invalide

    @commands.command()
    async def ping(self, ctx: commands.Context):
        # Commande pour vérifier la latence du bot
        await ctx.message.edit(f"🏓 Pong ! (Ping: **{round(self.bot.latency * 1000)}ms**)", delete_after=config_selfbot.deltime)

    @commands.command()
    async def bio(self, ctx: commands.Context):
        # Commande pour modifier la bio de l'utilisateur
        message_split = ctx.message.content.split()  # Sépare le message pour obtenir les arguments
        new_bio = ctx.message.content.replace(f"{message_split[0]} ", "")  # Récupère la nouvelle bio
        await self.bot.user.edit(bio=new_bio)  # Met à jour la bio
        await ctx.message.edit(f"📖 Bio {lang.text('bio_command')} \"`{new_bio}`\"", delete_after=config_selfbot.deltime)  # Confirme la mise à jour

    @commands.command()
    async def userinfo(self, ctx: commands.Context):
        # Commande pour obtenir des informations sur un utilisateur
        if ctx.message.mentions:
            user = ctx.message.mentions[0]  # Si un utilisateur est mentionné, l'utilise
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))  # Récupère l'utilisateur par ID
            except Exception:
                user = ctx.author  # Sinon, utilise l'auteur de la commande

        user = await self.bot.fetch_user(user.id)  # Récupère l'utilisateur pour les informations de bannière

        if ctx.guild:
            guild = ctx.guild
            member = guild.get_member(user.id)  # Récupère le membre du serveur
            roles = [role.name for role in member.roles[1:] if role.name != '@everyone'] if member else []  # Récupère les rôles du membre
        else:
            roles = []

        # Formate le message d'informations sur l'utilisateur
        message = f"""🗒️| {lang.text('info_title')} <@{user.id}> :
>  👤| {lang.text('info_global')}: `{user.global_name}`
>  🌐| {lang.text('info_username')}: `{user.name}`
>  🆔| ID: `{user.id}`
>  🌈| {lang.text('info_banner')}: {"[" + lang.text('info_banner_link') + "](" + user.banner.url + ")" if not user.banner is None else "`" + lang.text('empty') + "`"}
>  📅| {lang.text('info_created_at')}: `{user.created_at.strftime('%Y/%m/%d %H:%M:%S')}`
>  🖼️| {lang.text('info_avatar')}: {"[" + lang.text('info_avatar_link') + "](" + user.avatar.url + ")" if not user.avatar is None else "`" + lang.text('empty') + "`"}"""

        if roles:  # Ajoute les rôles au message s'il y en a
            message += f"\n>  🎭| {lang.text('info_roles')}: {', '.join(roles)}"

        await ctx.message.edit(message, delete_after=config_selfbot.deltime)  # Envoie le message d'informations

    # TODO:
    # Amélioration : Ajouter le statut de l'utilisateur dans la commande `userinfo`.
    # Ajouter : commande `serverinfo` qui renverra des informations sur le serveur.
    # Ajouter : commande `botinvite` qui renverra une invitation pour le bot avec l'ID donné.
    # Ajouter : commande `support` qui renverra des liens de support.
