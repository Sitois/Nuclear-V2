import discord
from discord.ext import commands
import asyncio
import random

import config_selfbot
import fr_en

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

  🏮| __**General:**__ `{config_selfbot.prefix}general`
  🎤| __**{fr_en.help_voice[config_selfbot.lang]}:**__ `{config_selfbot.prefix}voice`
  🕹️| __**Rich Presence:**__ `{config_selfbot.prefix}presence`
  🎲| __**Fun:**__ `{config_selfbot.prefix}fun`
  🏯| __**Raid:**__ `{config_selfbot.prefix}raid`
  ⚙️| __**Config:**__ `{config_selfbot.prefix}config`""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def fun(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎲| __**Fun:**__
 `{config_selfbot.prefix}cat`: {fr_en.help_fun_cat[config_selfbot.lang]}.
 `{config_selfbot.prefix}good`: {fr_en.help_fun_good[config_selfbot.lang]}.
 `{config_selfbot.prefix}call`: {fr_en.help_fun_call[config_selfbot.lang]}.
 `{config_selfbot.prefix}gift`: {fr_en.help_fun_gift[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def config(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

⚙️| __**Config:**__
 `{config_selfbot.prefix}nitrosniper`: {fr_en.help_general_sniper[config_selfbot.lang]}.
 `{config_selfbot.prefix}restart`: {fr_en.help_config_restart[config_selfbot.lang]}.
 `{config_selfbot.prefix}stop`: {fr_en.help_config_stop[config_selfbot.lang]}.
 `{config_selfbot.prefix}lang`""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def raid(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏯| __**Raid:**__
 `{config_selfbot.prefix}spam`: Spam. (`{config_selfbot.prefix}spam` 2 hello).
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}kickall`: {fr_en.help_raid_kick[config_selfbot.lang]}.
 `{config_selfbot.prefix}banall`: {fr_en.help_raid_banall[config_selfbot.lang]}""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def general(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏮| __**GENERAL:**__
 `{config_selfbot.prefix}ping`: {fr_en.help_general_ping[config_selfbot.lang]}.
 `{config_selfbot.prefix}snipe`: {fr_en.help_general_snipe[config_selfbot.lang]}.
 `{config_selfbot.prefix}clear`: {fr_en.help_general_clear[config_selfbot.lang]}.
 `{config_selfbot.prefix}hype`: {fr_en.help_general_hype[config_selfbot.lang]} (bravery, brilliance, balance).
 `{config_selfbot.prefix}bio`: {fr_en.help_general_bio[config_selfbot.lang]}.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()

    @commands.command()
    async def voice(self, ctx):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
                           
🎤| __**Voice:**__
 `{config_selfbot.prefix}joinvc`: {fr_en.help_voice_vc[config_selfbot.lang]} (joinvc <voice_channel_id>).
 `{config_selfbot.prefix}joincam`: {fr_en.help_voice_cam[config_selfbot.lang]} (joincam <voice_channel_id>).
 `{config_selfbot.prefix}leavevc`: {fr_en.help_voice_leave[config_selfbot.lang]} (leavevc <voice_channel_id>.""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()