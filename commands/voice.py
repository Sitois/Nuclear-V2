import discord
from discord.ext import commands
import asyncio
import os
import sys

parent_dir = os.path.abspath('./')
sys.path.append(parent_dir)
import config_selfbot
import fr_en

class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joinvc(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(fr_en.voice_not_dm[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        voice_id = ctx.message.content.split()[1]
        try:
            voice_id = int(voice_id)
        except Exception:
            await ctx.message.edit(fr_en.voice_channel_error[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

        voice_channel = self.bot.get_channel(voice_id)
        if voice_channel is None:
            await ctx.message.edit(fr_en.voice_channel_error_not_found[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return


        try:
            voice_client = await voice_channel.connect()
            await ctx.guild.change_voice_state(channel=voice_channel, self_mute=True)
            await ctx.message.edit(f"📲 {fr_en.voice_join[config_selfbot.lang]} `{voice_channel.name}`.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        except Exception as e:
            await ctx.message.edit(f"❌ {fr_en.voice_join_error[config_selfbot.lang]} : {e}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def joincam(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(fr_en.voice_not_dm[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return
        
        voice_id = ctx.message.content.split()[1]
        try:
            voice_id = int(voice_id)
        except Exception:
            await ctx.message.edit(fr_en.voice_channel_error[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

        voice_channel = self.bot.get_channel(voice_id)
        if voice_channel is None:
            await ctx.message.edit(fr_en.voice_channel_error_not_found[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return


        try:
            await voice_channel.connect()
            await ctx.guild.change_voice_state(channel=voice_channel, self_video=True, self_mute=True)
            await ctx.message.edit(f"🎥 {fr_en.voice_join_cam[config_selfbot.lang]} `{voice_channel.name}` {fr_en.voice_join_cam_two[config_selfbot.lang]}.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        except Exception as e:
            await ctx.message.edit(f"❌ {fr_en.voice_join_error[config_selfbot.lang]} : {e}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def leavevc(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(fr_en.voice_not_dm[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return
        
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.message.edit(fr_en.leave_voice_error_not_found[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        voice_channel = ctx.author.voice.channel

        try:
            await ctx.voice_client.disconnect()
            await ctx.message.edit(f"💼 {fr_en.leave_voice[config_selfbot.lang]} `{voice_channel.name}`.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        except Exception as e:
            await ctx.message.edit(f"❌ {fr_en.leave_voice_error[config_selfbot.lang]} : {e}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()