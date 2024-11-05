from discord.ext import commands

import asyncio

import config_selfbot
from utils import lang


class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot  # Initialisation du bot

    @commands.command()
    async def joinvc(self, ctx: commands.Context):
        # Commande pour rejoindre un canal vocal
        voice_id = ctx.message.content.split()[1]  # Récupère l'ID du canal vocal depuis le message
        try:
            voice_id = int(voice_id)  # Convertit l'ID en entier
        except Exception:
            await ctx.message.edit(lang.text('voice_channel_error'), delete_after=config_selfbot.deltime)  # Alerte en cas d'erreur de conversion
            return

        voice_channel = self.bot.get_channel(voice_id)  # Récupère le canal vocal par son ID
        if voice_channel is None:
            await ctx.message.edit(lang.text('voice_channel_error_not_found'), delete_after=config_selfbot.deltime)  # Alerte si le canal vocal n'est pas trouvé
            return

        try:
            await voice_channel.connect()  # Rejoint le canal vocal
            await voice_channel.guild.change_voice_state(channel=voice_channel, self_mute=True)  # Se met en sourdine
            await ctx.message.edit(f"📲 {lang.text('voice_join')} `{voice_channel.name}`.", delete_after=config_selfbot.deltime)  # Confirme le join
        except Exception as e:
            await ctx.message.edit(f"❌ {lang.text('voice_join_error')} : {e}", delete_after=config_selfbot.deltime)  # Alerte en cas d'erreur
            return

    @commands.command()
    async def joincam(self, ctx: commands.Context):
        # Commande pour rejoindre un canal vocal avec vidéo
        voice_id = ctx.message.content.split()[1]  # Récupère l'ID du canal vocal depuis le message
        try:
            voice_id = int(voice_id)  # Convertit l'ID en entier
        except Exception:
            await ctx.message.edit(lang.text('voice_channel_error'), delete_after=config_selfbot.deltime)  # Alerte en cas d'erreur de conversion
            return

        voice_channel = self.bot.get_channel(voice_id)  # Récupère le canal vocal par son ID

        if voice_channel is None:
            await ctx.message.edit(lang.text('voice_channel_error_not_found'), delete_after=config_selfbot.deltime)  # Alerte si le canal vocal n'est pas trouvé
            return

        try:
            await voice_channel.connect()  # Rejoint le canal vocal
            await voice_channel.guild.change_voice_state(channel=voice_channel, self_video=True, self_mute=True)  # Active la vidéo et se met en sourdine
            await ctx.message.edit(f"🎥 {lang.text('voice_join_cam')} `{voice_channel.name}` {lang.text('voice_join_cam_two')}")  # Confirme le join avec vidéo
            await asyncio.sleep(config_selfbot.deltime)  # Attend un moment avant de supprimer le message
            await ctx.message.delete()  # Supprime le message d'origine
        except Exception as e:
            await ctx.message.edit(f"❌ {lang.text('voice_join_error')} : {e}", delete_after=config_selfbot.deltime)  # Alerte en cas d'erreur
            return

    @commands.command()
    async def leavevc(self, ctx: commands.Context):
        # Commande pour quitter le canal vocal
        voice_channel = ctx.message.author.voice.channel  # Récupère le canal vocal de l'utilisateur
        voice_client = ctx.voice_client  # Récupère le client vocal

        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.message.edit(lang.text('leave_voice_error_not_found'), delete_after=config_selfbot.deltime)  # Alerte si l'utilisateur n'est pas dans un canal vocal
            return

        try:
            await voice_client.disconnect()  # Déconnecte le client vocal
            await ctx.message.edit(f"💼 {lang.text('leave_voice')} `{voice_channel.name}`.", delete_after=config_selfbot.deltime)  # Confirme le départ
        except Exception as e:
            await ctx.message.edit(f"❌ {lang.text('leave_voice_error')} : {e}", delete_after=config_selfbot.deltime)  # Alerte en cas d'erreur
            return
