#!/bin/bash

# Installer les dépendances nécessaires
pip install colorama requests pynacl python-dotenv aiohttp

# Télécharger la version correcte de discord.py-self depuis les releases de Nuclear-V2
echo "Téléchargement de la version compatible de discord.py-self..."
mkdir -p ./discord_py_self_temp
curl -L -o discord.py-self.zip https://github.com/Sitois/Nuclear-V2/releases/latest/download/discord.py-self.zip || {
  echo "Échec du téléchargement depuis les releases. Tentative alternative..."
  # Si le téléchargement échoue, essayer d'installer depuis le dépôt Git
  pip install git+https://github.com/dolfies/discord.py-self.git
}

if [ -f discord.py-self.zip ]; then
  unzip -o discord.py-self.zip -d ./discord_py_self_temp
  if [ -d ./discord_py_self_temp ]; then
    pip install -e ./discord_py_self_temp || echo "Échec de l'installation du package local"
  fi
  rm -rf discord.py-self.zip
fi

# Créer un petit serveur web pour satisfaire l'exigence de port de Render
echo "Création d'un serveur web pour Render..."
cat > webserver.py << 'EOF'
import threading
import http.server
import socketserver
import os

def run_web_server():
    PORT = int(os.getenv('PORT', 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Démarrer le serveur web dans un thread séparé
threading.Thread(target=run_web_server, daemon=True).start()
EOF

# Lancer le selfbot avec le serveur web
python -c "import webserver; webserver.run_web_server()" &
python main.py 
