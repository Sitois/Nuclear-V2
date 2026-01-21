from utils import rpc
#######################
#  selfbot            #
#        basic        #
#         config ^^   #
#######################

# en: SelfBot name
# fr: Nom du SelfBot
selfbot_name = "Nuclear" # Tip: Don't use the "Selfbot" word into your selfbot name, most of servers blacklist this word with AutoMod.

# en: Account Token.
# fr: Token du compte.
# Use the anonymous token system. Enter your token into `anonymous_token.txt`, Nuclear will launch with it then clear the file.
anonymous_token = False
# en: How to get your account token: https://github.com/Sitois/Nuclear-V2#-how-to-get-a-user-token
# fr: Tuto pour obtenir son token: https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-comment-obtenir-son-token
token = ""

# en: Commands prefix.
# fr: Prefix des commandes.
prefix = "&"

# fr: Langue.
# en: Language.
lang = "en" # fr / en / es / jp

# fr: Activer/Désactiver les logs de discord (ex: Connected to gateway , Rate Limited etc..).
# en: Toggle discord logs (like: Connected to gateway, Rate Limited etc...).
discord_log = True

# en: Default Nitro Sniper mode. (True=On, False=Off)
# fr: Mode du Nitro Sniper par défaut. (True=On, False=Off)
nitro_sniper = False

# en: Commands delay of delete.
# fr: Délai de supression des commandes.
deltime = 20
########################


#######################
#  good               #
#        person       #
#######################

# en: Default paramter for Good Person.
# fr: Paramètre par défaut de Good Person.
good_person = False

# en: Good Person badwords.
# fr: Mot interdit pour Good Person.
badwords = ["fuck", "shit", "pute", "connard", "connasse", "conasse", "nigg", "bitch", "kys", "fdp", "ntm", "tg"]

# en: Good Person "good words".
# fr: Mot "bon" pour Good Person.
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
        "excuse me",
        "i'm 67 brainroted"
        ]
########################
########################

#######################
#  raid               #
#        config       #
#######################
# en: Ban reason (for &banall).
# fr: Raison du banissement (pour &banall).
ban_reason = "ezzed by Nuclear lol."
kick_reason = "ezzed by Nuclear lol."

#######################
# fr: RPC par défaut  #
# en: Default RPC     #
#######################

activity_name = "☄"
activity_details = " "
activity_state = " "
application_id = 1193291951290712154

streaming_url = "https://twitch.tv/twitch"
activity_button_one = "Nuclear !"
activity_button_one_link = "https://github.com/Sitois/Nuclear"
activity_button_two = "Star it!"
activity_button_two_link = "https://github.com/Sitois/Nuclear"

# see &tuto
icon = rpc.get_raw_json("Sitois", "Nuclear-V2", "assets.json")
assets = {"large_image": icon["dark"]["large_image"],
          "large_text": "☄",
          "small_image": icon["dark"]["small_image"],
          "small_text": None
          }


#################
