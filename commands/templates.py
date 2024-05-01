import discord
from discord.ext import commands
import datetime
import time
import asyncio
import rpc

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
            assets = {"large_image": "mp:attachments/1135264530188992562/1194342294371958864/HAJ65By.png?ex=662f39b0&is=662de830&hm=a006c6aa09c89f7be46b65340405ed423e0bfb30b584877a4c4d075f37ea32b6&=&format=webp&quality=lossless",
                      "large_text": "heyyy",
                      "small_image": "mp:attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=662f3987&is=662de807&hm=8bac90f1321ab6b4535c78cd110015e66f2387eb38aac122b681668f24058a40&=&format=webp&width=885&height=498",
                      "small_text": "hiii"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Hi !",
                                        details="hi !!!!!!",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))
            
            await ctx.message.edit("👋 Template \"hi !\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "omori":
            assets = {"large_image": "mp:attachments/1135264530188992562/1233797659429699745/uBNj49H.png?ex=662e671c&is=662d159c&hm=081493b0d766c8f1cf90cb6d230bdd4d633386e6cb99ebd701bbae8d854edf46&=&format=webp&quality=lossless",
                      "large_text": "Omori",
                      "small_image": "mp:attachments/1135264530188992562/1233797777436180511/4z6pDi6.png?ex=662e6738&is=662d15b8&hm=d7f9767e68ad97115b2032957aefd43933b67e8cd71bc2b17c36b1fdc608e0c0&=&format=webp&quality=lossless&width=373&height=498",
                      "small_text": "The bulb."
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Omori",
                                        details="In Game",
                                        state="Fighting a boss.",
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("💡 Template \"Omori\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "cod":
            assets = {"large_image": "mp:attachments/1135264530188992562/1199007140782813284/5rr7SXS.png?ex=662fb76a&is=662e65ea&hm=74dc022b8cdb28235aa47517b015a9ea9005ae4ee2e791f172790a673a437a2f&=&format=webp&quality=lossless",
                      "large_text": "Call Of Duty: MWIII",
                      "small_image": "mp:attachments/1135264530188992562/1234196811426693160/vVgU3XI.png?ex=662fdada&is=662e895a&hm=308cd37825d203d89472f24fa1f89d165c5cc88b544679d7116becc59fb03028&=&format=webp&quality=lossless",
                      "small_text": "Battle Pass level 21"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Call Of Duty: MWIII",
                                        details=langs.rpc_cod_details[config_selfbot.lang],
                                        state=langs.rpc_cod_state[config_selfbot.lang],
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🔫 Template \"Call Of Duty\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "youtube":
            assets = {"large_image": "mp:attachments/1135264530188992562/1197991793111863417/ILAO8CE.png?ex=662f518d&is=662e000d&hm=33f7c2c5e2fba654684dff9298fb4c530cf0c5b48fc5b636b9dbb8eed1c71cc6&=&format=webp&quality=lossless&width=498&height=498",
                      "large_text": "YouTube",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="YouTube",
                                        details="Watching Videos",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🎦 Template \"YouTube\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "car":
            assets = {"large_image": "mp:attachments/1135264530188992562/1197994235174080602/gBXD4Yu.gif?ex=662f53d3&is=662e0253&hm=ec7d176cd7a822deaa503de324feba9cce4655ddf68588b034a752c5bde85585&=",
                      "large_text": "Drift Car",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🏎️ Template \"Car\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "js":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198623222678179960/FYcrOR1.png?ex=662efa9d&is=662da91d&hm=3ec239c03ac70b20678be0006aa9a469f5a9836dc581b4651429e12caa7cfa87&=&format=webp&quality=lossless",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("👨‍💻 Template \"JavaScript\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "python":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=662ef55b&is=662da3db&hm=66825352ae51d1f30e0f99a551a31d6c09e7fa0c716050e77d67497fbac19392&=&format=webp&quality=lossless",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("👨‍💻 Template \"Python\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "webdeck":
            assets = {"large_image": "mp:attachments/1135264530188992562/1197999417853218927/jj0PYp2.png?ex=662f58a6&is=662e0726&hm=60c39acba6a4b41e5c643100bb3671320407a02eeb901ed22c7aa1e89584a0d8&=&format=webp&quality=lossless",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("📱 Template \"WebDeck\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "nuclear":
            assets = {"large_image": "mp:attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=662f0dff&is=662dbc7f&hm=71b8aabd5af9c550d925999b2aa17422ad77d1cdc5a65cab906755cd11bb861b&=&format=webp&quality=lossless",
                      "large_text": "github.com/Sitois/Nuclear-V2",
                      "small_image": "mp:attachments/1135264530188992562/1206622218847518821/zQk1BeA.png?ex=662dc1c2&is=662c7042&hm=98548b094da0e982a9d33780630917197867b296889c2090f580d5ae46ba96e6&=&format=webp&quality=lossless&width=498&height=498",
                      "small_text": "On GitHub!"
                      }
            activity = discord.Activity(type=discord.ActivityType.streaming,
                                        name="Nuclear",
                                        details="Nuclear $B",
                                        state="Best free open-source $B!",
                                        assets=assets,
                                        url=config_selfbot.streaming_url,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🌌 Template \"Nuclear\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "dark":
            assets = {"large_image": "mp:attachments/1135264530188992562/1205872002238382111/PNjYcIL.png?ex=662daa11&is=662c5891&hm=fd617583fee2ee05c504c282364ef5c30dbd54c9c252ba0b4179888c37ad08af&=&format=webp&quality=lossless",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🖤 Template \"Dark\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "gta":
            assets = {"large_image": "mp:attachments/1135264530188992562/1200905385230475424/rhqvEdX.png?ex=662e0d8b&is=662cbc0b&hm=fc34f39c588683ed87a5e2fe6ea3917c5f1cf15cd8ee4e4ca175238669271367&=&format=webp&quality=lossless",
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
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("🔫 Template \"Grand Theft Auto VI\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "reset":
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
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit(f"🔄️ RPC Reset.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
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