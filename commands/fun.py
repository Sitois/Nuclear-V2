import discord
from discord.ext import commands
import asyncio
import random
import requests
import json
import base64


import config_selfbot
import langs


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.good_person: bool = config_selfbot.good_person
        self.badwords: list = config_selfbot.badwords
        self.good_person_list: list = config_selfbot.good_person_list

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.good_person and ctx.author.id == self.bot.user.id:
            if any(word in ctx.content.lower() for word in self.badwords):
                await ctx.edit(random.choice(self.good_person_list))

    @commands.command()
    async def call(self, ctx: commands.Context):
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
    async def good(self, ctx: commands.Context):
        if self.good_person:
            self.good_person = False
            await ctx.message.edit(f"🔥 Good Person {langs.disable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            self.good_person = True
            await ctx.message.edit(f"🌈 Good Person {langs.enable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def hack(self, ctx: commands.Context):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author
        
        await ctx.message.edit(f"---{langs.fun_hack_step_one[config_selfbot.lang]} <@{user.id}>---")
        await asyncio.sleep(2)
        await ctx.message.edit(f"{langs.fun_hack_step_two[config_selfbot.lang]}...")
        await asyncio.sleep(2)
        await ctx.message.edit(f"{langs.fun_hack_step_three[config_selfbot.lang]} {user.name}@gmail.com")
        await asyncio.sleep(2)
        await ctx.message.edit(langs.fun_hack_step_four[config_selfbot.lang])
        await asyncio.sleep(2)
        await ctx.message.edit(f"{langs.fun_hack_step_five[config_selfbot.lang]} <@{user.id}>")

    @commands.command()
    async def cat(self, ctx: commands.Context):
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
    async def gift(self, ctx: commands.Context):
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

        if rng >= 85:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** [femboy](https://tenor.com/bQmRX.gif) 💅!")
        elif rng >= 75:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** [femboy](https://tenor.com/bUyzv.gif) 😈!")
        else:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** femboy!")

    @commands.command()
    async def token(self, ctx: commands.Context):
        if ctx.message.mentions:
            user_id = ctx.message.mentions[0].id
        else:
            try:
                user_id = self.bot.get_user(int(ctx.message.content.split()[1])).id
            except Exception:
                user_id = ctx.author.id

        encode_text = base64.b64encode(str(user_id).encode('utf-8'))
        start_token = str(encode_text).strip("b'").strip()
        await ctx.message.edit(f"🌠 {langs.fun_token[config_selfbot.lang]} <@{user_id}> token: `{start_token}.`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    """
    TODO: Fix copyuser: discord.errors.CaptchaRequired: 400 Bad Request (error code: -1): Captcha required, at await self.bot.user.edit().
          Improve: Copy user's Rich Presence.


    @commands.command()
    async def copyuser(self, ctx):
        # Check if it's a valid user and return an error if not.
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                await ctx.message.edit(langs.fun_copy_user_fail[config_selfbot.lang])
                await asyncio.sleep(config_selfbot.deltime)
                await ctx.message.delete()
                return

        await ctx.message.edit("wait i save ur profile")

        # Save curent profile for the recover command.
        global user_backup
        global user_backup_profile
        global user_backup_avatar
        global user_backup_banner

        user_backup = await self.bot.fetch_user(self.bot.user.id)

        user_backup_profile = await user_backup.profile()
        await asyncio.sleep(0.7)
        user_backup_avatar = await user_backup.avatar.read()
        await asyncio.sleep(1)

        # Save banner only if bot user have nitro
        user_backup_banner = await user_backup.banner.read() if self.bot.user.premium_type is discord.PremiumType.nitro else None
        await asyncio.sleep(0.9) if self.bot.user.premium_type is discord.PremiumType.nitro else None

        # Fetch user's profile
        user = await self.bot.fetch_user(user.id)

        await ctx.message.edit("wait i copy the user")

        user_avatar = await user.avatar.read() if user.avatar else None
        await asyncio.sleep(1.2)
        user_banner = await user.banner.read() if user.banner else None
        await asyncio.sleep(1.4)
        user_profile = await user.profile()
        await asyncio.sleep(0.7)

        if self.bot.user.premium_type is discord.PremiumType.nitro and user.premium_type is discord.PremiumType.nitro:
            await self.bot.user.edit(#username=user.name, It require the account's password...
                                     global_name=user.display_name,
                                     avatar=user_avatar,
                                     banner=user_banner,
                                     bio=user_bio)
        elif self.bot.user.premium_type is discord.PremiumType.nitro:
            await self.bot.user.edit(#username=user.name, It require the account's password...
                                     global_name=user.display_name,
                                     avatar=user_avatar,
                                     bio=user_bio)
        else:
            await self.bot.user.edit(#username=user.name, It require the account's password...
                                     global_name=user.display_name,
                                     avatar=user_avatar,
                                     accent_colour=user.accent_colour,
                                     bio=user_bio)
        await ctx.message.edit("it works !!!")

    @commands.command()
    async def recover(self, ctx):
        await ctx.message.edit("wait i do the old profile")
        if self.bot.user.premium_type is discord.PremiumType.nitro:
            await self.bot.user.edit(#username=user.name, It require the account's password...
                                     global_name=user_backup.display_name,
                                     avatar=user_backup_avatar,
                                     banner=user_backup_banner,
                                     bio=user_backup_profile.bio)
        else:
            await self.bot.user.edit(#username=user.name, It require the account's password...
                                     global_name=user_backup.display_name,
                                     avatar=user_backup_avatar,
                                     accent_colour=user_backup.accent_colour,
                                     bio=user_backup_profile.bio)
        
        await ctx.message.edit("ui c bon bb")
        """