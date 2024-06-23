import config_selfbot

#######################
#  selfbot            #
#    translation >.<  #
#######################

token_error = {
    "fr": "Token incorrect. Merci d'entrer un token valide dans config_selfbot.py",
    "en": "Improper token. Please configure a valid token in config_selfbot.py"
}

error_discord_version = {
    "fr": "Votre librairie discord ne fonctionne pas avec ce selfbot. Installez la version fonctionnel ici:",
    "en": "Your discord library version doesn't work with this selfbot. Install the working version from"
}

aihottp_error = {
    "fr": "Ancienne version d'aiohttp. Cette version est utilisé uniquement sur discord.py==1.7.3. Tentative de réparer le problème...\n(si ça ne fonctionne pas: `pip uninstall aiohttp` et `pip install aiohttp`)...\nAppuyez sur Entrer.",
    "en": "Old aiohttp error. This error is from discord.py==1.7.3.\nTrying to update aiohttp (if it doesn'twork: `pip uninstall aiohttp` and `pip install aiohttp`)...\nPress Enter."
}

aihottp_success = {
    "fr": "Redémarrage en cours...",
    "en": "Restarting..."
}

weird_error = {
    "fr": "Maybe a config error. Make sure all informations in config_selfbot.py are correct.\nError:",
    "en": "Peut-être une erreur de configuration. Assurez-vous que toutes les informations dans config_selfbot.py sont correctes.\nErreur:"
}

expired_token = {
    "fr": "Account's Token has changed. Please insert the new one into config_selfbot.py",
    "en": "Le Token du compte a changé. Merci d'insérer le nouveau dans config_selfbot.py"
}

cog_success = {
    "fr": "Catégorie chargé avec succès !",
    "en": "Successfully loaded category!"
}

cog_fail = {
    "fr": "Erreur lors du chargement de cette catégorie: ",
    "en": "Error while trying to load catergory: "
}

enable = {
    "fr": "activé !",
    "en": "enabled!"
}

disable = {
    "fr": "désactivé !",
    "en": "disabled!"
}


empty = {
    "fr": "Aucune",
    "en": "None"
}

author = {
    "fr": "Auteur",
    "en": "Author"
}

incorrect = {
    "fr": "Choix incorrect.",
    "en": "Incorrect choice."
}

is_ = {
    "fr": "est",
    "en": "is"
}

####################
#  launch          #
# translation !!!  #
####################

start_text = {
    "fr": "Démarrage du selfbot en cours...",
    "en": "Starting the selfbot..."
}

ready_text = {
    "fr": "Connecté en tant que",
    "en": "Connected as"
}

ready_text_two = {
    "fr": "démarré en",
    "en": "started in"
}

ready_text_three = {
    "fr": "secondes.",
    "en": "seconds."
}

unstable_version = {
    "fr": """Vous utilisez une version INSTABLE:
- Si vous faites faces à un problème, merci d'en avertir le Support.
- Si vous corrigez/ajoutez quelque chose, merci d'ouvrir une pull request sur GitHub pour l'ajouter dans le projet principal.
- UpdateChecker est désactivé.
- Si vous n'êtes pas un développeur, je vous recommande d'utiliser la version stable actuelle:""",
    "en": """You are using an UNSTABLE version:
- If you get any issues, please report them in the Support.
- If you fix/add something, please open a pull request on GitHub to add it into the main project.
- UpdateChecker is disabled.
- If you aren't a developer, you should use the current stable version:"""
}

error_check_version_one = {
    "fr": "Une nouvelle version",
    "en": "A new version"
}

error_check_version_two = {
    "fr": "est disponible:",
    "en": "is out at:"
}

error_check_version_three = {
    "fr": "Vous utilisez actuellement la version ",
    "en": "You are currently using "
}

panel_message = {
    "fr": f"""# __N'utilisez pas les commandes dans des serveurs, vous pouvez vous faire signaler__ #
> ## [Support](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#support) ##

Commencez avec `{config_selfbot.prefix}help`!
Vous pouvez utilisez toutes les commandes, sans problèmes, dans ce panel.""",
    "en": f"""# __Don't use command in servers, you can get reported.__ #

> ## [Support](https://github.com/Sitois/Nuclear-V2#support) ##

Get started with `{config_selfbot.prefix}help`!
You can use every commands safely, in this panel."""
}

####################
#  help            #
# translation !!!  #
####################

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

help_voice = {
    "fr": "Vocal",
    "en": "Voice"
}


help_general_hype = {
    "fr": "Défini votre badge HypeSquad",
    "en": "Set your HypeSquad badge"
}

help_general_ping = {
    "fr": "Affiche la latence du selfbot",
    "en": "Display the selfbot's ping"
}

help_general_sniper = {
    "fr": "Active / désactive le NitroSniper",
    "en": "Enable / disable NitroSniper"
}

error_no_message_snipe = {
    "fr": "❌ Aucun message supprimé récemment dans ce salon !",
    "en": "❌ No message deleted recently in this channel!"
}

time_snipe = {
    "fr": "Supprimé il y a",
    "en": "Deleted at"
}

help_config_restart = {
    "fr": "Redémarre le selfbot (peut régler un bug)",
    "en": "Restart the selfbot. (it can fix a bug)"
}

help_config_stop = {
    "fr": "Stop le selfbot",
    "en": "Stop the selfbot"
}

help_general_bio = {
    "fr": "Change la biographie du compte",
    "en": "Change account's bio"
}

help_general_snipe = {
    "fr": "Snipe le dernier message supprimé.",
    "en": "Snipe the last deleted message."
}

help_general_clear = {
    "fr": "Supprime le nombre de messages fourni.",
    "en": "Clear given number of messages."
}

help_general_user_info = {
    "fr": "Renvoie les informations sur l'utilisateur mentionné.",
    "en": "Return informations about the mentionned user."
}

help_voice_vc = {
    "fr": "Rejoins le salon vocal",
    "en": "Join the voice channel"
}

help_voice_cam = {
    "fr": "Rejoins le salon vocal avec une fausse caméra",
    "en": "Join the voice channel with a fake camera"
}

help_voice_leave = {
    "fr": "Quitte le salon vocal",
    "en": "Leave the voice channnel"
}

help_fun_cat = {
    "fr": "Chat mignon 🐈",
    "en": "Cute cat 🐈"
}

help_fun_good = {
    "fr": "Vous transforme en une Bonne Personne ! (*censure les insultes*)",
    "en": "Transform you into a Good Person ! (*no insults*)"
}

help_fun_token = {
    "fr": "Renvoie le début du token de la personne mentionné",
    "en": "Returns the beginning of the token of the mentionned user"
}

help_fun_hug = {
    "fr": "Hug GIF (cute!)",
    "en": "GIF de calin (mignon!!)"
}

help_fun_call = {
    "fr": "Spam d'appel (seulement en MP!)",
    "en": "Join and Leave the voice (only in dm!)"
}

help_fun_gift = {
    "fr": "Envoie un faux lien Nitro",
    "en": "Send a fake Nitro"
}

help_fun_hack = {
    "fr": "aque quelqu'un (😈)",
    "en": "hack someone fr (😈)"
}

help_fun_femboy = {
    "fr": "Indique le pourcentage de femboy-ité",
    "en": "Return the femboy percent of someone"
}

help_raid_dmall = {
    "fr": "Envoi un message privé à votre liste d'amis",
    "en": "Send a private message to your friend list."
}

help_raid_banall = {
    "fr": "Bannis tout les membres du serveur",
    "en": "Ban all members"
}

help_raid_kick = {
    "fr": "Kick tout les membres du serveur",
    "en": "Kick all members"
}

help_tools_close_dm = {
    "fr": "Ferme tout vos MP",
    "en": "Close all your DMs"
}

help_tools_bump = {
    "fr": "Bump automatiquement avec Disboard",
    "en": "Automatically bump with Disboard"
}

help_tools_close_dm_bots = {
    "fr": "Ferme tout vos MP avec des bots",
    "en": "Close all your DMs with bots"
}

help_backup_backups = {
    "fr": "Affiche la liste des sauvegardes disponibles.",
    "en": "Return the list of available backups."
}

help_backup_save = {
    "fr": "Sauvegarde ce serveur.",
    "en": "Save this server."
}

help_backup_load = {
    "fr": "Charge une sauvegarde.",
    "en": "Load a backup."
}

help_backup_tip = {
    "fr": "Vous pouvez indiquer un autre serveur avec son ID!",
    "en": "You can specify another server with its ID!"
}

help_backup_note = {
    "fr": "Les abckups prennent énormément de temps à se charger, soyez patient!",
    "en": "Backups take a long time to load, be patient!"
}
# le attention ça prend 10 minutes, le vous pouvez mettre l'ID du serveur sinonça pred celui où t'as envoyé le msg
help_backup_delete = {
    "fr": "Supprime une backup avec son ID.",
    "en": "Delete a backup with its ID."
}


####################
#  commands        #
# translation !!!  #
####################

restart_command = {
    "fr": "✅ Selfbot redémarré avec succès (patientez quelques secondes...) !",
    "en": "✅ Succesfully restarted the selfbot (wait a couple of seconds...)!"
}

stop_command = {
    "fr": "⭕ Le selfbot a bien été stoppé.",
    "en": "⭕ Succesfully stopped the selfbot."
}

leave_voice = {
    "fr": "Déconnection du salon",
    "en": "Disconnected from"
}

leave_voice_error = {
    "fr": "Error while leaving the voice channel",
    "en": "Erreur lors de la déconnexion au salon vocal"
}

leave_voice_error_not_found = {
    "fr": "❌ Vous devez être connecté à un salon vocal pour utiliser cette commande !",
    "en": "❌ You must be connected to a voice channel to use this command!"
}

voice_channel_error = {
    "fr": "❌ Veuillez indiquer un ID de salon vocal valide !",
    "en": "❌ Please enter a valid voice channel ID!"
}

voice_channel_error_not_found = {
    "fr": "❌ Le salon vocal avec cet ID n'existe pas.",
    "en": "❌ Unable to find the voice channel!"
}

hype_command = {
    "fr": "modifié en",
    "en": "changed to"
}

hype_fail = {
    "fr": "❌ HypeSquad renseignée incorrect. (brilliance, balance, bravery).",
    "en": "❌ Given HypeSquad house is incorrect. (brilliance, balance, bravery)."
}

bio_command = {
    "fr": "changée en",
    "en": "changed to"
}

spam_cooldown = {
    "fr": f"❌ Un spam est déjà en cours ! Pour l'arrêter, faites `{config_selfbot.prefix}restart`.",
    "en": f"❌ A spam is already active! To spam the current spam, do `{config_selfbot.prefix}restart`."
}

spam_invalid = {
    "fr": "❌ Veuillez indiquer un nombre valide !",
    "en": "❌ You must enter a valid number!"
}

spam_too_much = {
    "fr": "❌ Veulliez indiquer une valeur en dessous de 100 !",
    "en": "❌ Please enter a value below 100!"
}

only_dm_fun = {
    "fr": "❌ Cette commande n'est disponible qu'en MP!",
    "en": "❌ You must use this command in DM!"
}

voice_join = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_error = {
    "fr": "Erreur lors de la connexion au salon vocal",
    "en": "Error while trying to connect to the voice channel"
}

voice_join_cam = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_cam_two = {
    "fr": "avec la caméra activée",
    "en": "with camera"
}

nitro_sniper_claimed = {
    "fr": "a déjà été réclamé par quelqu'un d'autre !",
    "en": "was already redeemed by someone else!"
}

nitro_sniper_valid = {
    "fr": "a bien été réclamé sur le compte !",
    "en": "has been claimed on the account!"
}

nitro_sniper_invalid_code = {
    "fr": "est invalide !",
    "en": "is invalid!"
}

fun_hack_step_one = {
    "fr": "aquage de",
    "en": "hacking"
}

fun_hack_step_two = {
    "fr": "récupération de l'adresse mail",
    "en": "getting email adress"
}

fun_hack_step_three = {
    "fr": "adresse mail trouvée",
    "en": "found email adress"
}

fun_hack_step_four = {
    "fr": "spam à tout ses contaktes...",
    "en": "spamming all contacts"
}

fun_hack_step_five = {
    "fr": "g bien aquer",
    "en": "successfully hackd"
}

fun_copy_user_fail = {
    "fr": "❌ Veuillez indiquer un utilisateur à copier (ID ou mention).",
    "en": "❌ Please give an ID / mention for the user to copy."
}

fun_token = {
    "fr": "Début du token de",
    "en": "Start of the token of"
}

info_title = {
    "fr": "Informations sur",
    "en": "Informations about"
}

info_global = {
    "fr": "Nom d'affichage",
    "en": "Display name"
}

info_banner = {
    "fr": "Bannière",
    "en": "Banner"
}

info_created_at = {
    "fr": "Créé le",
    "en": "Created at"
}

info_avatar = {
    "fr": "Photo de profil",
    "en": "Avatar"
}

info_avatar_link = {
    "fr": "Lien vers la photo",
    "en": "Avatar's link"
}

info_banner_link = {
    "fr": "Lien vers la bannière",
    "en": "Banner's link"
}

info_roles = {
    "fr": "Rôles",
    "en": "Roles"
}

info_username = {
    "fr": "Nom d'utilisateur",
    "en": "Username"
}

raid_in_process = {
    "fr": "☣️ Raid en cours...",
    "en": "☣️ Raid in progress..."
}

raid_error_permisssion = {
    "fr": "‼️ Permission manquantes !",
    "en": "‼️ Missing permissions!"
}

raid_kick_all_success = {
    "fr": "✅ Tout les membres ont été kick du serveur avec succès.",
    "en": "✅ Succesfully kicked all members."
}

raid_ban_all_success = {
    "fr": "✅ Tout les membres ont été bannis du serveur avec succès.",
    "en": "✅ Succesfully banned all members."
}

raid_dm_all = {
    "fr": "☣️ Envoi du message privée à toute la liste d'amis...",
    "en": "☣️ Sending the message to all friends..."
}

raid_dm_all_fail = {
    "fr": "❌ Vous devez renseigner un message !",
    "en": "❌ You must enter a message!"
}

raid_dm_all_captcha = {
    "fr": "❌ Amis trop nombreux. Captcha requis !",
    "en": "❌ Too many friends. Captcha required!"
}

raid_dm_all_success = {
    "fr": "✅ Message envoyé avec succès à la liste d'amis !",
    "en": "✅ Succesfully sent message to all friends!"
}

tool_close_dms = {
    "fr": "🔧 Fermeture de tout vos MP...",
    "en": "🔧 Closing all your DMs..."
}

tool_bump = {
    "fr": "🔁 Le serveur sera bump sur ce salon",
    "en": "🔁 This server will be bumped on this channel"
}

tool_bump_not_found = {
    "fr": "❌ Le bot Disboard n'a pas été trouvé sur ce serveur.",
    "en": "❌ Disboard wasn't found on this server."
}

tool_bump_two = {
    "fr": "fois.",
    "en": "times."
}

tool_close_dms_success = {
    "fr": "✅ Tout vos MP ont bien été fermés !",
    "en": "✅ All of your DMs has been closed!"
}

tool_close_dms_bots = {
    "fr": "🔧 Fermeture de tout vos MP avec des bots...",
    "en": "🔧 Closing all your DMs with bots..."
}

tool_close_dms_bots_success = {
    "fr": "✅ Tout vos MP avec des bots ont bien été fermés !",
    "en": "✅ All of your DMs with bots has been closed!"
}

####################
#  rpc             #
# translation !!!  #
####################



rpc_name_translate = {
    "fr": "Défini le nom du RPC",
    "en": "Set RPC's name"
}

rpc_details_translate = {
    "fr": "Défini les details du RPC",
    "en": "Set RPC's details"
}

rpc_state_translate = {
    "fr": "Défini le \"state\" du RPC",
    "en": "Set RPC's state"
}

rpc_url_translate = {
    "fr": "Défini l'url de steaming du RPC ``(https://twitch.tv/nom)``",
    "en": "Set RPC's streaming URL ``(https://twitch.tv/name)``"
}

rpc_type_translate = {
    "fr": "Défini le type de votre RPC (game / watch / listen / stream)",
    "en": "Set RPC's type (game / watch / listen / stream)"
}

rpc_large_image_translate = {
    "fr": "Défini la grande image du RPC",
    "en": "Set RPC's large image"
}

rpc_large_text_translate = {
    "fr": "Défini le texte de la grande image du RPC",
    "en": "Set RPC's large image text"
}

rpc_small_image_translate = {
    "fr": "Défini la petite image du RPC",
    "en": "Set RPC's small image"
}

rpc_small_text_translate = {
    "fr": "Défini le texte de la petite image du RPC",
    "en": "Set RPC's small image text"
}

rpc_button_text_one_translate = {
    "fr": "Défini le texte du premier bouton du RPC",
    "en": "Set RPC's first button text"
}

rpc_button_link_one_translate = {
    "fr": "Défini le lien du premier bouton du RPC",
    "en": "Set RPC's first button link"
}

rpc_button_text_two_translate = {
    "fr": "Défini le texte du second bouton du RPC",
    "en": "Set RPC's second button text"
}

rpc_button_link_two_translate = {
    "fr": "Défini le lien du second bouton du RPC",
    "en": "Set RPC's second button link"
}




####################
# template         #
# translation !!!  #
####################

template_help_reset = {
    "fr": "Réinitialise votre RPC.",
    "en": "Reset your RPC."
}

template_help_clear = {
    "fr": "Supprime votre RPC.",
    "en": "Clear your RPC."
}

template_help_default = {
    "fr": "Modifie votre RPC par celui présent dans (`config_selfbot.py`).",
    "en": "Edit your RPC to the default one (in `config_selfbot.py`)."
}

template_help_cod = {
    "fr": "Utilise la template \"Call Of Duty\".",
    "en": "Use \"Call Of Duty\"'s template."
}

template_help_dark = {
    "fr": "Utilise la template \"dark\".",
    "en": "Use \"dark\" template."
}

template_help_python = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template."
}

template_help_js = {
    "fr": "Utilise la template \"JavaScript\".",
    "en": "Use \"JavaScript\" template."
}

template_help_omori = {
    "fr": "Utilise la template \"Omori\".",
    "en": "Use \"Omori\" template."
}

template_help_car = {
    "fr": "Utilise la template \"Car\".",
    "en": "Use \"Car\" template."
}

template_help_self = {
    "fr": "Utilise la template \"Nuclear\".",
    "en": "Use \"Nuclear\" template."
}

template_help_webdeck = {
    "fr": "Utilise la template \"WebDeck\".",
    "en": "Use \"WebDeck\" template."
}

template_help_hi = {
    "fr": "Utilise la template \"Hi !\".",
    "en": "Use \"Hi !\" template."
}

template_help_youtube = {
    "fr": "Utilise la template \"YouTube\".",
    "en": "Use \"YouTube\" template."
}

template_help_gta = {
    "fr": "Utilise la template \"GTA VI\".",
    "en": "Use \"GTA VI\" template."
}

template_help_tiktok = {
    "fr": "Utilise la template \"TikTok\".",
    "en": "Use \"TikTok\" template."
}

template_help_reload = {
    "fr": f"Vous pouvez mettre à jour les images avec la commande`{config_selfbot.prefix}reload` !",
    "en": f"You can reload Templates images with the `{config_selfbot.prefix}reload` command!"
}

template_reload = {
    "fr": "✅ Images des Templates mises à jour !",
    "en": "✅ Templates images updated!"
}



rpc_cod_details = {
    "fr": "En attente de mission...",
    "en": "Waiting for a mission..."
}

rpc_cod_state = {
    "fr": "Menu principal",
    "en": "In the main menu"
}


tutorial_rpc = {
    "fr": f""" Pour obtenir une image personnalisé:
  1. Envoyer une image (gif, png...) dans Discord. (dans n'importe quelle salon)
  2. Clique droit et "Copier l'adresse de l'image".
  3. Faites `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/exemple.png`.
  4. Fini !""",
    "en": f""" To get a custom rpc image, you should:
  1. Upload an image (gif, png...) into Discord. (in any channel)
  2. Right Click and "Copy Image Link".
  3. Do `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png`.
  4. Done !"""
}



backup_saving = {
    "fr": "🔁 Création de la backup en cours...",
    "en": "🔁 Creating backup..."
}

backup_not_find_folder = {
    "fr": "❌ Impossible de trouver le dossier 'backups' !",
    "en": "❌ Unable to find the 'backups' folder!"
}

backup_success_save = {
    "fr": "✅ Sauvegarde réussie pour le serveur",
    "en": "✅ Successfully saved guild"
}

backup_save_already_exist = {
    "fr": "❌ Une backup pour",
    "en": "❌ A save for"
}

backup_save_already_exist_two = {
    "fr": f"existe déjà. Utilisez `{config_selfbot.prefix}delete <server_id>` pour la supprimer.",
    "en:": f"already exists. Use `{config_selfbot.prefix}delete <server_id>` to remove it."
}

no_backup_error = {
    "fr": "❌ Aucune backup disponible.",
    "en": "❌ No backup available."
}

backup_list = {
    "fr": "Backups disponibles:\n",
    "en": "Severs backups:\n"
}

backup_invalid = {
    "fr": f"❌ Aucune backup disponible pour cet ID. Utilisez `{config_selfbot.prefix}backups` pour voir les backup disponibles !",
    "en": f"❌ No backup available for this server ID. Use `{config_selfbot.prefix}backups` to see available backups!"
}

backup_id_required = {
    "fr": "❌ Vous devez indiquer un ID de serveur !",
    "en": "❌ You must indicate a server ID!"
}

backup_done = {
    "fr": "✅ Backup effectué avec succès !",
    "en": "✅ Backup done successfully!"
}

backup_delete_done = {
    "fr": "✅ Backup supprimé avec succès !",
    "en": "✅ Backup deleted successfully!"
}

backup_no_permissions = {
    "fr": "❌ Vous n'avez pas la permission 'Administrateur' pour charger les backup.",
    "en": "❌ 'Administrator' permission is required to load backups."
}