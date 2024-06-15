import discord
from discord.ext import commands
import asyncio

import config_selfbot
import langs


class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def joinvc(self, ctx: commands.Context):
        voice_id = ctx.message.content.split()[1]
        try:
            voice_id = int(voice_id)
        except Exception:
            await ctx.message.edit(langs.voice_channel_error[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        voice_channel = self.bot.get_channel(voice_id)
        if voice_channel is None:
            await ctx.message.edit(langs.voice_channel_error_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return


        try:
            await voice_channel.connect()
            await voice_channel.guild.change_voice_state(channel=voice_channel, self_mute=True)
            await ctx.message.edit(f"📲 {langs.voice_join[config_selfbot.lang]} `{voice_channel.name}`.", delete_after=config_selfbot.deltime)
        except Exception as e:
            await ctx.message.edit(f"❌ {langs.voice_join_error[config_selfbot.lang]} : {e}", delete_after=config_selfbot.deltime)
            return

    @commands.command()
    async def joincam(self, ctx: commands.Context):
        voice_id = ctx.message.content.split()[1]
        try:
            voice_id = int(voice_id)
        except Exception:
            await ctx.message.edit(langs.voice_channel_error[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        voice_channel = self.bot.get_channel(voice_id)

        if voice_channel is None:
            await ctx.message.edit(langs.voice_channel_error_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return


        try:
            await voice_channel.connect()
            await voice_channel.guild.change_voice_state(channel=voice_channel, self_video=True, self_mute=True)
            await ctx.message.edit(f"🎥 {langs.voice_join_cam[config_selfbot.lang]} `{voice_channel.name}` {langs.voice_join_cam_two[config_selfbot.lang]}.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        except Exception as e:
            await ctx.message.edit(f"❌ {langs.voice_join_error[config_selfbot.lang]} : {e}", delete_after=config_selfbot.deltime)
            return

    @commands.command()
    async def leavevc(self, ctx: commands.Context):
        voice_channel = ctx.message.author.voice.channel
        voice_client = ctx.voice_client

        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.message.edit(langs.leave_voice_error_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            await voice_client.disconnect()
            await ctx.message.edit(f"💼 {langs.leave_voice[config_selfbot.lang]} `{voice_channel.name}`.", delete_after=config_selfbot.deltime)
        except Exception as e:
            await ctx.message.edit(f"❌ {langs.leave_voice_error[config_selfbot.lang]} : {e}", delete_after=config_selfbot.deltime)
            return