import discord
from discord.ext import commands
import requests

import asyncio, random, json, base64

import config_selfbot
from utils import lang


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.good_person: bool = config_selfbot.good_person
        self.badwords: list = config_selfbot.badwords
        self.good_person_list: list = config_selfbot.good_person_list

    # Écouteur d'événements pour vérifier les messages de l'utilisateur
    @commands.Cog.listener()
    async def on_message(self, ctx):
        # Vérifie si le filtre "good_person" est activé et si l'auteur est le bot
        if self.good_person and ctx.author.id == self.bot.user.id:
            # Si un mot interdit est trouvé, remplace le message par un mot positif
            if any(word in ctx.content.lower() for word in self.badwords):
                await ctx.edit(random.choice(self.good_person_list))

    # Commande pour appeler en DM avec des connexions rapides
    @commands.command()
    async def call(self, ctx: commands.Context):
        # Vérifie si la commande est exécutée dans un DM
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(lang.text('only_dm_fun'), delete_after=config_selfbot.deltime)
            return

        try:
            await ctx.message.delete()
            # Connexion et déconnexion rapides dans le canal vocal
            for i in range(5):
                voice_client = await ctx.channel.connect(reconnect=False)
                await asyncio.sleep(0.5)
                await voice_client.disconnect()
                await asyncio.sleep(1.3)
        except Exception as e:
            print(f"{lang.text('voice_join_error')}: {e}")

    # Commande pour activer/désactiver le filtre "good_person"
    @commands.command()
    async def good(self, ctx: commands.Context):
        if self.good_person:
            self.good_person = False
            await ctx.message.edit(f"🔥 Good Person {lang.text('disable')}", delete_after=config_selfbot.deltime)
        else:
            self.good_person = True
            await ctx.message.edit(f"🌈 Good Person {lang.text('enable')}", delete_after=config_selfbot.deltime)

    # Commande pour envoyer un gif de câlin
    @commands.command()
    async def hug(self, ctx: commands.Context):
        hug_gifs = ["https://media1.tenor.com/m/l35okzAUNMgAAAAC/peach-and-goma-peachcat.gif",
                    "https://media1.tenor.com/m/4-UFx3TTQK0AAAAC/november.gif",
                    "https://media1.tenor.com/m/n9C4G-QEsrcAAAAC/squeeze-hug.gif",
                    "https://media1.tenor.com/m/JKo6Z5x3slYAAAAC/hug-extasyxx.gif",
                    "https://media1.tenor.com/m/24n__MYJspQAAAAC/hug.gif"
                   ]

        # Modifie le message pour envoyer un gif de câlin aléatoire
        await ctx.message.edit(random.choice(hug_gifs))

    # Commande pour envoyer un gif de gifle
    @commands.command()
    async def slap(self, ctx: commands.Context):
        slap_gifs = ["https://tenor.com/bVL3e.gif",
                    "https://tenor.com/h0DwLm9JkoL.gif",
                    "https://tenor.com/bBKQH.gif",
                    "https://tenor.com/bR6Oj.gif",
                    "https://tenor.com/ptFuKOKXwCp.gif",
                    "https://tenor.com/fFuVfLoRW0z.gif"
                    ]

        # Modifie le message pour envoyer un gif de gifle aléatoire
        await ctx.message.edit(random.choice(slap_gifs))

    # Commande pour "pirater" un utilisateur (simulation humoristique)
    @commands.command()
    async def hack(self, ctx: commands.Context):
        # Vérifie si un utilisateur est mentionné sinon utilise l'auteur
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author

        # Simulation humoristique de différentes étapes de "piratage"
        await ctx.message.edit(f"---{lang.text('fun_hack_step_one')} <@{user.id}>---")
        await asyncio.sleep(2)
        await ctx.message.edit(f"{lang.text('fun_hack_step_two')}...")
        await asyncio.sleep(2)
        await ctx.message.edit(f"{lang.text('fun_hack_step_three')} {user.name}@gmail.com")
        await asyncio.sleep(2)
        await ctx.message.edit(lang.text('fun_hack_step_four'))
        await asyncio.sleep(2)
        await ctx.message.edit(f"{lang.text('fun_hack_step_five')} <@{user.id}>")

    # Commande pour afficher une image aléatoire de chat
    @commands.command()
    async def cat(self, ctx: commands.Context):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = json.loads(response.text)
            cat_image_url = data[0]['url']
            await ctx.message.edit(cat_image_url)
        else:
            await ctx.message.edit(f"Échec de la récupération d'un chat mignon : {response.text}", delete_after=config_selfbot.deltime)

    # Commande pour générer un faux code cadeau Discord
    @commands.command()
    async def gift(self, ctx: commands.Context):
        try:
            gift_type = ctx.message.content.split()[1]
        except Exception:
            gift_type = "random"

        # Génère un code cadeau spécifique ou aléatoire
        if gift_type == "poor":
            await ctx.message.edit("discord.gift/vhnuzE2YkNCZ7sfYHHKebKXB")
        elif gift_type == "nerd":
            await ctx.message.edit("discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
        elif gift_type == "hit":
            await ctx.message.edit("discord.gift/BMHmv4FWEM5WVGnHUHCYFKMx")
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"
            gift_code = ''.join(random.choice(alphabet + numbers) for _ in range(16))
            await ctx.message.edit(f"discord.gift/{gift_code}")

    # Commande pour vérifier le pourcentage de "femboy" d'un utilisateur
    @commands.command()
    async def howfemboy(self, ctx: commands.Context):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author

        rng = random.randint(1, 100)

        # Messages humoristiques basés sur le pourcentage de "femboy"
        if rng >= 85:
            await ctx.message.edit(f"<@{user.id}> {lang.text('is')} **{rng}%** [femboy](https://tenor.com/bQmRX.gif) 💅!")
        elif rng >= 75:
            await ctx.message.edit(f"<@{user.id}> {lang.text('is')} **{rng}%** [femboy](https://tenor.com/bUyzv.gif) 😈!")
        else:
            await ctx.message.edit(f"<@{user.id}> {lang.text('is')} **{rng}%** femboy!")

    # Commande pour générer un jeton simulé basé sur l'ID utilisateur
    @commands.command()
    async def token(self, ctx: commands.Context):
        if ctx.message.mentions:
            user_id = ctx.message.mentions[0].id
        else:
            try:
                user_id = self.bot.get_user(int(ctx.message.content.split()[1])).id
            except Exception:
                user_id = ctx.author.id

        # Encode l'ID utilisateur en base64 pour créer un "faux jeton"
        encode_text = base64.b64encode(str(user_id).encode('utf-8'))
        start_token = str(encode_text).strip("b'").strip()
        await ctx.message.edit(f"🌠 {lang.text('fun_token')} <@{user_id}> jeton: `{start_token}.`", delete_after=config_selfbot.deltime)


    """
    TODO: Fix copyuser: discord.errors.CaptchaRequired: 400 Bad Request (error code: -1): Captcha required, at await self.bot.user.edit().
          Improve: Copy user's Rich Presence.
          Imprive: Use dict to save user's profile


    @commands.command()
    async def copyuser(self, ctx):
        # Attempts to copy the profile and status of the specified user, with current limitations due to Captcha requirements.
        # Backs up the current profile of the bot user for future restoration.

    @commands.command()
    async def recover(self, ctx):
        # Restores the bot's previous profile, if saved, including avatar, bio, and banner for Nitro users.
