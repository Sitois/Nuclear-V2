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
            assets = {"large_image": "mp:attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=6635d107&is=66347f87&hm=c17d967bcfd61a7ba16ef4c8023c304020c4606837c55695ad5e345ed49b5d19&=&format=webp&width=885&height=498",
                      "large_text": "heyyy",
                      "small_image": "mp:attachments/1135264530188992562/1194342294371958864/HAJ65By.png?ex=6635d130&is=66347fb0&hm=60f431cd87f309eb53a0eb33826c74a938b1c120fba1fa893be0c4fc68e3559a&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1233797659429699745/uBNj49H.png?ex=6635a75c&is=663455dc&hm=a4f446a7647f5a0d4de40f9b1793933305b83b201beaeb5ac113de99a18e7629&=&format=webp&quality=lossless",
                      "large_text": "Omori",
                      "small_image": "mp:attachments/1135264530188992562/1233797777436180511/4z6pDi6.png?ex=6635a778&is=663455f8&hm=16aca2b4784728b8619bfda7d1d8683979594e28320f42043da0aa6ba0586231&=&format=webp&quality=lossless&width=373&height=498",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1199007140782813284/5rr7SXS.png?ex=6635a62a&is=663454aa&hm=6ea5112845f37f94c6bea3c2fe07fb09cb56e8aedac0bf065fb83fddd4640d95&=&format=webp&quality=lossless",
                      "large_text": "Call Of Duty: MWIII",
                      "small_image": "mp:attachments/1135264530188992562/1234196811426693160/vVgU3XI.png?ex=6635c99a&is=6634781a&hm=da3c5a0d79c33087ce54160bb5fa1aba4197cc2081f887f0c6f07eb262c50dfc&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1197991793111863417/ILAO8CE.png?ex=6635e90d&is=6634978d&hm=08549ee489d03f53dffd2fe99d97c4f53e428f7622e95b0da517772cd8fbfefc&=&format=webp&quality=lossless&width=498&height=498",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1197994235174080602/gBXD4Yu.gif?ex=6635eb53&is=663499d3&hm=dddfd32478f3ede14cf047ebe626031ae250b4f275559298264745419445feb9&=",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1198623222678179960/FYcrOR1.png?ex=66363add&is=6634e95d&hm=2313d7b5fb3bd028ff6610b500cb27f443d674f967c05e20f5ebc1f2e4631364&=&format=webp&quality=lossless",
                      "large_text": "Editing a JAVASCRIPT file",
                      "small_image": "mp:attachments/1135264530188992562/1198617586389225592/aBjaPbQ.png?ex=6636359d&is=6634e41d&hm=72ac7fc0bf606630d07ee156499d4d96fc4802d94dc1d802f8e45fcfb0574e5a&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=6636359b&is=6634e41b&hm=119d3ee4a2e0122befbf54a5d428cb23fc3b601b238eb788454b7ba0921b6e84&=&format=webp&quality=lossless",
                      "large_text": "Editing a PYTHON file",
                      "small_image": "mp:attachments/1135264530188992562/1198617586389225592/aBjaPbQ.png?ex=6636359d&is=6634e41d&hm=72ac7fc0bf606630d07ee156499d4d96fc4802d94dc1d802f8e45fcfb0574e5a&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1197999417853218927/jj0PYp2.png?ex=6635f026&is=66349ea6&hm=5ee28fed0533b393769c2415b53637965bbccf26e94998841e2385e17f838d3d&=&format=webp&quality=lossless",
                      "large_text": "WebDeck Icon",
                      "small_image": "mp:attachments/1135264530188992562/1233765320406073475/fa1I0M7.png?ex=663631fe&is=6634e07e&hm=b3a7128303d476b6781edfca7ad4320e83ee7c2cf73777eb63719d4e92aefe5d&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=6635a57f&is=663453ff&hm=a4288084bd5192bf12fee61449669087b8f77662d402701ee1e78307c6d57b9b&=&format=webp&quality=lossless",
                      "large_text": "github.com/Sitois/Nuclear-V2",
                      "small_image": "mp:attachments/1135264530188992562/1206622218847518821/zQk1BeA.png?ex=6635aac2&is=66345942&hm=434aec4a3ca30b1c7f0a635355f84796257cfcf164cad00074489ca8e171084e&=&format=webp&quality=lossless&width=498&height=498",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1205872002238382111/PNjYcIL.png?ex=66363bd1&is=6634ea51&hm=2cdd456feda072bc78b62bb34969f038e4336cd9e2e6dbc2401f31f686607057&=&format=webp&quality=lossless",
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
            assets = {"large_image": "mp:attachments/1135264530188992562/1200905385230475424/rhqvEdX.png?ex=6637480b&is=6635f68b&hm=0a6170c72203ffc2f683228c884b434b585de6030082daeb787046a99c6ec464&=&format=webp&quality=lossless",
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
        elif choice.lower() == "tiktok":
            assets = {"large_image": "mp:attachments/1135264530188992562/1235997837255376949/ssfXx3o.png?ex=66366830&is=663516b0&hm=44aff149f2a3cffca4ba34289cb1cc8e211545ad2ba649929af4d502bd0131ba&=&format=webp&quality=lossless&width=498&height=498",
                      "large_text": "TikTok",
                      "small_image": None,
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="TikTok",
                                        details="ForYou page",
                                        state=None,
                                        timestamps={"start": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=activity,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("📱 Template \"TikTok\".")
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

            await ctx.message.edit("🔄️ RPC Reset.")
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

            await ctx.message.edit("🔄️ RPC \"Default\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif choice.lower() == "clear":
            await self.bot.change_presence(status=discord.Status.idle,
                                    activity=None,
                                    afk=True,
                                    idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

            await ctx.message.edit("❌ RPC \"Clear\".")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            await ctx.message.edit(f"❌ {langs.incorrect[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()