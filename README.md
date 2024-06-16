[![Version française](https://img.shields.io/badge/Lire%20en-Fran%C3%A7ais-blue?style=for-the-badge&logo=appveyor)](https://github.com/Sitois/Nuclear-V2/blob/main/README-fr.md)



# 🌌 Nuclear-V2
### A powerful Discord Selfbot written in Python using [discord.py-self](https://github.com/dolfies/discord.py-self)!

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

  ## ⛔ Disclaimer
  **Discord SelfBots are not allowed by Discord TOS and can easily ban your account. Please use for educational purposes only. This project is just a proof of concept.**
</div>

## 📖 Table of content
1. [💾 Installation](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-installation)
2. [🔧 Config](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-config)
3. [🌟 Features](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-features)
4. [📜 How to get a user token](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-how-to-get-a-user-token)
5. [👀 Preview](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-preview)
6. [☣️ Issues](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#%EF%B8%8F-issues)
7. [🛠️ Developement version](https://github.com/Sitois/Nuclear-V2#%EF%B8%8F-developement-version)
8. [❓ How to contribute](https://github.com/Sitois/Nuclear-V2#-how-to-contribute)
9. [⭐ Contributors](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-contributors)
10. [🫂 Support](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#support)

## 💾 Installation
1. Download the latest version from the [Releases](https://github.com/Sitois/Nuclear-V2/releases) section on GitHub.
2. Make sure to have [Python](https://www.python.org/downloads/ "Install Python here") installed.
3. Open your Terminal and go to Nuclear with `cd`.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python main.py`
6. Get started with `&help`!

## 🔧 Config
Open `config_selfbot.py` with any text editor  and enter a [user token](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#-how-to-get-a-user-token).

## 🌟 Features
* Custom RPC templates,
* Build your own RPC,
* Voice commands,
* Raid commands,
* Massive DM (DM All),
* Nitro Sniper,
* Spam and Flood command,
* Snipe command,
* Auto bump,
* Servers backup,
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
Now your token is in your clipboard. <br><br>
3b. If you can't paste the code, just type `allow pasting` and retry. <br>
<br>
4. Paste your token in `config_selfbot.py`

## 👀 Preview
<div align="center">
  <img src="https://i.imgur.com/aMiocj8.png" alt="preview" width="" height="">
</div>
<br>
<div align="center">
  <img src="https://i.imgur.com/FP6kCj6.png" alt="preview_second" width="" height="">
</div>


<br>

## ☣️ Issues
### Library Issues
`discord.py-self` has some issues.
<br>

One of the most common is when an incompatible library is already installed. To solve this problem, you can uninstall them:
```powershell
pip uninstall discord discord.py py-cord pycord nextcord discord.py-self aiohttp
```
And now, you just need to re-install discord.py-self (from Git or from [here](https://github.com/Sitois/Nuclear-V2/releases/latest))

If you still get an error, you can check [discord.py-self's support](https://t.me/dpy_self_discussions)
### Nuclear's issues
Check [support](https://github.com/Sitois/Nuclear-V2?tab=readme-ov-file#support)!

## 🛠️ Developement version
1. Open your Terminal and go to the wanted folder with `cd`.
2. Clone the repository: `git clone https://github.com/Sitois/Nuclear-V2`
**or**
Just clone it with the green "Code" button above the README.


## ❓ How to contribute

🖤 You can contribute by leaving a star if you love my project! <br>
🧷 You can also translate the selfbot (using `langs.py`)! <br>
Or you can just help me with my "need help" list:
  - Captcha: Check comments on `main.py`
  - Every "TODO:" in the code

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

A big thank to [Lenoch](https://github.com/Lenochxd) for the README and for learning me Python ;-; ! Check her current [project](https://github.com/Lenochxd/WebDeck)!

And a big thank to [Shell1010](https://github.com/Shell1010) for helping me during the developement of the first version!

# Support
- Guilded server: [https://guilded.gg/nuclear](https://guilded.gg/nuclear)
- Discord server: [https://discord.gg/2XRbQQQR8D](https://discord.gg/2XRbQQQR8D)
- Telegram news: [https://t.me/nuclear_support](https://t.me/nuclear_support)
- Telegram discussions / support: [https://t.me/+9t1ED-hddqhjOTRk](https://t.me/+9t1ED-hddqhjOTRk)

<br>

---

[![](https://visitcount.itsvg.in/api?id=Nuclear&label=Repo%20Views&color=2&icon=5&pretty=false)](https://visitcount.itsvg.in)

---
Nuclear-V1: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Nuclear-V2: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018e9e0c-29ce-4e43-9113-34945236a808)

My total Code Time: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401.svg?style=flat)](https://wakatime.com/@018af69f-9d50-4699-932d-026a9efb0401)