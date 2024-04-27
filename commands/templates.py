import discord
from discord.ext import commands
import datetime
import time
import asyncio

import config_selfbot
import langs

class TemplatesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def use(self, ctx):
        today_date = datetime.datetime.today()
        choice = ctx.message.content.split()[1]
        if choice.lower() == "hi":
            assets = {"large_image": "mp:attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=65b93b47&is=65a6c647&hm=af5387b219eb9f9bf4cf7137758c4fad9da45a174305655ccb84c977a38dcd9f&=&format=webp&width=744&height=419",
                      "large_text": "heyyy",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Hi !",
                                        details="hi !!!!!!",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))
            
            await ctx.message.edit("👋 Template \"hi !\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "omori":
            assets = {"large_image": "mp:attachments/1135264530188992562/1177984303456604253/i9ja3eA.gif?ex=65b517df&is=65a2a2df&hm=ba4d90afb6d6f47adceb1dbdc8ae28435c20a0fc46dd52cd3b492b427d356987&=&width=559&height=419",
                      "large_text": "Omori",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Omori",
                                        details="In Game",
                                        state="Fighting a boss.",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("💡 Template \"Omori\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "cod":
            assets = {"large_image": "mp:attachments/1135264530188992562/1199007140782813284/5rr7SXS.png?ex=65c0f96a&is=65ae846a&hm=f92e8757ce026cb26fc3d6e44e2e9e02ccb2577e9f047e62f9891c0f5925c725&=&format=webp&quality=lossless",
                      "large_text": None,
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Call Of Duty: MWIII",
                                        details=langs.rpc_cod_details[config_selfbot.lang],
                                        state=langs.rpc_cod_state[config_selfbot.lang],
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🔫 Template \"Call Of Duty\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "youtube":
            assets = {"large_image": "mp:attachments/1135264530188992562/1197991793111863417/ILAO8CE.png?ex=65bd47cd&is=65aad2cd&hm=585fcd20ef938d1a7637732d5d251cba50c82024c980c5b1e785bb486e4c5f4a&=&format=webp&quality=lossless&width=419&height=419",
                      "large_text": None,
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="Youtube",
                                        details="Watching Videos",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🎦 Template \"YouTube\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "car":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198216462536552468/Wy5D92g.gif?ex=65be190a&is=65aba40a&hm=ee3adfbaccfb4a72ef71196d5b675aaef7df29a6f92f6841e4b161ed989aa783&=",
                      "large_text": None,
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="Drift Car",
                                        details="Watching DriftCar",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🏎️ Template \"Car\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "js":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198623222678179960/FYcrOR1.png?ex=65bf93dd&is=65ad1edd&hm=196ea799818a84abed3db5089be49eb2f470fe31e9ed5d984bfb6b898c868a4a&=&format=webp&quality=lossless",
                      "large_text": "Editing a JAVASCRIPT file",
                      "small_image": "mp:attachments/1135264530188992562/1198617586389225592/aBjaPbQ.png?ex=662da3dd&is=662c525d&hm=ffe2d4eb99afb709b3ce0955211d88db77ff00d29623279f4248c8dce6544cb0&=&format=webp&quality=lossless",
                      "small_text": "Visual Studio Code"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Visual Studio Code",
                                        details=f"🛠️ Editing {self.bot.user.name}.js (273 lines)",
                                        state="📂 Workspace: Nuclear-V2",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("👨‍💻 Template \"JavaScript\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "python":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=65bf8e9b&is=65ad199b&hm=d61ea94e9db57f790e49dab09a9390bd61e5362a14cd44738a9a2e8aa70092d0&=&format=webp&quality=lossless",
                      "large_text": "Editing a PYTHON file",
                      "small_image": "mp:attachments/1135264530188992562/1198617586389225592/aBjaPbQ.png?ex=662da3dd&is=662c525d&hm=ffe2d4eb99afb709b3ce0955211d88db77ff00d29623279f4248c8dce6544cb0&=&format=webp&quality=lossless",
                      "small_text": "Visual Studio Code"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Visual Studio Code",
                                        details=f"🛠️ Editing {self.bot.user.name}.py",
                                        state="📂 Workspace: Nuclear-V2",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("👨‍💻 Template \"Python\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "webdeck":
            assets = {"large_image": "mp:attachments/1135264530188992562/1197999417853218927/jj0PYp2.png?ex=65bd4ee6&is=65aad9e6&hm=ef2a47c5023678209436c74e3067469cf5c28143e5c12a3f714746fd03f1321e&=&format=webp&quality=lossless",
                      "large_text": "WebDeck Icon",
                      "small_image": "mp:attachments/1135264530188992562/1233765320406073475/fa1I0M7.png?ex=662e48fe&is=662cf77e&hm=964f0c85372beda0f0dfe864081dfb536fa611c664e63bb046ed1b13109d6875&=&format=webp&quality=lossless",
                      "small_text": "Lenochxd"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="WebDeck",
                                        details="github.com/Lenochxd/WebDeck",
                                        state="Using a with Free StreamDeck!",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("📱 Template \"WebDeck\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "nuclear":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=65be55bf&is=65abe0bf&hm=40a3c63ca07dfac28726eadae220a07412551a69deea021b73c24ae00933782e&=&format=webp&quality=lossless",
                      "large_text": "Nuclear $B",
                      "small_image": "mp:attachments/1135264530188992562/1206622218847518821/zQk1BeA.png?ex=662dc1c2&is=662c7042&hm=98548b094da0e982a9d33780630917197867b296889c2090f580d5ae46ba96e6&=&format=webp&quality=lossless&width=498&height=498",
                      "small_text": "On GitHub!"
                      }
            activity = discord.Activity(type=discord.ActivityType.streaming,
                                        name="Nuclear",
                                        details="Nuclear $B",
                                        state="github.com/Sitois/Nuclear",
                                        assets=assets,
                                        url=config_selfbot.streaming_url,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🌌 Template \"Nuclear\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "dark":
            assets = {"large_image": "mp:attachments/1135264530188992562/1205872002238382111/PNjYcIL.png?ex=65d9f2d1&is=65c77dd1&hm=37a71d4fc6c032214d71c8d94d7d6f6c99f8f9773c467cf8f7cc4d56a618da73&=&format=webp&quality=lossless",
                      "large_text": "☄",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.competing,
                                        name="☄",
                                        details=None,
                                        state=None,
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🖤 Template \"Dark\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "gta":
            assets = {"large_image": "mp:attachments/1135264530188992562/1200905385230475424/rhqvEdX.png?ex=65c7e14b&is=65b56c4b&hm=b375f98036eb15cedb369aff743ab040585f4777cc3756530e936fd5bbbb98d4&=&format=webp&quality=lossless&width=417&height=419",
                      "large_text": "Grand Theft Auto VI",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="GTA VI",
                                        details="Welcome to Vice City !",
                                        state="Playing SinglePlayer",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit(f"🔫 Template \"Grand Theft Auto VI\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            """
        elif choice.lower() == "reset": # RPC FROM ``rpc.json``
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name,
                                        details=config_selfbot.activity_details,
                                        state=config_selfbot.activity_state,
                                        timestamps={"start": time.time()},
                                        assets=config_selfbot.assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit(f"🔄️ RPC Reset.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            """
        elif choice.lower() == "default":
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name,
                                        details=config_selfbot.activity_details,
                                        state=config_selfbot.activity_state,
                                        timestamps={"start": time.time()},
                                        assets=config_selfbot.assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit(f"🔄️ RPC \"Default\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit("❌ Incorrect !")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()