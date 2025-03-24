#!/bin/bash

# Télécharger la version correcte de discord.py-self depuis les releases de Nuclear-V2
echo "Téléchargement de la version compatible de discord.py-self..."
curl -L -o discord.py-self.zip https://github.com/Sitois/Nuclear-V2/releases/latest/download/discord.py-self.zip
unzip -o discord.py-self.zip -d ./discord_py_self_temp
pip install -e ./discord_py_self_temp
rm -rf discord.py-self.zip

# Lancer le selfbot
python main.py 
