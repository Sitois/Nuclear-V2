from utils import rpc
#######################
#  selfbot            #
#        basic        #
#         config ^^   #
#######################

# en: SelfBot name
# fr: Nom du SelfBot
# es: Nombre del SelfBot
# jp: セルフボットの名前
selfbot_name = "Nuclear" # Tip: Don't use the "Selfbot" word into your selfbot name, most of servers blacklist this word with AutoMod

# en: Account Token.
# fr: Token du compte.
# es: Token de la cuenta.
# jp: アカウントのトークン
token = ""

# en: Commands prefix.
# fr: Prefix des commandes.
# es: Prefijo de comandos.
# jp: コマンドの接頭辞
prefix = "&"

# fr: Langue.
# en: Language.
# es: Idioma.
# jp: 言語
lang = "en" # fr / en / es /jp

# fr: Activer/Désactiver les logs de discord (ex: Connected to gateway , Rate Limited etc..).
# en: Toggle discord logs (like: Connected to gateway, Rate Limited etc...).
# es: Activar/Desactivar registros de Discord (como: Conectado a la gateway, Límite de velocidad, etc...).
# jp: Discordのログを切り替える（例: Gatewayに接続しました、レート制限など...）
discord_log = True

# fr: Default Nitro Sniper mode. (True=On, False=Off)
# fr: Mode du Nitro Sniper par défaut. (True=On, False=Off)
# es: Modo de Nitro Sniper por defecto. (True=Activado, False=Desactivado)
# jp: デフォルトのNitroスナイパーモード（True=オン、False=オフ）
nitro_sniper = False

# en: Commands delay of delete.
# fr: Délai de supression des commandes.
# es: Retraso en la eliminación de comandos.
# jp: コマンド削除の遅延
deltime = 20
########################


#######################
#  good               #
#        person       #
#######################

# en: Default paramter for Good Person.
# fr: Paramètre par défaut de Good Person.
# es: Parámetro predeterminado para Good Person.
# jp: Good Personのデフォルトパラメータ
good_person = False

# en: Good Person badwords.
# fr: Mot interdit pour Good Person.
# es: Palabras prohibidas para Good Person.
# jp: Good Personの禁止ワード
badwords = ["fuck", "shit", "pute", "connard", "connasse", "conasse", "nigg", "bitch", "kys", "fdp", "ntm", "tg"]

# en: Good Person "good words".
# fr: Mot "bon" pour Good Person.
# es: Palabras "buenas" para Good Person.
# jp: Good Personの「いい言葉」
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
########################

#######################
#  raid               #
#        config       #
#######################
# en: Ban reason (for &banall).
# fr: Raison du banissement (pour &banall).
# es: Razón de baneo (para &banall).
# jp: Ban理由（&banall用）
ban_reason = "ezzed by Nuclear lol."
kick_reason = "ezzed by Nuclear lol."

#######################
# fr: RPC par défaut  #
# en: Default RPC     #
# es: RPC por defecto  #
# jp: デフォルトRPC    #
#######################

activity_name = "☄"
activity_details = " "
activity_state = " "
application_id = 1193291951290712154

streaming_url = "https://twitch.tv/twitch"
activity_button_one = "Nuclear !"
activity_button_one_answer = "https://github.com/Sitois/Nuclear" # doesn't work for the moment
activity_button_two = "Star it!"
activity_button_two_answer = "https://github.com/Sitois/Nuclear" # doesn't work for the moment

# see &tuto
icon = rpc.get_raw_json("Sitois", "Nuclear-V2", "assets.json")
assets = {"large_image": icon["dark"]["large_image"],
          "large_text": "☄",
          "small_image": icon["dark"]["small_image"],
          "small_text": None
          }


################# 
