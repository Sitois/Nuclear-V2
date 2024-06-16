import subprocess
try:
    import sys, os, platform
    import ctypes
    import datetime, time
    import threading
    import random, asyncio
    import config_selfbot
    import langs
    from utils import rpc, log, __version__
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands
except ImportError:
    import sys, os
    if os.name == 'nt':
     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
     subprocess.check_call([sys.executable, "-m", "pip3", "install", '-r' , 'requirements.txt'])
    import platform
    import ctypes
    import datetime, time
    import threading
    import random, asyncio
    import config_selfbot
    import langs
    from utils import rpc, log, __version__
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands

os.system('cls' if os.name == 'nt' else 'clear')

print(fr"""{Fore.LIGHTCYAN_EX}$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  v{__version__}{Style.RESET_ALL}""")


def set_terminal_title(title):
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


if config_selfbot.token == "":
   config_selfbot.token = input("Token: ")

if config_selfbot.lang == "":
   print("""Language Choice / Choix de la langue:
fr: Français
en: English""")
   config_selfbot.lang = input("fr / en: ")

if config_selfbot.prefix == "":
   config_selfbot.prefix = input("Prefix: ")

if config_selfbot.selfbot_name == "":
   config_selfbot.selfbot_name = input("Selfbot name: ")


def check_latest_version(repo_owner, repo_name):
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
        log.warning(f"{langs.unstable_version[config_selfbot.lang]} https://github.com/Sitois/Nuclear-V2/releases/tag/{check_latest_version('Sitois', 'Nuclear-V2')}")
        check_loop = False
except Exception:
    pass

# Prevent from starting the selfbot with discord.py==1.7.3
if discord.__version__.startswith("1.7.3"):
    log.critical(f"{langs.error_discord_version[config_selfbot.lang]} https://github.com/Sitois/Nuclear/releases/tag/{check_latest_version('Sitois', 'Nuclear-V2')}")
    exit()

# Prevent from starting the selfbot with the broken pip version
if discord.__version__.startswith("2.0.0"):
    log.critical(f"{langs.error_discord_version[config_selfbot.lang]} https://github.com/Sitois/Nuclear-V2/releases/tag/{check_latest_version('Sitois', 'Nuclear-V2')}")
    exit()


def call_check_repo():
    repo_owner = "Sitois"
    repo_name = "Nuclear-V2"
    while True:
        latest_version = check_latest_version(repo_owner, repo_name)
        if latest_version:
            if not latest_version == f"v{__version__}":
                log.info(f"""{langs.error_check_version_one[config_selfbot.lang]} ({latest_version}) {langs.error_check_version_two[config_selfbot.lang]} https://github.com/{repo_owner}/{repo_name}/releases/tag/{latest_version}
{langs.error_check_version_three[config_selfbot.lang]} v{__version__}""")
            time.sleep(3600)

def run_in_background():
    thread = threading.Thread(target=call_check_repo, daemon=True)
    thread.start()

if check_loop:
    try:
        run_in_background()
    except Exception as e:
        log.warning(f"Error while trying to check the last Nuclear version: {e}")

log.start(f"{langs.start_text[config_selfbot.lang]}")



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
bot = commands.Bot(command_prefix=config_selfbot.prefix, self_bot=True, help_command=None)#, captcha_handler=handle_captcha)

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
        log.success(f"HelpCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"HelpCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(FunCommands(bot))
        log.success(f"FunCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"FunCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(UtilsCommands(bot))
        log.success(f"UtilsCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"UtilsCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(VoiceCommands(bot))
        log.success(f"VoiceCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"VoiceCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(ConfigCommands(bot))
        log.success(f"ConfigCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"ConfigCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(RaidCommands(bot))
        log.success(f"RaidCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"RaidCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(ToolsCommands(bot))
        log.success(f"ToolsCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"ToolsCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(TemplatesCommands(bot))
        log.success(f"TemplatesCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"TemplatesCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(RichPresenceCommands(bot))
        log.success(f"RichPresenceCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"RichPresenceCommands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(BackupCommands(bot))
        log.success(f"BackupCommands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"BackupCommands: {langs.cog_fail[config_selfbot.lang]} {e}")

    # Print when the bot is ready to receive and answer to commands
    log.alert(f"{langs.ready_text[config_selfbot.lang]} @{bot.user.name} ({bot.user.id}), {langs.ready_text_two[config_selfbot.lang]} {round(time.time()) - round(start_time)} {langs.ready_text_three[config_selfbot.lang]}")

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

    await bot.change_presence(status=discord.Status.idle,
                              activity=activity,
                              afk=True,
                              idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

    # TODO: Servers backup.

    with open('nuclear_icon.png', 'rb') as image:
        nuclear_icon = image.read()
 
    if rpc.read_variable_json("create_panel"):
        panel = await bot.create_group()
        await asyncio.sleep(0.7)
        await panel.edit(name="Nuclear Panel", icon=nuclear_icon)
        await panel.send(langs.panel_message[config_selfbot.lang])
        await panel.send(f"<@{bot.user.id}>", delete_after=0.4)
        rpc.edit_variable_json("create_panel", False)
        log.alert("NuclearPanel successfully created (check DMs!).")


def restart_selfbot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.edit(langs.restart_command[config_selfbot.lang])
    time.sleep(2)
    await ctx.message.delete()
    restart_selfbot()

@bot.command()
async def stop(ctx):
    await ctx.message.edit(langs.stop_command[config_selfbot.lang])
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
    This error is from discord.py==1.7.3(it's the last version of discord.py that works with user account) that use an old version of aiohttp.
    This should fix this problem and restart the selfbot :).
    """
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "aiohttp"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip3", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip3", "install", "-U", "aiohttp"])

    log.info(langs.aihottp_success[config_selfbot.lang])
    
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
    log.critical(langs.token_error[config_selfbot.lang])
except Exception as e:
    # Check what the error is from, and react
    if "400, message='Can not decode content-encoding: br'" in str(e):
        # If the Exception is about the old aiohttp error, it try to fix itself with fix_aiohttp()
        log.warning(langs.aihottp_error[config_selfbot.lang])
        fix_aiohttp()
    elif "4004" in str(e):
        # If the session has closed with 4004 (token has changed), log the error.
        log.critical(langs.expired_token[config_selfbot.lang])
    else:
        # Else, print the Exception.
        log.critical(f"{langs.weird_error[config_selfbot.lang]} {e}")