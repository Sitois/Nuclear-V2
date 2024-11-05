#!/usr/bin/python3
# -*- coding: utf-8 -*-
print("========================")
print("LAUNCHING NUCLEAR-V2")

import subprocess  # Importe le module subprocess pour exécuter des commandes système
print("10%, Importing required modules...")

try:
    import sys, os, platform  # Importe des modules système pour gérer des fonctionnalités du système d'exploitation
    import ctypes  # Utilisé pour les appels système natifs, comme changer le titre du terminal sous Windows
    import datetime, time  # Importe des modules pour gérer les dates et le temps
    import threading  # Importe le module threading pour créer des threads
    import asyncio  # Module pour programmer des fonctions asynchrones
    import config_selfbot  # Importe la configuration du selfbot
    print("25%, Loaded required python-integrated libraries.")
    
    from utils import rpc, log, __version__, lang  # Importe des modules utilitaires
    print("35%, Loading commands...")
    
    from commands import *  # Importe tous les modules de commandes
    from colorama import Fore, Style, Back  # Coloration des textes dans la console
    import requests  # Module pour faire des requêtes HTTP
    #import twocaptcha  # (commenté) module pour résoudre des captchas
    print("50%, Loading discord.py-self...")
    
    import discord  # Importe discord.py pour les fonctionnalités Discord
    from discord.ext import commands  # Importation des commandes discord
    import nacl  # Importe le module nacl pour gérer la sécurité
except ImportError:
    import sys, os
    print("++++++++++++++++++++++++")
    print("MISSING REQUIRED LIBRARIES")
    print("Downloading missing libraries from pip ...")
    
    # Installation des modules manquants
    if os.name == 'nt':  # Si le système est Windows
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:  # Si le système est autre
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

# Efface le terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Affichage de texte coloré avec la version du selfbot
print(fr"""{Fore.LIGHTCYAN_EX}$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  v{__version__}{Style.RESET_ALL}""")

# Change le titre du terminal
def set_terminal_title(title: str):
    """Change le titre du terminal en fonction du système d'exploitation."""
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':  # Pour macOS
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

# Essaye de définir le titre du terminal, log en cas d'échec
try:
    set_terminal_title("| Nuclear-V2 Selfbot |")
except Exception as e:
    log.warning(f"Error while trying to change the terminal name: {e}")

# Demande des informations si elles ne sont pas configurées dans le fichier de configuration
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

# Choix de la langue si non configurée
if config_selfbot.lang == "":
    print("Language Choice:")
    print('\n'.join([f"{list(item.values())[0]}: {list(item.values())[2]}" for item in lang.languages()]))
    config_selfbot.lang = input("Lang: ")

# Demande de préfixe si non configuré
if config_selfbot.prefix == "":
    config_selfbot.prefix = input("Prefix: ")

# Nom du selfbot si non configuré
if config_selfbot.selfbot_name == "":
    config_selfbot.selfbot_name = input("Selfbot name: ")

# Vérifie la dernière version disponible du selfbot sur GitHub
def check_latest_version(repo_owner: str, repo_name: str):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

check_loop = True  # Contrôle pour la boucle de vérification

# Désactive le vérificateur de mise à jour pour la version de développement
try:
    if float(__version__) > float(check_latest_version('Sitois', 'Nuclear-V2').strip('v')):
        log.warning(f"{lang.text('unstable_version')} https://github.com/Sitois/Nuclear-V2/releases/latest")
        check_loop = False
except Exception:
    # Évite les plantages si la version est sous forme 'v1.1.1'
    pass

# Prévention de l'utilisation d'une autre bibliothèque Discord que discord.py-self
if discord.__title__ != "discord.py-self":
    log.critical(lang.text('error_discord_version'))
    exit()

# Prévention de l'utilisation d'une version de pip défectueuse de discord.py
if discord.__version__.startswith("2.0.0"):
    log.critical(lang.text('error_discord_version'))
    exit()

# Boucle de vérification régulière de la version du selfbot
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

# Exécute call_check_repo en arrière-plan
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
#  démarrage du    #
#   selfbot !!!    #
####################

today_date = datetime.datetime.today()  # Date d'aujourd'hui pour le lancement du selfbot

# TODO: Compléter le gestionnaire de captcha
"""
API_KEY = 'YOUR_API_KEY'


solver = twocaptcha.TwoCaptcha(API_KEY)

async def handle_captcha(exc: discord.CaptchaRequired, bot: commands.Bot) -> None:
    try:
        result = solver.recaptcha(sitekey=exc.site_key, url=exc.site_url)
        await exc.solve(result['code'])
        print("Captcha solved successfully")
    except Exception as e:
        print(f"Error solving captcha: {e}")
"""
# Configuration de l'objet bot avec le préfixe et désactivation des messages non-commandes
bot = commands.Bot(command_prefix=config_selfbot.prefix, self_bot=True)
bot.remove_command("help")  # Supprime la commande d'aide par défaut

# Fonction de démarrage du bot
@bot.event
async def on_ready():
    # Log le message lorsque le bot est prêt à l'utilisation
    log.info(lang.text('bot_ready').format(config_selfbot.selfbot_name))
    print(f"Bot connected as {bot.user}")  # Affiche l'utilisateur connecté

# Fonction pour gérer les erreurs de commandes
@bot.event
async def on_command_error(ctx, error):
    # Si l'utilisateur ne dispose pas des permissions requises
    if isinstance(error, commands.MissingPermissions):
        log.warning(lang.text('missing_permissions').format(ctx.author))
    # Si la commande n'existe pas
    elif isinstance(error, commands.CommandNotFound):
        log.info(lang.text('command_not_found').format(ctx.message.content))
    # Pour toute autre erreur, log avec la trace complète
    else:
        log.error(f"Unexpected error: {error}")

# Commande d'exemple (remplacez par vos commandes)
@bot.command()
async def ping(ctx):
    """Commande simple de ping pour vérifier la réactivité du bot"""
    await ctx.send('Pong!')
    log.info(lang.text('command_executed').format('ping'))

# Boucle principale pour exécuter le bot
try:
    bot.run(config_selfbot.token, bot=False)  # Lancement du selfbot avec le token
except Exception as e:
    log.critical(f"Failed to start bot: {e}")  # Log une erreur critique si le bot ne démarre pas
