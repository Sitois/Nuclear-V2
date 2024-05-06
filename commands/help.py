import discord
from discord.ext import commands
import asyncio
import random

import config_selfbot
import langs

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        poetry = {
            "fr": [
            "Jour meilleur n'existe qu'avec douleur.",
            "La seule personne que vous êtes destiné à devenir est la personne que vous décidez d'être.",
            "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.",
            "L'échec est le fondement de la réussite.",
            "Ne rêvez pas votre vie, vivez vos rêves.",
            "Crois en toi, et les autres suivront.",
            "Sois le changement que tu veux voir dans le monde.",
            "Poursuis tes rêves, ils connaissent le chemin.",
            "La vie récompense l'action.",
            "Tu es plus fort que tu ne le crois.",
            "Le succès commence par l'action.",
            "La persévérance bat le talent.",
            "Ne remettez pas à demain.",
            "Chaque effort compte.",
            "Les montagnes les plus hautes ont les pentes les plus raides.",
            "Les éclats de lumière percent l'obscurité la plus profonde."
            ],
            "en": [
            "Your attitude determines your direction.",
            "Progress, not perfection.",
            "Embrace the challenges, for they are the stepping stones to success.",
            "Embrace failure as a stepping stone, not a stumbling block.",
            "The only limits that exist are the ones you place on yourself.",
            "Courage is not the absence of fear but the triumph over it.",
            "Dreams don't work unless you do",
            "Opportunities don't happen. You create them.",
            "Don't wait for the perfect moment; take the moment and make it perfect.",
            "The only way to do great work is to love what you do.",
            "Believe you can, and you're halfway there.",
            "Don't watch the clock; do what it does. Keep going"
            ],
        }


        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
  ☄ "{random.choice(poetry[config_selfbot.lang])}" ☄

  📂| __**Utils:**__ `{config_selfbot.prefix}utils`
  🎤| __**{langs.help_voice[config_selfbot.lang]}:**__ `{config_selfbot.prefix}voice`
  🕹️| __**Rich Presence:**__ `{config_selfbot.prefix}presence`
  📖| __**Templates:**__ `{config_selfbot.prefix}templates`
  🎲| __**Fun:**__ `{config_selfbot.prefix}fun`
  🏯| __**Raid:**__ `{config_selfbot.prefix}raid`
  🔧| __**Tools:**__ `{config_selfbot.prefix}tools`
  ⚙️| __**Config:**__ `{config_selfbot.prefix}config`""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def tools(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🔧| __**Tools:**__
 `{config_selfbot.prefix}closealldm`: {langs.help_tools_close_dm[config_selfbot.lang]}.
 `{config_selfbot.prefix}botclosedm`: {langs.help_tools_close_dm_bots[config_selfbot.lang]}.
 `{config_selfbot.prefix}dmall`: {langs.help_raid_dmall[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def fun(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎲| __**Fun:**__
 `{config_selfbot.prefix}cat`: {langs.help_fun_cat[config_selfbot.lang]}.
 `{config_selfbot.prefix}good`: {langs.help_fun_good[config_selfbot.lang]}.
 `{config_selfbot.prefix}call`: {langs.help_fun_call[config_selfbot.lang]}.
 `{config_selfbot.prefix}gift <random/nerd/poor>`: {langs.help_fun_gift[config_selfbot.lang]}.
 `{config_selfbot.prefix}hack`: {langs.help_fun_hack[config_selfbot.lang]}.
 `{config_selfbot.prefix}howfemboy`: {langs.help_fun_femboy[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def config(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

⚙️| __**Config:**__
 `{config_selfbot.prefix}nitrosniper`: {langs.help_general_sniper[config_selfbot.lang]}.
 `{config_selfbot.prefix}restart`: {langs.help_config_restart[config_selfbot.lang]}.
 `{config_selfbot.prefix}stop`: {langs.help_config_stop[config_selfbot.lang]}.
 `{config_selfbot.prefix}lang`""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def raid(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏯| __**Raid:**__
 `{config_selfbot.prefix}spam`: Spam. (`{config_selfbot.prefix}spam` 2 hello).
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}kickall`: {langs.help_raid_kick[config_selfbot.lang]}.
 `{config_selfbot.prefix}banall`: {langs.help_raid_banall[config_selfbot.lang]}""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def utils(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

📂| __**Utils:**__
 `{config_selfbot.prefix}ping`: {langs.help_general_ping[config_selfbot.lang]}.
 `{config_selfbot.prefix}snipe`: {langs.help_general_snipe[config_selfbot.lang]}
 `{config_selfbot.prefix}clear`: {langs.help_general_clear[config_selfbot.lang]}
 `{config_selfbot.prefix}hype`: {langs.help_general_hype[config_selfbot.lang]} (bravery, brilliance, balance).
 `{config_selfbot.prefix}bio`: {langs.help_general_bio[config_selfbot.lang]}.
 `{config_selfbot.prefix}userinfo`: {langs.help_general_user_info[config_selfbot.lang]}""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def voice(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
                           
🎤| __**Voice:**__
 `{config_selfbot.prefix}joinvc <voice_channel_id>`: {langs.help_voice_vc[config_selfbot.lang]}.
 `{config_selfbot.prefix}joincam <voice_channel_id>`: {langs.help_voice_cam[config_selfbot.lang]}.
 `{config_selfbot.prefix}leavevc`: {langs.help_voice_leave[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def tuto(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

    🎮| __**Rich Presence Image Tutorial:**__
    {langs.tutorial_rpc[config_selfbot.lang]}""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def templates(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

    📖| __**Templates:**__
    `{config_selfbot.prefix}use default`: {langs.template_help_default[config_selfbot.lang]}
    `{config_selfbot.prefix}use reset`: {langs.template_help_reset[config_selfbot.lang]}
    `{config_selfbot.prefix}use clear`: {langs.template_help_clear[config_selfbot.lang]}
    `{config_selfbot.prefix}use hi`: {langs.template_help_hi[config_selfbot.lang]}
    `{config_selfbot.prefix}use webdeck`: {langs.template_help_webdeck[config_selfbot.lang]}
    `{config_selfbot.prefix}use omori`: {langs.template_help_omori[config_selfbot.lang]}
    `{config_selfbot.prefix}use youtube`: {langs.template_help_youtube[config_selfbot.lang]}
    `{config_selfbot.prefix}use car`: {langs.template_help_car[config_selfbot.lang]}
    `{config_selfbot.prefix}use nuclear`: {langs.template_help_self[config_selfbot.lang]}
    `{config_selfbot.prefix}use dark`: {langs.template_help_dark[config_selfbot.lang]}
    `{config_selfbot.prefix}use python`: {langs.template_help_python[config_selfbot.lang]}
    `{config_selfbot.prefix}use js`: {langs.template_help_js[config_selfbot.lang]}
    `{config_selfbot.prefix}use cod`: {langs.template_help_cod[config_selfbot.lang]}
    `{config_selfbot.prefix}use gta`: {langs.template_help_gta[config_selfbot.lang]}
    `{config_selfbot.prefix}use tiktok`: {langs.template_help_tiktok[config_selfbot.lang]}""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def presence(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

    🕹️| __**Rich Presence Settings:**__                
    `{config_selfbot.prefix}rpc_name`: {langs.rpc_name_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_details`: {langs.rpc_details_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_state`: {langs.rpc_state_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_url`: {langs.rpc_url_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_type`: {langs.rpc_type_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_large_image`: {langs.rpc_large_image_translate[config_selfbot.lang]}. (`{config_selfbot.prefix}tuto` !)
    `{config_selfbot.prefix}rpc_large_text`: {langs.rpc_large_text_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_small_image`: {langs.rpc_small_image_translate[config_selfbot.lang]}. (`{config_selfbot.prefix}tuto` !)
    `{config_selfbot.prefix}rpc_small_text`: {langs.rpc_small_text_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_button_text_one`: {langs.rpc_button_text_one_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_button_link_one`: {langs.rpc_button_link_one_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_button_text_two`: {langs.rpc_button_text_two_translate[config_selfbot.lang]}.
    `{config_selfbot.prefix}rpc_button_link_two`: {langs.rpc_button_link_two_translate[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()