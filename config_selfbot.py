from utils import rpc
#######################
#  selfbot            #
#        config       #
#######################

# fr: Nom du SelfBot
# Astuce : Évitez d'utiliser le mot "Selfbot" dans le nom, car certains serveurs le blacklistent avec AutoMod.
selfbot_name = "Nuclear" 

# fr: Token du compte pour se connecter ; gardez-le sécurisé et ne le partagez pas.
token = ""  

# fr: Préfixe pour déclencher les commandes.
prefix = "&"  

# fr: Langue de l'interface ; options disponibles : 'fr' (Français), 'en' (Anglais), 'es' (Espagnol), 'jp' (Japonais).
lang = "en"  

# fr: Activer/Désactiver les logs Discord (ex : Connexion au gateway, Limite de débit).
discord_log = True  

# fr: Mode par défaut du Nitro Sniper (True=Activé, False=Désactivé)
nitro_sniper = False  

# fr: Délai de suppression des messages de commande en secondes.
deltime = 20  

########################


#######################
#  personne           #
#         gentille    #
#######################

# fr: Paramètre par défaut pour l'option "Gentille Personne".
good_person = False  

# fr: Liste de mots interdits pour "Gentille Personne".
badwords = ["fuck", "shit", "pute", "connard", "connasse", "conasse", "nigg", "bitch", "kys", "fdp", "ntm", "tg"]

# fr: Liste de mots "gentils" pour l'option "Gentille Personne".
good_person_list = [
        "GeForce RTX 4000",
        "🍗",
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.",
        "AMD Ryzen™ 9 7900",
        "Intel Core is very good",
        "🐈",
        "🍟",
        "yipeeeeeeeee",
        "😍",
        "🌠",
        "u r beautiful",
        "you are all very intelligent",
        "excuse me"
]
########################


#######################
#  configuration      #
#         de raid     #
#######################

# fr: Raison du bannissement (pour &banall).
ban_reason = "ezzed by Nuclear lol."

# fr: Raison de l'expulsion.
kick_reason = "ezzed by Nuclear lol."


#######################
#   RPC par défaut    #
#######################

# fr: Nom de l'activité affichée dans le profil.
activity_name = "☄"  

# fr: Détails affichés dans l'activité.
activity_details = " "

# fr: État affiché dans l'activité.
activity_state = " "

# fr: ID de l'application RPC.
application_id = 1193291951290712154  

# fr: URL de streaming pour l'activité.
streaming_url = "https://twitch.tv/twitch"

# fr: Boutons d'activité (actuellement inactifs).
activity_button_one = "Nuclear !"
activity_button_one_answer = "https://github.com/Sitois/Nuclear" 

activity_button_two = "Star it!"
activity_button_two_answer = "https://github.com/Sitois/Nuclear" 

# fr: Voir &tuto pour les instructions d'icônes.
icon = rpc.get_raw_json("Sitois", "Nuclear-V2", "assets.json")
assets = {
    "large_image": icon["dark"]["large_image"],
    "large_text": "☄",
    "small_image": icon["dark"]["small_image"],
    "small_text": None
}
##############################################
