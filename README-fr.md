[![English version](https://img.shields.io/badge/Read%20in-english-blue?style=for-the-badge&logo=appveyor)](https://github.com/Sitois/Nuclear-V2/blob/main/README.md)


# 🌌 Nuclear
### Un puissant SelfBot Discord écrit en Python utilisant [discord.py-self](https://github.com/dolfies/discord.py-self)! ###

<div align="center">
  <img src="https://i.imgur.com/0Hc2Z9y.png" alt="icon" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/releases)
  [![GitHub downloads](https://img.shields.io/github/downloads/Sitois/Nuclear-V2/total.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/releases)
  [![GitHub stars](https://img.shields.io/github/stars/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/stargazers)
  [![GitHub watchers](https://img.shields.io/github/watchers/Sitois/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/watchers)
  [![CodeFactor](https://www.codefactor.io/repository/github/Sitois/Nuclear-V2/badge?style=flat)](https://www.codefactor.io/repository/github/Sitois/Nuclear-V2)
  [![GitHub issues](https://img.shields.io/github/issues/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/issues)
  [![Support](https://shields.yoki-labs.xyz/shields/i/kQj8PmAp?style=flat)](https://www.guilded.gg/i/kQj8PmAp?cid=c7d78c47-5231-47fa-b388-e11d41360e2a&intent=chat)
  [![Telegram Support](https://img.shields.io/endpoint?url=https%3A%2F%2Frunkit.io%2Fdamiankrawczyk%2Ftelegram-badge%2Fbranches%2Fmaster%3Furl%3Dhttps%3A%2F%2Ft.me%2Fnuclear_support)](https://t.me/nuclear_support)
</div>
<div align="center">

  [![Discord Support](https://dcbadge.limes.pink/api/server/https://discord.gg/2XRbQQQR8D)](https://discord.gg/2XRbQQQR8D)

## ⛔ Avertissement
**Les SelfBots ne sont pas autorisés par les CGU (ou TOS) de Discord et peuvent facilement entraîner le banissement de votre compte. Veuillez utiliser ce script uniquement à des fins éducatives.**

</div>

## 📖 Table des matières
1. [💾 Installation](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-installation)
2. [🔧 Configuration](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-configuration)
3. [🌟 Fonctionnalités](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-fonctionnalit%C3%A9s)
4. [📜 Comment obtenir son token](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-comment-obtenir-son-token)
5. [👀 Aperçu](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-aper%C3%A7u)
6. [☣️ Problèmes](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#%EF%B8%8F-probl%C3%A8mes)
7. [🛠️ Developement version](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#%EF%B8%8F-developement-version)
8. [❓ Comment contribuer](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-comment-contribuer)
9. [⭐ Contributeurs](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-contributeurs)
10. [🫂 Support](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#support)

## 💾 Installation

1. Téléchargez la dernière version depuis la section [Releases](https://github.com/Sitois/Nuclear-V2/releases) sur GitHub.
2. Assurez-vous d'avoir [Python](https://www.python.org/downloads/ "Installez Python ici") installé.
3. Ouvrez votre Terminal et rendez-vous dans le dossier Nuclear en utilisant `cd`.
4. Installez les dépendances : `pip install -r requirements.txt`
5. Exécutez le programme : `python main.py`
6. Commencez avec `&help` !

## 🔧 Configuration
Ouvrez `config_selfbot.py` avec n'importe quel éditeur de texte et saisissez un [token d'__utilisateur__](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#-comment-obtenir-son-token).

## 🌟 Fonctionnalités
* Templates RPC personnalisés,
* Créez votre propre RPC,
* Commandes vocal,
* Commandes de raids,
* MP nombreux (DM All),
* Nitro Sniper,
* Flood et Spam,
* Snipe,
* Et bien plus, consultez la commande `Help` !

## 📜 Comment obtenir son token
1. Rendez-vous sur [Discord Web](https://discord.com/app)
2. Faites ``CTRL + MAJ + I`` puis allez dans `Console`
3. Collez ce code:
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) return;
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```
Maintenant, votre token est dans votre presse-papier. <br><br>
3b. Si vous n'arrivez pas à coller ce code, écrivez `allow pasting` et réessayez. <br>
<br>
4. Collez votre token dans `config_selfbot.py`

## 👀 Aperçu
<div align="center">
  <img src="https://i.imgur.com/aMiocj8.png" alt="preview" width="" height="">
</div>
<br>
<div align="center">
  <img src="https://i.imgur.com/FP6kCj6.png" alt="preview_second" width="" height="">
</div>

<br>

## ☣️ Problèmes
Aucun problème n'a été trouvé pour le moment. (si t'en rencontre viesn sur le [Support](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md#support))

## 🛠️ Developement version
1. Ouvrez votre Terminal et rendez-vous dans le dossier souhaitée à l'aide de `cd`.
2. Clonez le repo: `git clone https://github.com/Sitois/Nuclear-V2`
**ou**
Clonez le repo avec le bouton vert "Code", au-dessus du README.


## ❓ Comment contribuer

🖤 Vous pouvez contribuer en laissant une star si vous aimez le projet ! <br>
🧷 Vous pouvez aussi le traduire (avec `langs.py`) ! <br>
Ou vous pouvez juste m'aider avec ma liste "besoin d'aide":
  - Captcha: Commentaires dans `main.py`

## ⭐ Contributeurs
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/Lenochxd">
        <img src="https://avatars.githubusercontent.com/u/101269524?s=64&v=4" alt="Lenochxd" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        Lenochxd
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Shell1010">
        <img src="https://avatars.githubusercontent.com/u/72198971?s=64&v=4" alt="Shell1010" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        Shell1010
      </a>
    </td>
<table>

Un grand merci à [Lenoch](https://github.com/Lenochxd) pour le README et pour m'avoir appris Python ;-; ! Jettez un oeuil à son [projet](https://github.com/Lenochxd/Webdeck) !

Un grand merci à [Shell1010](https://github.com/Shell1010) pour m'avoir aidé durant le développement de la première version !

# Support
- Serveur Guilded: [https://guilded.gg/nuclear](https://guilded.gg/nuclear)
- Serveur Discord: [https://discord.gg/2XRbQQQR8D](https://discord.gg/2XRbQQQR8D)
- Telegram news: [https://t.me/nuclear_support](https://t.me/nuclear_support)
- Telegram discussions / support: [https://t.me/+9t1ED-hddqhjOTRk](https://t.me/+9t1ED-hddqhjOTRk)

<br>

---

[![](https://visitcount.itsvg.in/api?id=Nuclear&label=Repo%20Views&color=2&icon=5&pretty=false)](https://visitcount.itsvg.in)

---

Nuclear-V1: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Nuclear-V2: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808)

Mon temps total de Code: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401.svg?style=flat)](https://wakatime.com/@018af69f-9d50-4699-932d-026a9efb0401)