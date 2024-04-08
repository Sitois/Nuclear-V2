[![Version française](https://img.shields.io/badge/Lire%20en-Fran%C3%A7ais-blue?style=for-the-badge&logo=appveyor)](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md)



# 🌌 Nuclear-V2
### A powerful Discord Selfbot written in Python using [discord.py-self](https://github.com/dolfies/discord.py-self)! ###

<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=65be55bf&is=65abe0bf&hm=40a3c63ca07dfac28726eadae220a07412551a69deea021b73c24ae00933782e&=&format=webp&quality=lossless" alt="icon" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/releases)
  [![GitHub downloads](https://img.shields.io/github/downloads/Sitois/Nuclear-V2/total.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/releases)
  [![GitHub stars](https://img.shields.io/github/stars/Sitois/Nuclea-V2r.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/stargazers)
  [![GitHub watchers](https://img.shields.io/github/watchers/Sitois-V2/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/watchers)
  [![CodeFactor](https://www.codefactor.io/repository/github/Sitois/Nuclear-V2/badge?style=flat)](https://www.codefactor.io/repository/github/Sitois/Nuclear-V2)
  [![GitHub issues](https://img.shields.io/github/issues/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Sitois/Nuclear-V2/issues)
  [![Support](https://shields.yoki-labs.xyz/shields/i/kQj8PmAp?style=flat)](https://www.guilded.gg/i/kQj8PmAp?cid=c7d78c47-5231-47fa-b388-e11d41360e2a&intent=chat)
</div>

## ⛔ Disclaimer
**Discord SelfBots are not allowed by Discord TOS and can easily ban your account. Please use for educational purposes only.**

## 📖 Table of content
1. [💾 Installation](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-installation)
2. [🔧 Config](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-config)
3. [🌟 Features](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-features)
4. [📜 How to get a user token](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-how-to-get-a-token)
5. [👀 Preview](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-preview)
6. [☣️ Issues](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#%EF%B8%8F-issues)
7. [⭐ Contributors](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-contributors)
7. [🫂 Support](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#support)

## 💾 Installation

1. Download the latest version from the [Releases](https://github.com/Sitois/Nuclear-V2/releases) section on GitHub.
2. Make sure to have [Python](https://www.python.org/downloads/ "Install Python here") installed.
3. Open your Terminal and go to Nuclear with `cd`.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python selfbot.py`

## 🔧 Config
Open `config_selfbot.py` with any text editor.

## 🌟 Features
* Custom RPC templates,
* Build your own RPC,
* Voice commands,
* Nitro Sniper,
* AI command,
* Spam and Flood command,
* Snipe command,
* And others, check the `Help` command!

## 📜 How to get a user token
1. Go to [Discord Web](https://discord.com/app)
2. Do ``CTRL + MAJ + I`` and go to `Console`
3. Paste this code:
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
Now your token is in your clipboard.
<br>
4. Paste your token in `config_selfbot.py`

## 👀 Preview
<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1206262903427170334/FtTnNGY.png?ex=65db5edf&is=65c8e9df&hm=29286b2127bab0abf906413138924631942c5abb69d7b56cf506295ef5ed2234&=&format=webp&quality=lossless" alt="preview" width="" height="">
</div>
<br>
<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1206253306360496259/EcJ09br.png?ex=65db55ef&is=65c8e0ef&hm=078cf750eb91ca80100bf59f478fbb3254647fd825a4d622b1a6d2af6b3a9912&=&format=webp&quality=lossless" alt="preview_second" width="" height="">
</div>


<br>

## ☣️ Issues
THERE IS NO ISSUES !!&!11!!!! (if you get one, come on the [guilded](https://guilded.gg/nuclear) !!)

## ⭐ Contributors
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

A big thank to Lenoch ! Check her current [project](https://github.com/Lenochxd/WebDeck)!

And a big thank to Shell1010 for helping me during the developement of the first version!

# Support
- Guilded server: [https://guilded.gg/nuclear](https://guilded.gg/nuclear)

<br>

---

Project Code Time: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

My total Code Time: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401.svg?style=flat)](https://wakatime.com/@018af69f-9d50-4699-932d-026a9efb0401)