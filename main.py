import subprocess
try:
    import sys
    import os
    import datetime
    import platform
    import ctypes
    import config_selfbot
    import fr_en
    from Commands import *
    from colorama import Fore, Style, Back
    import requests
    import discord
    from discord.ext import commands
except ImportError:
    import sys
    import os
    if sys.platform == 'win32':
     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
     subprocess.check_call([sys.executable, "-m", "pip3", "install", '-r' , 'requirements.txt'])
    import datetime
    import platform
    import ctypes
    import config_selfbot
    import fr_en
    from Commands import *
    from colorama import Fore, Style, Back
    import requests
    import discord
    from discord.ext import commands

os.system('cls' if os.name == 'nt' else 'clear')

nuclear_version = "v2.0"

print(Fore.LIGHTCYAN_EX + f"""$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  {nuclear_version}""", Style.RESET_ALL)



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
   print(f"Error while trying to change the terminal name: {e}")


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
   config_selfbot.selfbot_name = input("SelfBot name: ")


def check_latest_version(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

def call_check_repo():
    global nuclear_version
    repo_owner = "Sitois"
    repo_name = "Nuclear-V2"
    current_version = nuclear_version
    
    latest_version = check_latest_version(repo_owner, repo_name)
    if latest_version:
        if not latest_version == current_version:
            print(Fore.BLUE, "[INFO]", f"{fr_en.error_check_version_one[config_selfbot.lang]} ({latest_version}) {fr_en.error_check_version_two[config_selfbot.lang]} https://github.com/Sitois/Nuclear/releases/tag/{latest_version}")
            print(f" {fr_en.error_check_version_three[config_selfbot.lang]} {current_version}", Style.RESET_ALL)

try:
    call_check_repo()
except Exception as e:
    print(f"Error while trying to check the last Nuclear version: {e}")

print(Fore.LIGHTYELLOW_EX, "[#]", Fore.YELLOW, fr_en.start_text[config_selfbot.lang], Style.RESET_ALL)



####################
#  start           #
#   setup     !!!  #
####################

assets = config_selfbot.assets

today_date = datetime.datetime.today()

bot = commands.Bot(command_prefix=config_selfbot.prefix, self_bot=True, help_command=None)



@bot.event
async def on_ready():
    global today_date
    # Cogs !!
    try:
        await bot.add_cog(HelpCommands(bot))
        print(Fore.GREEN, "[+]", Fore.LIGHTGREEN_EX, 'HelpCommands:', fr_en.cog_success[config_selfbot.lang], Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED, "[-]", Fore.LIGHTRED_EX, 'HelpCommands:', fr_en.cog_fail[config_selfbot.lang], e, Style.RESET_ALL)
    try:
        await bot.add_cog(FunCommands(bot))
        print(Fore.GREEN, "[+]", Fore.LIGHTGREEN_EX, 'FunCommands:', fr_en.cog_success[config_selfbot.lang], Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED, "[-]", Fore.LIGHTRED_EX, 'FunCommands:', fr_en.cog_fail[config_selfbot.lang], e, Style.RESET_ALL)
    try:
        await bot.add_cog(GeneralCommands(bot))
        print(Fore.GREEN, "[+]", Fore.LIGHTGREEN_EX, 'GeneralCommands:', fr_en.cog_success[config_selfbot.lang], Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED, "[-]", Fore.LIGHTRED_EX, 'GeneralCommands:', fr_en.cog_fail[config_selfbot.lang], e, Style.RESET_ALL)
    print(Fore.RED, "[!]", Fore.LIGHTRED_EX, f"{fr_en.ready_text[config_selfbot.lang]} @{bot.user.name} ({bot.user.id}).", Style.RESET_ALL)
    print(Fore.MAGENTA + " ------------------", Style.RESET_ALL)
    activity = discord.Activity(type=discord.ActivityType.competing,
                                name=config_selfbot.activity_name,
                                details=config_selfbot.activity_details,
                                state=config_selfbot.activity_state,
                                #timestamps={"start": time.time()}, # ONLY FOR PLAYING ACTIVITY
                                assets=config_selfbot.assets,
                                buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])
    await bot.change_presence(status=discord.Status.idle,
                              activity=activity,
                              afk=True,
                              idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))


#############
#############





####################
# start the        #
#      selfbot !!  #
####################
    
try:
    bot.run(config_selfbot.token)
except discord.LoginFailure:
    print(Fore.LIGHTRED_EX, "[CRITICAL]", Fore.RED, fr_en.token_error[config_selfbot.lang], Style.RESET_ALL)
except Exception as e:
    print(Fore.LIGHTRED_EX, "[CRITICAL]", Fore.RED, fr_en.weird_error[config_selfbot.lang], e, Style.RESET_ALL)