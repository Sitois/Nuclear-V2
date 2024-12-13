#!/usr/bin/python3
# -*- coding: utf-8 -*-
print("========================")
print("LAUNCHING NUCLEAR-V2")
import subprocess
print("10%, Importing required modules...")
try:
    import sys, os, platform
    # load icons(fixed error when iconloader dll crashes the program)
    os.system("nuclear_icon.png")
    import ctypes
    import datetime, time
    import threading
    import asyncio
    import config_selfbot
    print("25%, Loaded required python-integrated libraries.")
    from utils import rpc, log, __version__, lang
    print("35%, Loading commands...")
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    print("50%, Loading discord.py-self...")
    import discord
    from discord.ext import commands
    import nacl
    print("75%, Imported requried modules!")
except ImportError:
    import sys, os
    print("++++++++++++++++++++++++")
    print("MISSING REQUIRED LIBRARIES")
    print("Downloading missing libraries from pip ...")
    if os.name == 'nt':
     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
     subprocess.check_call([sys.executable, "-m", "pip3", "install", '-r' , 'requirements.txt'])
    print("++++++++++++++++++++++++")
    import platform
    import ctypes
    import datetime, time
    import threading
    import asyncio
    import config_selfbot
    print("25%, Loading required python-integrated libraries...")
    from utils import rpc, log, __version__, lang
    print("35%, Loading commands...")
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    print("50%, Loading discord.py-self...")
    import discord
    from discord.ext import commands
    import nacl
    print("75%, Imported requried modules!")

print("100%")
print("========================")

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

print(fr"""{Fore.LIGHTCYAN_EX}$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  v{__version__}{Style.RESET_ALL}""")


# Change terminal title
def set_terminal_title(title: str):
    """Changes the terminal title."""
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

try:
   set_terminal_title("| Nuclear-V2 Selfbot |")
except Exception as e:
   log.warning(f"Error while trying to change the terminal name: {e}")


# Ask for required informations if not already set up in config file.
if config_selfbot.token == "":
    config_selfbot.token = input("Token: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fr"""{Fore.LIGHTCYAN_EX}$$\   $$\                     $$\                               
    $$$\  $$ |                    $$ |                              
    $$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
    $$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
    $$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
    $$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
    $$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
    \__|  \__| \______/  \_______|\__| \_______| \_______|\__|  v{__version__}{Style.RESET_ALL}""")


if config_selfbot.lang == "":
    print("Language Choice:")
    print('\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()]))
    config_selfbot.lang = input("Lang: ")

if config_selfbot.prefix == "":
    config_selfbot.prefix = input("Prefix: ")

if config_selfbot.selfbot_name == "":
    config_selfbot.selfbot_name = input("Selfbot name: ")


def check_latest_version(repo_owner: str, repo_name: str):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

check_loop = True

# Check if it's a developement version, if it is, disable UpdateChecker
try:
    if float(__version__) > float(check_latest_version('Sitois', 'Nuclear-V2').strip('v')):
        log.warning(f"{lang.text('unstable_version')} https://github.com/Sitois/Nuclear-V2/releases/latest")
        check_loop = False
except Exception:
    # Avoid crashes if the version is i.g.: 'v1.1.1'.
    pass

# Prevent from starting the selfbot with another discord library
if discord.__title__ != "discord.py-self":
    log.critical(lang.text('error_discord_version'))
    exit()

# Prevent from starting the selfbot with the broken pip version
if discord.__version__.startswith("2.0.0"):
    log.critical(lang.text('error_discord_version'))
    exit()


def call_check_repo():
    repo_owner = "Sitois"
    repo_name = "Nuclear-V2"
    while True:
        latest_version = check_latest_version(repo_owner, repo_name)
        if latest_version:
            if not latest_version == f"v{__version__}":
                log.info(f"""{lang.text('error_check_version')} ({latest_version}) {lang.text('error_check_version_two')} https://github.com/{repo_owner}/{repo_name}/releases/tag/{latest_version}
{lang.text('error_check_version_three')} v{__version__}""")
            time.sleep(3600)

def run_in_background():
    thread = threading.Thread(target=call_check_repo, daemon=True)
    thread.start()

if check_loop:
    try:
        run_in_background()
    except Exception as e:
        log.warning(f"Error while trying to check the last Nuclear version: {e}")

log.start(lang.text('start_text'))



####################
#  start           #
#   setup     !!!  #
####################
today_date = datetime.datetime.today()

# TODO: Finish captcha handler
"""
API_KEY = 'YOUR_API_KEY'


solver = twocaptcha.TwoCaptcha(API_KEY)

async def handle_captcha(exc: discord.CaptchaRequired, bot: commands.Bot) -> str:
    result = solver.solve_captcha(site_key=exc.sitekey, page_url="https://discord.com/")
    return result['code']
"""

# Define the bot instance
bot = commands.Bot(command_prefix=config_selfbot.prefix,
                   self_bot=True,
                   #captcha_handler=handle_captcha,
                   help_command=None)

# Get the start timestamp to put the time it took to start at on_ready()
start_time = time.time()

@bot.event
async def on_ready():
    global today_date
    global start_time

    log.separate_yellow()

    # Load commands from cogs
    try:
        await bot.add_cog(HelpCommands(bot))
        log.success(f"HelpCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"HelpCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(FunCommands(bot))
        log.success(f"FunCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"FunCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(UtilsCommands(bot))
        log.success(f"UtilsCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"UtilsCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(VoiceCommands(bot))
        log.success(f"VoiceCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"VoiceCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(ConfigCommands(bot))
        log.success(f"ConfigCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"ConfigCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(RaidCommands(bot))
        log.success(f"RaidCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"RaidCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(ToolsCommands(bot))
        log.success(f"ToolsCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"ToolsCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(TemplatesCommands(bot))
        log.success(f"TemplatesCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"TemplatesCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(RichPresenceCommands(bot))
        log.success(f"RichPresenceCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"RichPresenceCommands: {lang.text('cog_fail')} {e}")
    try:
        await bot.add_cog(BackupCommands(bot))
        log.success(f"BackupCommands: {lang.text('cog_success')}")
    except Exception as e:
        log.fail(f"BackupCommands: {lang.text('cog_fail')} {e}")

    # Print when the bot is ready to receive and answer to commands
    log.alert(f"{lang.text('ready_text')} @{bot.user.name} ({bot.user.id}), {lang.text('ready_text_two')} {round(time.time()) - round(start_time)} {lang.text('ready_text_three')}")

    log.separate_magenta()

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

    try:
        await bot.change_presence(status=discord.Status.idle,
                                  activity=activity,
                                  afk=True,
                                  idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))
    except Exception as e:
        log.alert(f"{lang.text('no_notification_rpc')}\n{e}\n{lang.text('no_notification_rpc_two')}")
        try:
            await bot.change_presence(status=discord.Status.idle,
                                      activity=activity,
                                      edit_settings=False)
            log.success(lang.text('no_notification_rpc_success'))
        except Exception as e:
            log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")

    if rpc.read_variable_json("create_panel"):
        os.system("nuclear_icon.png")
        print("icon successfully loaded")

def restart_selfbot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command()
async def restart(ctx: commands.Context):
    await ctx.message.edit(lang.text('restart_command'))
    time.sleep(2)
    await ctx.message.delete()
    restart_selfbot()

@bot.command()
async def stop(ctx: commands.Context):
    await ctx.message.edit(lang.text('stop_command'))
    time.sleep(2)
    await ctx.message.delete()
    await bot.close()
    exit()

#############
#############


####################
# start the        #
#      selfbot !!  #
####################



def fix_aiohttp():
    """
    This error is from discord.py==1.7.3(it's the last version of discord.py
    that works with user account) that use an old version of aiohttp.

    This should fix this error.
    """
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "aiohttp"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip3", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip3", "install", "-U", "aiohttp"])

    log.info(lang.text('aihottp_success'))
    
    time.sleep(3)

    restart_selfbot()


# Launch the selfbot
# By the way, this is the first and the only moment where we use the token in the selfbot.
try:
    if config_selfbot.discord_log:
        # If `discord_log` in `config_selfbot` is True, enable discord.py-self's logs
        bot.run(config_selfbot.token)
    else:
        # Else, disable discord.py-self's logs
        bot.run(config_selfbot.token, log_handler=None)
except discord.LoginFailure:
    # Log if the passed token is incorrect
    log.critical(lang.text('token_error'))
except Exception as e:
    # Check what the error is from, and react
    if "400, message='Can not decode content-encoding: br'" in str(e):
        # If the Exception is about the old aiohttp error, it try to fix itself with fix_aiohttp()
        log.warning(lang.text('aihottp_error'))
        fix_aiohttp()
    elif "4004" in str(e):
        # If the session has closed with 4004 (token has changed), log the error.
        log.critical(lang.text('expired_token'))
    else:
        # Else, print the Exception.
        log.critical(f"{lang.text('weird_error')} {e}")
