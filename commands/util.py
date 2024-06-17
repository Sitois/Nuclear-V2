import discord
from discord.ext import commands
import asyncio
import time

from utils import random_cooldown
import config_selfbot
import langs


class UtilsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.sniped_messages: dict = {}

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
    async def snipe(self, ctx: commands.Context):
        sniped_message = self.sniped_messages.get(ctx.channel.id)
        if sniped_message:
            images_text = "".join(sniped_message['images']) if not sniped_message['images'] is None else langs.empty[config_selfbot.lang]
            await ctx.message.edit(f"""Je t'ai eu !!!
<@{sniped_message['author_id']}> as envoillé : ''** {images_text}{sniped_message['content']} **''
Malheureusement, cela a été supprimé <t:{sniped_message['time']}:R>...""")
        else:
            await ctx.message.edit(langs.error_no_message_snipe[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def snipepic(self, ctx: commands.Context):
        sniped_message = self.sniped_messages.get(ctx.channel.id)
        if sniped_message:
            images_text = "".join(sniped_message['images']) if not sniped_message['images'] is None else langs.empty[config_selfbot.lang]
            await ctx.message.edit(f"""Je t'ai eu !!!
<@{sniped_message['author_id']}> as envoillé une image ! ( {images_text} )
Malheureusement, cela a été supprimé <t:{sniped_message['time']}:R>...""")
        else:
            await ctx.message.edit(langs.error_no_picture_snipe[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def clear(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        try:
            str_amount = message_split[1]
        except Exception:
            str_amount = "19"

        try:
            amount = int(str_amount) + 1
        except Exception:
            await ctx.message.edit(langs.spam_invalid[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(f"> 🌌 **{config_selfbot.selfbot_name}**", delete_after=1.7)

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

    @commands.command()
    async def hype(self, ctx: commands.Context):
        house = ctx.message.content.split()[1]
        if house == "balance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.balance)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``", delete_after=config_selfbot.deltime)
        elif house == "bravery":
            await self.bot.user.edit(house=discord.HypeSquadHouse.bravery)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``", delete_after=config_selfbot.deltime)
        elif house == "brilliance":
            await self.bot.user.edit(house=discord.HypeSquadHouse.brilliance)
            await ctx.message.edit(f"🪄 HypeSquad {langs.hype_command[config_selfbot.lang]} ``{house}``", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(langs.hype_fail[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.message.edit(f"🏓 Pong ! (Ping: **{round(self.bot.latency * 1000)}ms**)", delete_after=config_selfbot.deltime)

    @commands.command()
    async def bio(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        new_bio = ctx.message.content.replace(f"{message_split[0]} ", "")
        await self.bot.user.edit(bio=new_bio)
        await ctx.message.edit(f"📖 Bio {langs.bio_command[config_selfbot.lang]} \"`{new_bio}`\"", delete_after=config_selfbot.deltime)

    @commands.command()
    async def userinfo(self, ctx: commands.Context):
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


        await ctx.message.edit(message, delete_after=config_selfbot.deltime)

    # TODO:
    # Improvement: Add user's status in the `useinfo` command.
    # Add: `serverinfo` command that will return informations about the server.
    # Add: `botinvite` command that will return a botinvite using the given bot ID.
    # Add: `support` command that will return support links.
