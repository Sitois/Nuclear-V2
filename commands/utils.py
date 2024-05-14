import discord
from discord.ext import commands
import asyncio
import random
import time

import config_selfbot
import langs

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum*100000,maximum*100000) / 100000
    return cooldown

class UtilsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sniped_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.id == self.bot.user.id:
            try:
                attachments_urls = [attachment.url for attachment in message.attachments]
                self.sniped_messages[message.channel.id] = {
                    'author': message.author,
                    'content': message.content,
                    'images': attachments_urls if message.attachments else None,
                    'time': round(time.time())
                }
            except Exception:
                return

    @commands.command()
    async def snipe(self, ctx):
        sniped_message = self.sniped_messages.get(ctx.channel.id)
        if sniped_message:
            images_text = ", ".join(sniped_message['images']) if not sniped_message['images'] is None else langs.empty[config_selfbot.lang]
            await ctx.message.edit(f"""__**🔫 Sniper:**__

🗣️ {langs.author[config_selfbot.lang]}: {sniped_message['author']}
📩 Message:
```txt
{sniped_message['content']}
```
🖼️ Images: {images_text}
⌚ {langs.time_snipe[config_selfbot.lang]}: <t:{sniped_message['time']}:R>""")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(langs.error_no_message_snipe[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def clear(self, ctx):
        message_split = ctx.message.content.split()
        try:
            str_amount = message_split[1]
        except Exception:
            str_amount = "19"

        try:
            amount = int(str_amount) + 1
        except Exception:
            await ctx.message.edit(langs.spam_invalid[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return
        
        async for message in ctx.channel.history(limit=amount):
            if message.author.id == self.bot.user.id:
                await message.delete()
                await asyncio.sleep(random_cooldown(0.4, 1))
        """
        This can hardly rate limit you because user don't have access to bulk-message-delete endpoint.
        
        else:
            def is_me(m):
                return m.author.id == self.bot.user.id
            await ctx.channel.purge(limit=amount, check=is_me)
        """

        await ctx.channel.send(f"> 🌌 **{config_selfbot.selfbot_name}**", delete_after=1.4)

    @commands.command()
    async def hype(self, ctx):
        house = ctx.message.content.split()[1]
        if house == "balance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.balance)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif house == "bravery":
            await self.bot.user.edit(house=discord.HypeSquadHouse.bravery)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif house == "brilliance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.brilliance)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(langs.hype_fail[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.edit(f"🏓 Pong ! (Ping: **{round(self.bot.latency * 1000)}ms**)")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def bio(self, ctx):
        message_split = ctx.message.content.split()
        new_bio = ctx.message.content.replace(f"{message_split[0]} ", "")
        await self.bot.user.edit(bio=new_bio)
        await ctx.message.edit(f"📖 Bio {langs.bio_command[config_selfbot.lang]} \"`{new_bio}`\"")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def userinfo(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author

        user = await self.bot.fetch_user(user.id) # We can use ``await self.bot.get_user(user.id)``; that will do less api requests; but it's necessary to fetch_user for the banner.

        if ctx.guild:
            guild = ctx.guild
            member = guild.get_member(user.id)
            roles = [role.name for role in member.roles[1:] if role.name != '@everyone'] if member else []
        else:
            roles = []

        message = f"""🗒️| {langs.info_title[config_selfbot.lang]} <@{user.id}> :
>  👤| {langs.info_global[config_selfbot.lang]}: `{user.global_name}`
>  🌐| {langs.info_username[config_selfbot.lang]}: `{user.name}`
>  🆔| ID: `{user.id}`
>  🌈| {langs.info_banner[config_selfbot.lang]}: {"[" + langs.info_banner_link[config_selfbot.lang] + "](" + user.banner.url + ")" if not user.banner is None else "`" + langs.empty[config_selfbot.lang] + "`"}
>  📅| {langs.info_created_at[config_selfbot.lang]}: `{user.created_at.strftime('%Y/%m/%d %H:%M:%S')}`
>  🖼️| {langs.info_avatar[config_selfbot.lang]}: {"[" + langs.info_avatar_link[config_selfbot.lang] + "](" + user.avatar.url + ")" if not user.avatar is None else "`" + langs.empty[config_selfbot.lang] + "`"}"""

        if roles:
            message += f"\n>  🎭| {langs.info_roles[config_selfbot.lang]}: {', '.join(roles)}"


        await ctx.message.edit(message)
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()