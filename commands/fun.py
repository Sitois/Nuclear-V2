import discord
from discord.ext import commands
import asyncio
import random
import requests
import json


import config_selfbot
import fr_en


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.good_person = False

    @commands.command()
    async def call(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(fr_en.only_dm_fun[config_selfbot.lang])
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
            print(f"{fr_en.voice_join_error[config_selfbot.lang]}: {e}")

    @commands.command()
    async def good(self, ctx):
        if not self.good_person:
            self.good_person = True
            await ctx.message.edit(f"🌈 Good Person {fr_en.enable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif self.good_person:
            self.good_person = False
            await ctx.message.edit(f"🔥 Good Person {fr_en.disable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, ctx):
        good_person_list =[
        "GeForce RTX 4000",
        "🍗",
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.",
        "AMD Ryzen™ 9 7900",
        "Intel Core is very good",
        "🐈",
        "🍟",
        "yipeeeeeeeee",
        "😍",
        "🌠",
        "u r beautiful",
        "you are all very intelligent",
        "excuse me"
        ]

        if self.good_person:
            if ctx.author.id == self.bot.user.id:
                if any(word in ctx.content for word in config_selfbot.badwords):
                    await ctx.edit(random.choice(good_person_list))

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = json.loads(response.text)
            cat_image_url = data[0]['url']
            await ctx.send(cat_image_url)
        else:
            await ctx.send(f"Failed to fetch a cute cat: {response.text}")

    @commands.command()
    async def gift(self, ctx):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        gift_code = ''.join(random.choice(alphabet + numbers) for _ in range(16))
        await ctx.message.edit(f"discord.gift/{gift_code}")