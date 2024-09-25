import discord
from discord.ext import commands
from colorama import Fore, Style, Back

from utils import log, lang
import config_selfbot


class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.nitro_sniper: bool = config_selfbot.nitro_sniper

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if self.nitro_sniper and not message.author.id == self.bot.user.id:
            if "discord.gift/" in message.content:
                try:
                    gift_code = message.content.split("discord.gift/")[1].split()[0]

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

                    if gift_code == "BMHmv4FWEM5WVGnHUHCYFKMx":
                        # Prevent from claiming the custom "Does he know ?" nitro code.
                        return

                    if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code} | Channel: {message.channel.name}({message.channel.id}) | Guild: {message.guild.name}({message.guild.id}){Style.RESET_ALL}")
                    gift = await self.bot.fetch_gift(gift_code)
                    await gift.redeem(channel=message.channel)
                    log.success(f"discord.gift/{gift_code} {lang.text('nitro_sniper_valid')}")
                except discord.NotFound:
                    log.alert(f"discord.gift/{gift_code} {lang.text('nitro_sniper_invalid_code')}")
                except discord.HTTPException:
                    log.alert(f"discord.gift/{gift_code} {lang.text('nitro_sniper_claimed')}")

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
        try:
            choice = ctx.message.content.split()[1].lower()
        except Exception:
            message = lang.text('config_lang_invalid')
            message += '\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()])
            await ctx.message.edit(message, delete_after=config_selfbot.deltime)
            return

        available_languages = [f"{list(item.values())[0]}" for item in lang.languages()]
        if choice in available_languages:
            config_selfbot.lang = choice
            await ctx.message.edit(f"🟢 **{choice}**.", delete_after=config_selfbot.deltime)
        else:
            message = lang.text('config_lang_invalid')
            message += '\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()])
            await ctx.message.edit(message)