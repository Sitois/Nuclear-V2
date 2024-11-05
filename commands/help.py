# Translation:
# You can put any poetry, no need to translate specifically these
poetry = {"fr": [
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
            "Les éclats de lumière percent l'obscurité la plus profonde.",
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
            "Don't watch the clock; do what it does. Keep going.",
            ],
            "es": [
            "Tu actitud determina tu dirección.",
            "Progreso, no perfección.",
            "Abraza los desafíos, porque son los peldaños hacia el éxito.",
            "Abraza el fracaso como un peldaño, no como un obstáculo.",
            "Los únicos límites que existen son los que te impones a ti mismo.",
            "El coraje no es la ausencia de miedo, sino el triunfo sobre él.",
            "Los sueños no funcionan a menos que tú lo hagas.",
            "Las oportunidades no suceden. Tú las creas.",
            "No esperes el momento perfecto; toma el momento y hazlo perfecto.",
            "La única manera de hacer un gran trabajo es amar lo que haces.",
            "Cree que puedes, y ya estás a mitad de camino.",
            "No mires el reloj; haz lo que hace. Sigue adelante.",
            "Un meilleur día solo existe con dolor.",
            "La única persona que estás destinado a convertirte es la persona que decides ser.",
            "El futuro pertenece a aquellos que creen en la belleza de sus sueños.",
            "El fracaso es la base del éxito.",
            "No sueñes tu vida, vive tus sueños.",
            "Cree en ti mismo, y los demás te seguirán.",
            "Sé el cambio que quieres ver en el mundo.",
            "Persigue tus sueños, ellos conocen el camino.",
            "La vida recompensa la acción.",
            "Eres más fuerte de lo que crees.",
            "El éxito comienza con la acción.",
            "La perseverancia supera al talento.",
            "No dejes para mañana.",
            "Cada esfuerzo cuenta.",
            "Las montañas más altas tienen las pendientes más empinadas.",
            "Los destellos de luz atraviesan la oscuridad más profunda.",
            ],
            "jp": [
            "あなたの態度があなたの方向を決めます。",
            "完璧さではなく、進歩。",
            "挑戦を受け入れ、それが成功への踏み石であることを認識してください。",
            "失敗を障害ではなく、踏み石として受け入れましょう。",
            "存在する限界は、自分が設ける限界だけです。",
            "勇気は恐怖の不在ではなく、それを克服することです。",
            "夢は、あなたが働かなければ実現しません。",
            "機会は起こるものではありません。あなたが作り出します。",
            "完璧な瞬間を待たず、その瞬間を完璧にしましょう。",
            "素晴らしい仕事をする唯一の方法は、あなたがしていることを愛することです。",
            "自分ができると信じれば、半分は達成したも同然です。",
            "時計を見てはいけません; 時計のように行動し続けましょう。",
            "より良い日々は痛みと共にしか存在しません。",
            "あなたがなるべき唯一の人は、あなたが決めた人です。",
            "未来は、自分の夢の美しさを信じる人々のものです。",
            "失敗は成功の基盤です。",
            "人生を夢見るのではなく、夢を生きましょう。",
            "自分を信じれば、他の人もついてきます。",
            "世界で見たい変化になりましょう。",
            "夢を追いかけてください、それらは道を知っています。",
            "人生は行動を報います。",
            "あなたは自分が思うよりも強いです。",
            "成功は行動から始まります。",
            "忍耐は才能に勝ります。",
            "明日まで延ばさないでください。",
            "すべての努力が大切です。",
            "最も高い山は最も急な斜面を持っています。",
            "光の閃光は最も深い暗闇を貫きます。",
            ],
}

from discord.ext import commands
import random

import config_selfbot
from utils import lang


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context):
        # Command pour afficher l'aide avec une citation aléatoire
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name}:**__ ☄
  ☄ "{random.choice(poetry[config_selfbot.lang])}" ☄

  📂| __**{lang.text('help_utils')}:**__ `{config_selfbot.prefix}utils`
  🎤| __**{lang.text('help_voice')}:**__ `{config_selfbot.prefix}voice`
  🕹️| __**{lang.text('help_rich_presence')}:**__ `{config_selfbot.prefix}presence`
  📖| __**{lang.text('help_templates')}:**__ `{config_selfbot.prefix}templates`
  🎲| __**{lang.text('help_fun')}:**__ `{config_selfbot.prefix}fun`
  🏯| __**{lang.text('help_raid')}:**__ `{config_selfbot.prefix}raid`
  🔧| __**{lang.text('help_tools')}:**__ `{config_selfbot.prefix}tools`
  ⚙️| __**{lang.text('help_config')}:**__ `{config_selfbot.prefix}config`
  🗃️| __**{lang.text('help_backup')}:**__ `{config_selfbot.prefix}backup`""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def backup(self, ctx: commands.Context):
        # Commande pour afficher les options de sauvegarde
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🗃️| __**{lang.text('help_backup')}:**__
 `{config_selfbot.prefix}backups`: {lang.text('help_backup_backups')}
 `{config_selfbot.prefix}save {lang.text('optional')}[<server_id>]`: {lang.text('help_backup_save')}
 `{config_selfbot.prefix}load <backup_id> {lang.text('optional')}[<server_id>]`: {lang.text('help_backup_load')}
 `{config_selfbot.prefix}delete`: {lang.text('help_backup_delete')}
 🖋️ {lang.text('help_backup_note')}
 💡 {lang.text('help_backup_tip')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def tools(self, ctx: commands.Context):
        # Commande pour afficher les outils disponibles
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🔧| __**{lang.text('help_tools')}:**__
 `{config_selfbot.prefix}closealldm`: {lang.text('help_tools_close_dm')}
 `{config_selfbot.prefix}botclosedm`: {lang.text('help_tools_close_dm_bots')}
 `{config_selfbot.prefix}dmall`: {lang.text('help_tools_dmall')}
 `{config_selfbot.prefix}bump <amount>`: {lang.text('help_tools_bump')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def fun(self, ctx: commands.Context):
        # Commande pour afficher les commandes amusantes
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎲| __**{lang.text('help_fun')}:**__
 `{config_selfbot.prefix}joke`: {lang.text('help_fun_joke')}
 `{config_selfbot.prefix}fact`: {lang.text('help_fun_fact')}
 `{config_selfbot.prefix}quote`: {lang.text('help_fun_quote')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def presence(self, ctx: commands.Context):
        # Commande pour afficher les options de présence
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🕹️| __**{lang.text('help_rich_presence')}:**__
 `{config_selfbot.prefix}richpresence`: {lang.text('help_rich_presence_update')}
 `{config_selfbot.prefix}setactivity`: {lang.text('help_rich_presence_set')}
 `{config_selfbot.prefix}setstatus`: {lang.text('help_rich_presence_status')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def templates(self, ctx: commands.Context):
        # Commande pour afficher les modèles disponibles
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

📖| __**{lang.text('help_templates')}:**__
 `{config_selfbot.prefix}addtemplate <name>`: {lang.text('help_templates_add')}
 `{config_selfbot.prefix}removetemplate <name>`: {lang.text('help_templates_remove')}
 `{config_selfbot.prefix}templatelist`: {lang.text('help_templates_list')}
 `{config_selfbot.prefix}edittemplate <name>`: {lang.text('help_templates_edit')}
 `{config_selfbot.prefix}showtemplate <name>`: {lang.text('help_templates_show')}
 `{config_selfbot.prefix}use <name>`: {lang.text('help_templates_use')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def voice(self, ctx: commands.Context):
        # Commande pour afficher les options de voix
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎤| __**{lang.text('help_voice')}:**__
 `{config_selfbot.prefix}join`: {lang.text('help_voice_join')}
 `{config_selfbot.prefix}leave`: {lang.text('help_voice_leave')}
 `{config_selfbot.prefix}play <url>`: {lang.text('help_voice_play')}
 `{config_selfbot.prefix}pause`: {lang.text('help_voice_pause')}
 `{config_selfbot.prefix}resume`: {lang.text('help_voice_resume')}
 `{config_selfbot.prefix}stop`: {lang.text('help_voice_stop')}
 `{config_selfbot.prefix}skip`: {lang.text('help_voice_skip')}""", delete_after=config_selfbot.deltime)
