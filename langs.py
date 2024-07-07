import config_selfbot

#######################
#  selfbot            #
#    translation >.<  #
#######################

token_error = {
    "fr": "Token incorrect. Merci d'entrer un token valide dans config_selfbot.py",
    "en": "Improper token. Please configure a valid token in config_selfbot.py",
    "es": "Token incorrecto. Por favor, configure un token válido en config_selfbot.py",
    "jp": "トークンが正しくありません。config_selfbot.pyに有効なトークンを設定してください"
}

error_discord_version = {
    "fr": "Votre librairie discord ne fonctionne pas avec ce selfbot. Installez la version fonctionnel ici:",
    "en": "Your discord library version doesn't work with this selfbot. Install the working version from",
    "es": "Tu versión de la biblioteca de discord no funciona con este selfbot. Instala la versión funcional desde",
    "jp": "このセルフボットにはあなたのディスコードライブラリバージョンは機能しません。動作するバージョンをインストールしてください"
}

aihottp_error = {
    "fr": "Ancienne version d'aiohttp. Cette version est utilisé uniquement sur discord.py==1.7.3. Tentative de réparer le problème...\n(si ça ne fonctionne pas: `pip uninstall aiohttp` et `pip install aiohttp`)...\nAppuyez sur Entrer.",
    "en": "Old aiohttp error. This error is from discord.py==1.7.3.\nTrying to update aiohttp (if it doesn'twork: `pip uninstall aiohttp` and `pip install aiohttp`)...\nPress Enter.",
    "es": "Error de aiohttp antiguo. Este error es de discord.py==1.7.3.\nIntentando actualizar aiohttp (si no funciona: `pip uninstall aiohttp` y `pip install aiohttp`)...\nPresiona Enter.",
    "jp": "古いaiohttpエラー。このエラーはdiscord.py==1.7.3からです。\naiohttpを更新しようとしています（機能しない場合は、`pip uninstall aiohttp`と`pip install aiohttp`を実行してください）...\nEnterキーを押してください。"
}

aihottp_success = {
    "fr": "Redémarrage en cours...",
    "en": "Restarting...",
    "es": "Reiniciando...",
    "jp": "再起動中..."
}

weird_error = {
    "fr": "Peut-être une erreur de configuration. Assurez-vous que toutes les informations dans config_selfbot.py sont correctes.\nErreur:",
    "en": "Maybe a config error. Make sure all informations in config_selfbot.py are correct.\nError:",
    "es": "Tal vez un error de configuración. Asegúrate de que toda la información en config_selfbot.py sea correcta.\nError:",
    "jp": "設定エラーの可能性があります。config_selfbot.pyのすべての情報が正しいことを確認してください。\nエラー："
}

expired_token = {
    "fr": "Le Token du compte a changé. Merci d'insérer le nouveau dans config_selfbot.py",
    "en": "Account's Token has changed. Please insert the new one into config_selfbot.py",
    "es": "El token de la cuenta ha cambiado. Por favor, inserta el nuevo en config_selfbot.py",
    "jp": "アカウントのトークンが変更されました。新しいトークンをconfig_selfbot.pyに入力してください"
}

cog_success = {
    "fr": "Catégorie chargé avec succès !",
    "en": "Successfully loaded category!",
    "es": "¡Categoría cargada con éxito!",
    "jp": "カテゴリが正常に読み込まれました！"
}

cog_fail = {
    "fr": "Erreur lors du chargement de cette catégorie: ",
    "en": "Error while trying to load catergory: ",
    "es": "Error al intentar cargar la categoría: ",
    "jp": "カテゴリの読み込み中にエラーが発生しました："
}

enable = {
    "fr": "activé !",
    "en": "enabled!",
    "es": "¡habilitado!",
    "jp": "有効！"
}

disable = {
    "fr": "désactivé !",
    "en": "disabled!",
    "es": "¡deshabilitado!",
    "jp": "無効！"
}

empty = {
    "fr": "",
    "en": "",
    "es": "",
    "jp": ""
}

author = {
    "fr": "Auteur",
    "en": "Author",
    "es": "Autor",
    "jp": "著者"
}

incorrect = {
    "fr": "Choix incorrect.",
    "en": "Incorrect choice.",
    "es": "Opción incorrecta.",
    "jp": "不正解の選択。"
}

is_ = {
    "fr": "est",
    "en": "is",
    "es": "es",
    "jp": "は"
}

####################
#  launch          #
# translation !!!  #
####################

start_text = {
    "fr": "Démarrage du selfbot en cours...",
    "en": "Starting the selfbot...",
    "es": "Iniciando el selfbot...",
    "jp": "セルフボットを開始しています..."
}

ready_text = {
    "fr": "Connecté en tant que",
    "en": "Connected as",
    "es": "Conectado como",
    "jp": "として接続済み"
}

ready_text_two = {
    "fr": "démarré en",
    "en": "started in",
    "es": "iniciado en",
    "jp": "で開始"
}

ready_text_three = {
    "fr": "secondes.",
    "en": "seconds.",
    "es": "segundos.",
    "jp": "秒。"
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
- If you aren't a developer, you should use the current stable version:""",
    "es": """Estás usando una versión INESTABLE:
- Si encuentras algún problema, por favor, infórmalo en el Soporte.
- Si corriges/agregas algo, por favor, abre un pull request en GitHub para agregarlo al proyecto principal.
- UpdateChecker está desactivado.
- Si no eres un desarrollador, te recomiendo usar la versión estable actual:""",
    "jp": """あなたは不安定なバージョンを使用しています：
- 何か問題が発生した場合は、サポートに報告してください。
- 修正/追加した場合は、GitHubでプルリクエストを開いて、メインプロジェクトに追加してください。
- UpdateCheckerは無効です。
- 開発者でない場合は、現在の安定版を使用することをお勧めします："""
}

error_check_version_one = {
    "fr": "Une nouvelle version",
    "en": "A new version",
    "es": "Una nueva versión",
    "jp": "新しいバージョン"
}

error_check_version_two = {
    "fr": "est disponible:",
    "en": "is out at:",
    "es": "está disponible en:",
    "jp": "が公開されています："
}

error_check_version_three = {
    "fr": "Vous utilisez actuellement la version ",
    "en": "You are currently using ",
    "es": "Actualmente estás usando la versión ",
    "jp": "現在使用しているバージョンは "
}

panel_message = {
    "fr": f"""# __N'utilisez pas les commandes dans des serveurs, vous pouvez vous faire signaler__ #
> ## [Support](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#support) ##

Commencez avec `{config_selfbot.prefix}help`!
Vous pouvez utilisez toutes les commandes, sans problèmes, dans ce panel.""",
    "en": f"""# __Don't use command in servers, you can get reported.__ #

> ## [Support](https://github.com/Sitois/Nuclear-V2#support) ##

Get started with `{config_selfbot.prefix}help`!
You can use every commands safely, in this panel.""",
    "es": f"""# __No uses comandos en servidores, podrías ser reportado.__ #

> ## [Soporte](https://github.com/Sitois/Nuclear-V2#support) ##

¡Comienza con `{config_selfbot.prefix}help`!
Puedes usar todos los comandos de manera segura, en este panel.""",
    "jp": f"""# __サーバーでコマンドを使用しないでください。報告される可能性があります。__ #

> ## [サポート](https://github.com/Sitois/Nuclear-V2#support) ##

`{config_selfbot.prefix}help` で始めましょう！
このパネルで安全にすべてのコマンドを使用できます。"""
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
    "es": [
        "Tu actitud determina tu dirección.",
        "Progreso, no perfección.",
        "Abraza los desafíos, ya que son los peldaños hacia el éxito.",
        "Acepta el fracaso como un peldaño, no como un obstáculo.",
        "Los únicos límites que existen son los que te pones a ti mismo.",
        "El coraje no es la ausencia de miedo, sino el triunfo sobre él.",
        "Los sueños no funcionan a menos que tú lo hagas.",
        "Las oportunidades no suceden. Tú las creas.",
        "No esperes el momento perfecto; toma el momento y hazlo perfecto.",
        "La única manera de hacer un gran trabajo es amar lo que haces.",
        "Cree que puedes, y ya estás a mitad de camino.",
        "No mires el reloj; haz lo que él hace. Sigue avanzando."
    ],
    "jp": [
        "あなたの態度が方向を決める。",
        "進歩、完璧ではなく。",
        "挑戦を受け入れなさい、それは成功への踏み石です。",
        "失敗を踏み台として受け入れ、つまづきとしてではない。",
        "存在する唯一の制限は、あなたが自分に置くものです。",
        "勇気は恐怖の不在ではなく、それに打ち勝つことです。",
        "夢はあなたが働かないと実現しません。",
        "機会は起こりません。あなたがそれらを作成します。",
        "完璧な瞬間を待たないでください。瞬間を取って、それを完璧にします。",
        "偉大な仕事をする唯一の方法は、あなたがすることを愛することです。",
        "あなたができると信じるなら、あなたは途中です。",
        "時計を見ないでください。時計がすることをしてください。進み続ける。"
    ]
}

help_voice = {
    "fr": "Vocal",
    "en": "Voice",
    "es": "Voz",
    "jp": "ボイス"
}

help_general_hype = {
    "fr": "Défini votre badge HypeSquad",
    "en": "Set your HypeSquad badge",
    "es": "Establecer tu insignia HypeSquad",
    "jp": "あなたのHypeSquadバッジを設定する"
}

help_general_ping = {
    "fr": "Affiche la latence du selfbot",
    "en": "Display the selfbot's ping",
    "es": "Mostrar el ping del selfbot",
    "jp": "セルフボットのpingを表示する"
}

help_general_sniper = {
    "fr": "Active / désactive le NitroSniper",
    "en": "Enable / disable NitroSniper",
    "es": "Habilitar / deshabilitar NitroSniper",
    "jp": "NitroSniperを有効/無効にする"
}

error_no_message_snipe = {
    "fr": "❌ Aucun message supprimé récemment dans ce salon !",
    "en": "❌ No message deleted recently in this channel!",
    "es": "❌ ¡No se ha eliminado ningún mensaje recientemente en este canal!",
    "jp": "❌ 最近このチャンネルで削除されたメッセージはありません！"
}

time_snipe = {
    "fr": "Supprimé il y a",
    "en": "Deleted at",
    "es": "Eliminado a las",
    "jp": "削除された時間"
}

help_config_restart = {
    "fr": "Redémarre le selfbot (peut régler un bug)",
    "en": "Restart the selfbot. (it can fix a bug)",
    "es": "Reiniciar el selfbot. (puede solucionar un error)",
    "jp": "セルフボットを再起動します。（バグを修正できる可能性があります）"
}

help_config_stop = {
    "fr": "Stop le selfbot",
    "en": "Stop the selfbot",
    "es": "Detener el selfbot",
    "jp": "セルフボットを停止する"
}

help_general_bio = {
    "fr": "Change la biographie du compte",
    "en": "Change account's bio",
    "es": "Cambiar la biografía de la cuenta",
    "jp": "アカウントのバイオを変更する"
}

help_general_snipe = {
    "fr": "Snipe le dernier message supprimé.",
    "en": "Snipe the last deleted message.",
    "es": "Snipear el último mensaje eliminado.",
    "jp": "最後に削除されたメッセージをスナイプします。"
}

help_general_clear = {
    "fr": "Supprime le nombre de messages fourni.",
    "en": "Clear given number of messages.",
    "es": "Borrar el número dado de mensajes.",
    "jp": "指定された数のメッセージをクリアします。"
}

help_general_user_info = {
    "fr": "Renvoie les informations sur l'utilisateur mentionné.",
    "en": "Return information about the mentioned user.",
    "es": "Devuelve información sobre el usuario mencionado.",
    "jp": "言及されたユーザーに関する情報を返します。"
}

help_voice_vc = {
    "fr": "Rejoins le salon vocal",
    "en": "Join the voice channel",
    "es": "Únete al canal de voz",
    "jp": "ボイスチャンネルに参加する"
}

help_voice_cam = {
    "fr": "Rejoins le salon vocal avec une fausse caméra",
    "en": "Join the voice channel with a fake camera",
    "es": "Únete al canal de voz con una cámara falsa",
    "jp": "偽のカメラでボイスチャンネルに参加する"
}

help_voice_leave = {
    "fr": "Quitte le salon vocal",
    "en": "Leave the voice channel",
    "es": "Salir del canal de voz",
    "jp": "ボイスチャンネルを退出する"
}

help_fun_cat = {
    "fr": "Chat mignon 🐈",
    "en": "Cute cat 🐈",
    "es": "Gato lindo 🐈",
    "jp": "かわいい猫 🐈"
}

help_fun_good = {
    "fr": "Vous transforme en une Bonne Personne ! (*censure les insultes*)",
    "en": "Transform you into a Good Person ! (*no insults*)",
    "es": "¡Te transforma en una Buena Persona! (*sin insultos*)",
    "jp": "あなたを良い人に変える！ （*侮辱なし*）"
}

help_fun_token = {
    "fr": "Renvoie le début du token de la personne mentionné",
    "en": "Returns the beginning of the token of the mentioned user",
    "es": "Devuelve el comienzo del token del usuario mencionado",
    "jp": "言及されたユーザーのトークンの最初を返します"
}

help_fun_hug = {
    "fr": "Hug GIF (cute!)",
    "en": "Hug GIF (cute!)",
    "es": "GIF de abrazo (¡lindo!)",
    "jp": "ハグGIF（かわいい！）"
}

help_fun_call = {
    "fr": "Spam d'appel (seulement en MP!)",
    "en": "Join and Leave the voice (only in DM!)",
    "es": "Unirse y salir de la voz (¡solo en DM!)",
    "jp": "ボイスに参加して退出する（DMのみ！）"
}

help_fun_gift = {
    "fr": "Envoie un faux lien Nitro",
    "en": "Send a fake Nitro",
    "es": "Enviar un Nitro falso",
    "jp": "偽のNitroを送る"
}

help_fun_hack = {
    "fr": "Hacke quelqu'un (😈)",
    "en": "Hack someone (😈)",
    "es": "Hackear a alguien (😈)",
    "jp": "誰かをハックする (😈)"
}

help_fun_femboy = {
    "fr": "Indique le pourcentage de femboy-ité",
    "en": "Return the femboy percent of someone",
    "es": "Devuelve el porcentaje de femboy de alguien",
    "jp": "誰かのフェンボーイ率を返します"
}

help_raid_dmall = {
    "fr": "Envoi un message privé à votre liste d'amis",
    "en": "Send a private message to your friend list.",
    "es": "Enviar un mensaje privado a tu lista de amigos.",
    "jp": "友達リストにプライベートメッセージを送信します。"
}

help_raid_banall = {
    "fr": "Bannis tout les membres du serveur",
    "en": "Ban all members",
    "es": "Banear a todos los miembros",
    "jp": "すべてのメンバーを禁止する"
}

help_raid_kick = {
    "fr": "Kick tout les membres du serveur",
    "en": "Kick all members",
    "es": "Expulsar a todos los miembros",
    "jp": "すべてのメンバーをキックする"
}

help_tools_close_dm = {
    "fr": "Ferme tout vos MP",
    "en": "Close all your DMs",
    "es": "Cerrar todos tus DMs",
    "jp": "すべてのDMを閉じる"
}

help_tools_bump = {
    "fr": "Bump automatiquement avec Disboard",
    "en": "Automatically bump with Disboard",
    "es": "Bumpear automáticamente con Disboard",
    "jp": "Disboardで自動的にバンプする"
}

help_tools_close_dm_bots = {
    "fr": "Ferme tout vos MP avec des bots",
    "en": "Close all your DMs with bots",
    "es": "Cerrar todos tus DMs con bots",
    "jp": "ボットとのすべてのDMを閉じる"
}

help_backup_backups = {
    "fr": "Affiche la liste des sauvegardes disponibles.",
    "en": "Return the list of available backups",
    "es": "Devuelve la lista de copias de seguridad disponibles",
    "jp": "利用可能なバックアップのリストを返します"
}

help_backup_save = {
    "fr": "Sauvegarde ce serveur (vous pouvez indiquer un autre serveur avec son ID).",
    "en": "Save this server (you can specify another server with its ID).",
    "es": "Guardar este servidor (puedes especificar otro servidor con su ID).",
    "jp": "このサーバーを保存します（別のサーバーをそのIDで指定できます）。"
}

help_backup_load = {
    "fr": "Charge une sauvegarde (vous pouvez indiquer un autre serveur avec son ID).",
    "en": "Load a backup (you can specify another server with its ID).",
    "es": "Cargar una copia de seguridad (puedes especificar otro servidor con su ID).",
    "jp": "バックアップをロードします（別のサーバーをそのIDで指定できます）。"
}

help_backup_delete = {
    "fr": "Supprime une backup avec son ID.",
    "en": "Delete a backup with its ID.",
    "es": "Eliminar una copia de seguridad con su ID.",
    "jp": "IDでバックアップを削除します。"
}

backup_no_permissions = {
    "fr": "Vous n'avez pas les permissions nécessaires pour charger cette backup.",
    "en": "You don't have the permissions to load this backup.",
    "es": "No tienes los permisos necesarios para cargar esta copia de seguridad.",
    "jp": "このバックアップをロードする権限がありません。"
}

####################
#  commands        #
# translation !!!  #
####################


restart_command = {
    "fr": "✅ Selfbot redémarré avec succès (patientez quelques secondes...) !",
    "en": "✅ Succesfully restarted the selfbot (wait a couple of seconds...)!",
    "es": "✅ Selfbot reiniciado con éxito (espere unos segundos...)",
    "jp": "✅ Selfbotが正常に再起動しました（数秒お待ちください...）！"
}

stop_command = {
    "fr": "⭕ Le selfbot a bien été stoppé.",
    "en": "⭕ Succesfully stopped the selfbot.",
    "es": "⭕ Selfbot detenido correctamente.",
    "jp": "⭕ Selfbotが正常に停止しました。"
}

leave_voice = {
    "fr": "Déconnection du salon",
    "en": "Disconnected from",
    "es": "Desconectado de",
    "jp": "ボイスチャンネルから切断しました"
}

leave_voice_error = {
    "fr": "Erreur lors de la déconnexion au salon vocal",
    "en": "Error while leaving the voice channel",
    "es": "Error al salir del canal de voz",
    "jp": "ボイスチャンネルからの切断中にエラーが発生しました"
}

leave_voice_error_not_found = {
    "fr": "❌ Vous devez être connecté à un salon vocal pour utiliser cette commande !",
    "en": "❌ You must be connected to a voice channel to use this command!",
    "es": "❌ Debes estar conectado a un canal de voz para usar este comando!",
    "jp": "❌ このコマンドを使用するにはボイスチャンネルに接続している必要があります！"
}

voice_channel_error = {
    "fr": "❌ Veuillez indiquer un ID de salon vocal valide !",
    "en": "❌ Please enter a valid voice channel ID!",
    "es": "❌ ¡Por favor ingresa un ID de canal de voz válido!",
    "jp": "❌ 有効なボイスチャンネルIDを入力してください！"
}

voice_channel_error_not_found = {
    "fr": "❌ Le salon vocal avec cet ID n'existe pas.",
    "en": "❌ Unable to find the voice channel!",
    "es": "❌ ¡No se puede encontrar el canal de voz con ese ID!",
    "jp": "❌ 指定されたボイスチャンネルが見つかりません。"
}

hype_command = {
    "fr": "modifié en",
    "en": "changed to",
    "es": "cambiado a",
    "jp": "に変更されました"
}

hype_fail = {
    "fr": "❌ HypeSquad renseignée incorrect. (brilliance, balance, bravery).",
    "en": "❌ Given HypeSquad house is incorrect. (brilliance, balance, bravery).",
    "es": "❌ La casa de HypeSquad dada es incorrecta. (brilliance, balance, bravery).",
    "jp": "❌ 与えられた HypeSquad ハウスが間違っています。 (brilliance, balance, bravery)."
}

bio_command = {
    "fr": "changée en",
    "en": "changed to",
    "es": "cambiado a",
    "jp": "に変更されました"
}

spam_cooldown = {
    "fr": f"❌ Un spam est déjà en cours ! Pour l'arrêter, faites `{config_selfbot.prefix}restart`.",
    "en": f"❌ A spam is already active! To spam the current spam, do `{config_selfbot.prefix}restart`.",
    "es": f"❌ ¡Ya hay un spam activo! Para detener el spam actual, haz `{config_selfbot.prefix}restart`.",
    "jp": f"❌ スパムが既にアクティブです！ 現在のスパムを停止するには、`{config_selfbot.prefix}restart` を行ってください。"
}

spam_invalid = {
    "fr": "❌ Veuillez indiquer un nombre valide !",
    "en": "❌ You must enter a valid number!",
    "es": "❌ ¡Debes ingresar un número válido!",
    "jp": "❌ 有効な数字を入力してください！"
}

spam_too_much = {
    "fr": "❌ Veulliez indiquer une valeur en dessous de 100 !",
    "en": "❌ Please enter a value below 100!",
    "es": "❌ ¡Por favor ingresa un valor por debajo de 100!",
    "jp": "❌ 100以下の値を入力してください！"
}

only_dm_fun = {
    "fr": "❌ Cette commande n'est disponible qu'en MP!",
    "en": "❌ You must use this command in DM!",
    "es": "❌ ¡Debes usar este comando en DM!",
    "jp": "❌ このコマンドはDMでのみ使用できます！"
}

voice_join = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to",
    "es": "Conectado a",
    "jp": "ボイスチャンネルに接続しました"
}

voice_join_error = {
    "fr": "Erreur lors de la connexion au salon vocal",
    "en": "Error while trying to connect to the voice channel",
    "es": "Error al intentar conectarse al canal de voz",
    "jp": "ボイスチャンネルへの接続中にエラーが発生しました"
}

voice_join_cam = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to",
    "es": "Conectado a",
    "jp": "ボイスチャンネルに接続しました"
}

voice_join_cam_two = {
    "fr": "avec la caméra activée",
    "en": "with camera",
    "es": "con cámara",
    "jp": "カメラを使用して"
}

nitro_sniper_claimed = {
    "fr": "a déjà été réclamé par quelqu'un d'autre !",
    "en": "was already redeemed by someone else!",
    "es": "¡Ya ha sido reclamado por otra persona!",
    "jp": "はすでに他の誰かによって引き換えられました！"
}

nitro_sniper_valid = {
    "fr": "a bien été réclamé sur le compte !",
    "en": "has been claimed on the account!",
    "es": "ha sido reclamado en la cuenta!",
    "jp": "はアカウントで請求されました！"
}

nitro_sniper_invalid_code = {
    "fr": "est invalide !",
    "en": "is invalid!",
    "es": "¡es inválido!",
    "jp": "は無効です！"
}

fun_hack_step_one = {
    "fr": "aquage de",
    "en": "hacking",
    "es": "hackeo de",
    "jp": "ハッキング"
}

fun_hack_step_two = {
    "fr": "récupération de l'adresse mail",
    "en": "getting email address",
    "es": "obteniendo dirección de correo electrónico",
    "jp": "メールアドレスの取得"
}

fun_hack_step_three = {
    "fr": "adresse mail trouvée",
    "en": "found email address",
    "es": "se encontró la dirección de correo electrónico",
    "jp": "メールアドレスが見つかりました"
}

fun_hack_step_four = {
    "fr": "spam à tout ses contaktes...",
    "en": "spamming all contacts",
    "es": "enviando spam a todos los contactos",
    "jp": "すべての連絡先にスパムを送信中..."
}

fun_hack_step_five = {
    "fr": "g bien aquer",
    "en": "successfully hacked",
    "es": "hackeado exitosamente",
    "jp": "正常にハックされました"
}

fun_copy_user_fail = {
    "fr": "❌ Veuillez indiquer un utilisateur à copier (ID ou mention).",
    "en": "❌ Please give an ID / mention for the user to copy.",
    "es": "❌ Por favor, da un ID / mención para copiar al usuario.",
    "jp": "❌ ユーザーのIDまたはメンションを指定してください。"
}

fun_token = {
    "fr": "Début du token de",
    "en": "Start of the token of",
    "es": "Inicio del token de",
    "jp": "トークンの開始"
}

info_title = {
    "fr": "Informations sur",
    "en": "Informations about",
    "es": "Información sobre",
    "jp": "に関する情報"
}

info_global = {
    "fr": "Nom d'affichage",
    "en": "Display name",
    "es": "Nombre de visualización",
    "jp": "表示名"
}

info_banner = {
    "fr": "Bannière",
    "en": "Banner",
    "es": "Banner",
    "jp": "バナー"
}

info_created_at = {
    "fr": "Créé le",
    "en": "Created at",
    "es": "Creado el",
    "jp": "作成日"
}

info_avatar = {
    "fr": "Photo de profil",
    "en": "Avatar",
    "es": "Avatar",
    "jp": "アバター"
}

info_avatar_link = {
    "fr": "Lien vers la photo",
    "en": "Avatar's link",
    "es": "Enlace del avatar",
    "jp": "アバターのリンク"
}

info_banner_link = {
    "fr": "Lien vers la bannière",
    "en": "Banner's link",
    "es": "Enlace del banner",
    "jp": "バナーのリンク"
}

info_roles = {
    "fr": "Rôles",
    "en": "Roles",
    "es": "Roles",
    "jp": "役職"
}

info_username = {
    "fr": "Nom d'utilisateur",
    "en": "Username",
    "es": "Nombre de usuario",
    "jp": "ユーザー名"
}

raid_in_process = {
    "fr": "☣️ Raid en cours...",
    "en": "☣️ Raid in progress...",
    "es": "☣️ Raid en progreso...",
    "jp": "☣️ レイド進行中..."
}

raid_error_permisssion = {
    "fr": "‼️ Permission manquantes !",
    "en": "‼️ Missing permissions!",
    "es": "‼️ Permisos faltantes!",
    "jp": "‼️ 不足している権限！"
}

raid_kick_all_success = {
    "fr": "✅ Tout les membres ont été kick du serveur avec succès.",
    "en": "✅ Succesfully kicked all members.",
    "es": "✅ Todos los miembros fueron expulsados con éxito.",
    "jp": "✅ すべてのメンバーが正常にキックされました。"
}

raid_ban_all_success = {
    "fr": "✅ Tout les membres ont été bannis du serveur avec succès.",
    "en": "✅ Succesfully banned all members.",
    "es": "✅ Todos los miembros fueron baneados con éxito.",
    "jp": "✅ すべてのメンバーが正常に禁止されました。"
}

raid_dm_all = {
    "fr": "☣️ Envoi du message privée à toute la liste d'amis...",
    "en": "☣️ Sending the message to all friends...",
    "es": "☣️ Enviando el mensaje a todos los amigos...",
    "jp": "☣️ すべての友達にメッセージを送信中..."
}

raid_dm_all_fail = {
    "fr": "❌ Vous devez renseigner un message !",
    "en": "❌ You must enter a message!",
    "es": "❌ ¡Debes ingresar un mensaje!",
    "jp": "❌ メッセージを入力する必要があります！"
}

raid_dm_all_captcha = {
    "fr": "❌ Amis trop nombreux. Captcha requis !",
    "en": "❌ Too many friends. Captcha required!",
    "es": "❌ Demasiados amigos. ¡Se requiere captcha!",
    "jp": "❌ 友達が多すぎます。キャプチャが必要です！"
}

raid_dm_all_success = {
    "fr": "✅ Message envoyé avec succès à la liste d'amis !",
    "en": "✅ Succesfully sent message to all friends!",
    "es": "✅ Mensaje enviado con éxito a todos los amigos!",
    "jp": "✅ すべての友達にメッセージが正常に送信されました！"
}

tool_close_dms = {
    "fr": "🔧 Fermeture de tout vos MP...",
    "en": "🔧 Closing all your DMs...",
    "es": "🔧 Cerrando todos tus DMs...",
    "jp": "🔧 すべてのDMを閉じる..."
}

tool_bump = {
    "fr": "🔁 Le serveur sera bump sur ce salon",
    "en": "🔁 This server will be bumped on this channel",
    "es": "🔁 Este servidor será bump en este canal",
    "jp": "🔁 このサーバーはこのチャンネルでバンプされます"
}

tool_bump_not_found = {
    "fr": "❌ Le bot Disboard n'a pas été trouvé sur ce serveur.",
    "en": "❌ Disboard wasn't found on this server.",
    "es": "❌ No se encontró Disboard en este servidor.",
    "jp": "❌ このサーバーでDisboardが見つかりませんでした。"
}

tool_bump_two = {
    "fr": "fois.",
    "en": "times.",
    "es": "veces.",
    "jp": "回。"
}

tool_close_dms_success = {
    "fr": "✅ Tout vos MP ont bien été fermés !",
    "en": "✅ All of your DMs have been closed!",
    "es": "✅ Todos tus DMs han sido cerrados!",
    "jp": "✅ すべてのDMが閉じられました！"
}

tool_close_dms_bots = {
    "fr": "🔧 Fermeture de tout vos MP avec des bots...",
    "en": "🔧 Closing all your DMs with bots...",
    "es": "🔧 Cerrando todos tus DMs con bots...",
    "jp": "🔧 ボットとのすべてのDMを閉じる..."
}

tool_close_dms_bots_success = {
    "fr": "✅ Tout vos MP avec des bots ont bien été fermés !",
    "en": "✅ All of your DMs with bots have been closed!",
    "es": "✅ Todos tus DMs con bots han sido cerrados!",
    "jp": "✅ すべてのボットとのDMが閉じられました！"
}

####################
#  rpc             #
# translation !!!  #
####################
rpc_name_translate = {
    "fr": "Défini le nom du RPC",
    "en": "Set RPC's name",
    "es": "Establecer el nombre del RPC",
    "jp": "RPCの名前を設定する"
}

rpc_details_translate = {
    "fr": "Défini les details du RPC",
    "en": "Set RPC's details",
    "es": "Establecer los detalles del RPC",
    "jp": "RPCの詳細を設定する"
}

rpc_state_translate = {
    "fr": "Défini le \"state\" du RPC",
    "en": "Set RPC's state",
    "es": "Establecer el estado del RPC",
    "jp": "RPCの状態を設定する"
}

rpc_url_translate = {
    "fr": "Défini l'url de steaming du RPC ``(https://twitch.tv/nom)``",
    "en": "Set RPC's streaming URL ``(https://twitch.tv/name)``",
    "es": "Establecer la URL de streaming del RPC ``(https://twitch.tv/nombre)``",
    "jp": "RPCのストリーミングURLを設定する ``(https://twitch.tv/name)``"
}

rpc_type_translate = {
    "fr": "Défini le type de votre RPC (game / watch / listen / stream)",
    "en": "Set RPC's type (game / watch / listen / stream)",
    "es": "Establecer el tipo de tu RPC (game / watch / listen / stream)",
    "jp": "RPCのタイプを設定する (game / watch / listen / stream)"
}

rpc_large_image_translate = {
    "fr": "Défini la grande image du RPC",
    "en": "Set RPC's large image",
    "es": "Establecer la imagen grande del RPC",
    "jp": "RPCの大きな画像を設定する"
}

rpc_large_text_translate = {
    "fr": "Défini le texte de la grande image du RPC",
    "en": "Set RPC's large image text",
    "es": "Establecer el texto de la imagen grande del RPC",
    "jp": "RPCの大きな画像のテキストを設定する"
}

rpc_small_image_translate = {
    "fr": "Défini la petite image du RPC",
    "en": "Set RPC's small image",
    "es": "Establecer la imagen pequeña del RPC",
    "jp": "RPCの小さな画像を設定する"
}

rpc_small_text_translate = {
    "fr": "Défini le texte de la petite image du RPC",
    "en": "Set RPC's small image text",
    "es": "Establecer el texto de la imagen pequeña del RPC",
    "jp": "RPCの小さな画像のテキストを設定する"
}

rpc_button_text_one_translate = {
    "fr": "Défini le texte du premier bouton du RPC",
    "en": "Set RPC's first button text",
    "es": "Establecer el texto del primer botón del RPC",
    "jp": "RPCの最初のボタンのテキストを設定する"
}

rpc_button_link_one_translate = {
    "fr": "Défini le lien du premier bouton du RPC",
    "en": "Set RPC's first button link",
    "es": "Establecer el enlace del primer botón del RPC",
    "jp": "RPCの最初のボタンのリンクを設定する"
}

rpc_button_text_two_translate = {
    "fr": "Défini le texte du second bouton du RPC",
    "en": "Set RPC's second button text",
    "es": "Establecer el texto del segundo botón del RPC",
    "jp": "RPCの2番目のボタンのテキストを設定する"
}

rpc_button_link_two_translate = {
    "fr": "Défini le lien du second bouton du RPC",
    "en": "Set RPC's second button link",
    "es": "Establecer el enlace del segundo botón del RPC",
    "jp": "RPCの2番目のボタンのリンクを設定する"
}



####################
# template         #
# translation !!!  #
####################

template_help_reset = {
    "fr": "Réinitialise votre RPC.",
    "en": "Reset your RPC.",
    "es": "Restablecer tu RPC.",
    "jp": "RPCをリセットする。"
}

template_help_clear = {
    "fr": "Supprime votre RPC.",
    "en": "Clear your RPC.",
    "es": "Borrar tu RPC.",
    "jp": "RPCをクリアする。"
}

template_help_default = {
    "fr": "Modifie votre RPC par celui présent dans (`config_selfbot.py`).",
    "en": "Edit your RPC to the default one (in `config_selfbot.py`).",
    "es": "Editar tu RPC al predeterminado (en `config_selfbot.py`).",
    "jp": "`config_selfbot.py`でデフォルトのRPCに編集する。"
}

template_help_cod = {
    "fr": "Utilise la template \"Call Of Duty\".",
    "en": "Use \"Call Of Duty\"'s template.",
    "es": "Usar la plantilla \"Call Of Duty\".",
    "jp": "\"Call Of Duty\"のテンプレートを使用する。"
}

template_help_dark = {
    "fr": "Utilise la template \"dark\".",
    "en": "Use \"dark\" template.",
    "es": "Usar la plantilla \"dark\".",
    "jp": "\"dark\"のテンプレートを使用する。"
}

template_help_python = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template.",
    "es": "Usar la plantilla \"Python\".",
    "jp": "\"Python\"のテンプレートを使用する。"
}

template_help_js = {
    "fr": "Utilise la template \"JavaScript\".",
    "en": "Use \"JavaScript\" template.",
    "es": "Usar la plantilla \"JavaScript\".",
    "jp": "\"JavaScript\"のテンプレートを使用する。"
}

template_help_omori = {
    "fr": "Utilise la template \"Omori\".",
    "en": "Use \"Omori\" template.",
    "es": "Usar la plantilla \"Omori\".",
    "jp": "\"Omori\"のテンプレートを使用する。"
}

template_help_car = {
    "fr": "Utilise la template \"Car\".",
    "en": "Use \"Car\" template.",
    "es": "Usar la plantilla \"Car\".",
    "jp": "\"Car\"のテンプレートを使用する。"
}

template_help_self = {
    "fr": "Utilise la template \"Nuclear\".",
    "en": "Use \"Nuclear\" template.",
    "es": "Usar la plantilla \"Nuclear\".",
    "jp": "\"Nuclear\"のテンプレートを使用する。"
}

template_help_webdeck = {
    "fr": "Utilise la template \"WebDeck\".",
    "en": "Use \"WebDeck\" template.",
    "es": "Usar la plantilla \"WebDeck\".",
    "jp": "\"WebDeck\"のテンプレートを使用する。"
}

template_help_hi = {
    "fr": "Utilise la template \"Hi !\".",
    "en": "Use \"Hi !\" template.",
    "es": "Usar la plantilla \"Hi !\".",
    "jp": "\"Hi !\"のテンプレートを使用する。"
}

template_help_youtube = {
    "fr": "Utilise la template \"YouTube\".",
    "en": "Use \"YouTube\" template.",
    "es": "Usar la plantilla \"YouTube\".",
    "jp": "\"YouTube\"のテンプレートを使用する。"
}

template_help_gta = {
    "fr": "Utilise la template \"GTA VI\".",
    "en": "Use \"GTA VI\" template.",
    "es": "Usar la plantilla \"GTA VI\".",
    "jp": "\"GTA VI\"のテンプレートを使用する。"
}

template_help_tiktok = {
    "fr": "Utilise la template \"TikTok\".",
    "en": "Use \"TikTok\" template.",
    "es": "Usar la plantilla \"TikTok\".",
    "jp": "\"TikTok\"のテンプレートを使用する。"
}

template_help_reload = {
    "fr": f"Vous pouvez mettre à jour les images avec la commande `{config_selfbot.prefix}reload` !",
    "en": f"You can reload Templates images with the `{config_selfbot.prefix}reload` command!",
    "es": f"Puedes recargar las imágenes de las plantillas con el comando `{config_selfbot.prefix}reload` !",
    "jp": f"`{config_selfbot.prefix}reload`コマンドでテンプレート画像をリロードできます！"
}

template_reload = {
    "fr": "✅ Images des Templates mises à jour !",
    "en": "✅ Templates images updated!",
    "es": "✅ Imágenes de las plantillas actualizadas!",
    "jp": "✅ テンプレート画像が更新されました！"
}

rpc_cod_details = {
    "fr": "En attente de mission...",
    "en": "Waiting for a mission...",
    "es": "Esperando una misión...",
    "jp": "ミッション待ち..."
}

rpc_cod_state = {
    "fr": "Menu principal",
    "en": "In the main menu",
    "es": "En el menú principal",
    "jp": "メインメニューにいます"
}

tutorial_rpc = {
    "fr": f""" Pour obtenir une image personnalisée:
  1. Envoyez une image (gif, png...) dans Discord (dans n'importe quel salon).
  2. Cliquez avec le bouton droit et "Copiez l'adresse de l'image".
  3. Utilisez la commande `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/exemple.png`.
  4. C'est fait !""",
    "en": f""" To get a custom RPC image, follow these steps:
  1. Upload an image (gif, png...) in Discord (in any channel).
  2. Right-click and "Copy Image Link".
  3. Use the command `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png`.
  4. Done!""",
    "es": f""" Para obtener una imagen personalizada de RPC, sigue estos pasos:
  1. Sube una imagen (gif, png...) a Discord (en cualquier canal).
  2. Haz clic derecho y "Copiar enlace de la imagen".
  3. Utiliza el comando `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/ejemplo.png`.
  4. ¡Listo!""",
    "jp": f""" カスタムRPC画像を取得するには、次の手順に従ってください：
  1. Discordに画像（gif、pngなど）をアップロードします（どのチャンネルでも）。
  2. 右クリックして「画像リンクをコピー」します。
  3. コマンド `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png` を使用します。
  4. 完了！"""
}

backup_saving = {
    "fr": "🔁 Création de la sauvegarde en cours...",
    "en": "🔁 Creating backup...",
    "es": "🔁 Creando respaldo...",
    "jp": "🔁 バックアップを作成しています..."
}

backup_not_find_folder = {
    "fr": "❌ Impossible de trouver le dossier 'backups' !",
    "en": "❌ Unable to find the 'backups' folder!",
    "es": "❌ No se puede encontrar la carpeta 'backups'!",
    "jp": "❌ 'backups'フォルダが見つかりません！"
}

backup_success_save = {
    "fr": "✅ Sauvegarde réussie pour le serveur",
    "en": "✅ Successfully saved guild",
    "es": "✅ Servidor guardado con éxito",
    "jp": "✅ サーバーの保存に成功しました"
}

backup_save_already_exist = {
    "fr": "❌ Une sauvegarde pour",
    "en": "❌ A save for",
    "es": "❌ Ya existe un respaldo para",
    "jp:": "❌ 保存済み"
}

backup_save_already_exist_two = {
    "fr": f"existe déjà. Utilisez `{config_selfbot.prefix}delete <server_id>` pour la supprimer.",


    "en:": f"already exists. Use `{config_selfbot.prefix}delete <server_id>` to remove it.",
    "es": f"ya existe. Usa `{config_selfbot.prefix}delete <server_id>` para eliminarlo.",
    "jp": f"既に存在します。削除するには `{config_selfbot.prefix}delete <server_id>` を使用してください。"
}

no_backup_error = {
    "fr": "❌ Aucune sauvegarde disponible.",
    "en": "❌ No backup available.",
    "es": "❌ No hay respaldo disponible.",
    "jp": "❌ バックアップはありません。"
}

backup_list = {
    "fr": "Backups disponibles:\n",
    "en": "Severs backups:\n",
    "es": "Respaldo de servidores:\n",
    "jp": "利用可能なサーバーバックアップ：\n"
}

backup_invalid = {
    "fr": f"❌ Aucune sauvegarde disponible pour cet ID. Utilisez `{config_selfbot.prefix}backups` pour voir les sauvegardes disponibles !",
    "en": f"❌ No backup available for this server ID. Use `{config_selfbot.prefix}backups` to see available backups!",
    "es": f"❌ No hay respaldo disponible para este ID de servidor. Usa `{config_selfbot.prefix}backups` para ver los respaldos disponibles.",
    "jp": f"❌ このサーバーIDのバックアップは利用できません。`{config_selfbot.prefix}backups` を使用して利用可能なバックアップを確認してください！"
}

backup_id_required = {
    "fr": "❌ Vous devez indiquer un ID de serveur !",
    "en": "❌ You must indicate a server ID!",
    "es": "❌ Debes indicar un ID de servidor!",
    "jp": "❌ サーバーIDを指定する必要があります！"
}

backup_done = {
    "fr": "✅ Backup effectué avec succès !",
    "en": "✅ Backup done successfully!",
    "es": "✅ Respaldo realizado con éxito!",
    "jp": "✅ バックアップが正常に完了しました！"
}

backup_delete_done = {
    "fr": "✅ Backup supprimé avec succès !",
    "en": "✅ Backup deleted successfully!",
    "es": "✅ Respaldo eliminado exitosamente!",
    "jp": "✅ バックアップが正常に削除されました！"
}
