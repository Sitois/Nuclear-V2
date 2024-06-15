import discord
from discord.ext import commands
from colorama import Fore, Style, Back

from utils import log
import config_selfbot
import langs


class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.nitro_sniper: bool = config_selfbot.nitro_sniper

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.nitro_sniper and not ctx.author.id == self.bot.user.id:
            if "discord.gift/" in ctx.content:
                try:
                    gift_code = ctx.content.split("discord.gift/")[1].split()[0]

                    # Prevent from claiming certains unclaimable links.
                    if "-" in gift_code: 
                        # Prevent from claiming a promotional code.
                        return

                    if gift_code == "Udzwm3hrQECQBnEEFFCEwdSq":
                        # Prevent from claiming the custom "Nerd" nitro code.
                        return

                    if gift_code == "vhnuzE2YkNCZ7sfYHHKebKXB":
                        # Prevent from claiming the custom "No Nitro ?" nitro code.
                        return

                    if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code} | Channel: {ctx.channel.name}({ctx.channel.id}) | Guild: {ctx.guild.name}({ctx.guild.id}){Style.RESET_ALL}")
                    gift = await self.bot.fetch_gift(gift_code)
                    await gift.redeem(channel=ctx.channel)
                    log.success(f"discord.gift/{gift_code} {langs.nitro_sniper_valid[config_selfbot.lang]}")
                except discord.NotFound:
                    log.alert(f"discord.gift/{gift_code} {langs.nitro_sniper_invalid_code[config_selfbot.lang]}")
                except discord.HTTPException:
                    log.alert(f"discord.gift/{gift_code} {langs.nitro_sniper_claimed[config_selfbot.lang]}")

    @commands.command()
    async def nitrosniper(self, ctx: commands.Context):
        if not self.nitro_sniper:
            self.nitro_sniper = True
            await ctx.message.edit("🟢 Nitro Sniper **On**.", delete_after=config_selfbot.deltime)
        else:
            self.nitro_sniper = False
            await ctx.message.edit("🔴 Nitro Sniper **Off**.", delete_after=config_selfbot.deltime)

    @commands.command()
    async def lang(self, ctx: commands.Context):
        if config_selfbot.lang == "fr":
            config_selfbot.lang = "en"
            await ctx.message.edit("🟢 Language set to **English**.", delete_after=config_selfbot.deltime)
        else:
            config_selfbot.lang = "fr"
            await ctx.message.edit("🟢 Langue changée en **Français**.", delete_after=config_selfbot.deltime)