import discord
from discord.ext import commands
import datetime
import time
import asyncio
import rpc

import config_selfbot
import langs

class RichPresenceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.today_date = datetime.datetime.today()

    @commands.command()
    async def rpc_details(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_details", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            
        await ctx.message.edit(f"🕹️| Details: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_name(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_name", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
 
        await ctx.message.edit(f"🕹️| Name: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_state(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_state", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| State: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_url(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("streaming_url", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Stream URL: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_large_image(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("large_image", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Large Image: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_large_text(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("large_text", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Large image text: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_small_image(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("small_image", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Small Image: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_small_text(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("small_text", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Small image text: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_button_text_one(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_button_one", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Button One Text: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_button_text_two(self, ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")

        rpc.edit_variable_json("activity_button_two", message_content)

        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️|Button Text Two: `{message_content}`")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    """ # WAITING FOR DISCORD.PY-SELF TO ADD BUTTON LINKS
    @commands.command()
    async def rpc_button_link_one(ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        rpc.edit_variable_json("activity_button_one_answer", message_content)
        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await ctx.message.edit(f"🕹️| Button One Link: `{message_content}`")
        await asyncio.sleep(deltime)
        await ctx.message.delete()

    @commands.command()
    async def rpc_button_link_two(ctx):
        message_split = ctx.message.content.split()
        message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        rpc.edit_variable_json("activity_button_two_answer", message_content)
        assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                  "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                  "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                  "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                 }
        activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
        await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

        await bot.change_presence(status=config_selfbot.status_activity if rpc.read_variable_json("status_activity") == "VOID" else rpc.read_variable_json("status_activity"),
                                afk=afk,
                                activity=selfcord.Activity.Game(name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                                                    details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                                                    state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                                                    buttons={config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"): config_selfbot.activity_button_one_answer if rpc.read_variable_json("activity_button_one_answer") == "VOID" else rpc.read_variable_json("activity_button_one_answer"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two"): config_selfbot.activity_button_two_answer if rpc.read_variable_json("activity_button_two_answer") == "VOID" else rpc.read_variable_json("activity_button_two_answer")},
                                                                    key=config_selfbot.image_key if rpc.read_variable_json("image_key") == "VOID" else rpc.read_variable_json("image_key"), 
                                                                    application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                    )
                                                                    )
        await ctx.message.edit(f"🕹️| Button Link Two: `{message_content}`")
        await asyncio.sleep(deltime)
        await ctx.message.delete()
    """

    @commands.command()
    async def rpc_type(self, ctx):
        choice = ctx.message.content.split()[1]
        if choice.lower() == "game":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            timestamps={"start": time.time()},
                                            assets=assets,
                                            application_id=config_selfbot.application_id,
                                            buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("🎮 **Type:** \"Game\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "watch":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            timestamps={"start": time.time()},
                                            assets=assets,
                                            application_id=config_selfbot.application_id,
                                            buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("📺 **Type:** \"Watch\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "competing":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.competing,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            assets=assets,
                                            application_id=config_selfbot.application_id,
                                            buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("🎉 **Type:** \"Competing\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "listen":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.listening,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            timestamps={"start": time.time()},
                                            assets=assets,
                                            application_id=config_selfbot.application_id,
                                            buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("🎧 **Type:** \"Listen\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "stream":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.streaming,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            url=config_selfbot.streaming_url if rpc.read_variable_json("streaming_url") == "VOID" else rpc.read_variable_json("streaming_url"),
                                            assets=assets,
                                            application_id=config_selfbot.application_id,
                                            buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("⭕ **Type:** \"Stream\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "xbox":
            activity = discord.Activity(type=discord.ActivityType.playing,
                                            name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                            details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                            state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                            timestamps={"start": time.time()},
                                            assets=None,
                                            application_id=438122941302046720,
                                            buttons=None)

            await self.bot.change_presence(status=discord.Status.idle,
                                        activity=activity,
                                        afk=True,
                                        idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))

            await ctx.message.edit("🎮 **Type:** \"Xbox\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(f"❌ {langs.incorrect[config_selfbot.lang]} (`game` / `watch` / `listen` / `stream` / `competing` / `xbox`)")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()