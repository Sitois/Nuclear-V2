import discord
from discord.ext import commands
import asyncio
import random
import requests
import json


import config_selfbot
import langs


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.good_person = config_selfbot.good_person
        self.badwords = config_selfbot.badwords
        self.good_person_list = config_selfbot.good_person_list

    @commands.command()
    async def call(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(langs.only_dm_fun[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        try:
            await ctx.message.delete()
            for i in range(5):
                voice_client = await ctx.channel.connect(reconnect=False)
                await asyncio.sleep(0.5)
                await voice_client.disconnect()
                await asyncio.sleep(1.3)
        except Exception as e:
            print(f"{langs.voice_join_error[config_selfbot.lang]}: {e}")

    @commands.command()
    async def good(self, ctx):
        if not self.good_person:
            self.good_person = True
            await ctx.message.edit(f"🌈 Good Person {langs.enable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif self.good_person:
            self.good_person = False
            await ctx.message.edit(f"🔥 Good Person {langs.disable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.good_person:
            if ctx.author.id == self.bot.user.id:
                if any(word in ctx.content.lower() for word in self.badwords):
                    await ctx.edit(random.choice(self.good_person_list))

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = json.loads(response.text)
            cat_image_url = data[0]['url']
            await ctx.message.edit(cat_image_url)
        else:
            await ctx.message.edit(f"Failed to fetch a cute cat: {response.text}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def gift(self, ctx):
        try:
            gift_type = ctx.message.content.split()[1]
        except Exception:
            gift_type = "random"
        

        if gift_type == "poor":
            await ctx.message.edit("discord.gift/vhnuzE2YkNCZ7sfYHHKebKXB")
        elif gift_type == "nerd":
            await ctx.message.edit("discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"
            gift_code = ''.join(random.choice(alphabet + numbers) for _ in range(16))
            await ctx.message.edit(f"discord.gift/{gift_code}")