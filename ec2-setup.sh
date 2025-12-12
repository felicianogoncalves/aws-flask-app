#!/bin/bash
# Atualiza o sistema
apt update -y

# Instala Python e Git
apt install -y python3-pip git

# Clona o teu projeto do GitHub
git clone https://github.com/felicianogoncalves/aws-flask-app.git /home/ubuntu/app

# Entra na pasta
cd /home/ubuntu/app

# Instala o Flask
pip3 install -r requirements.txt

# Inicia a app em segundo plano na porta 80
nohup python3 app.py > /home/ubuntu/app.log 2>&1 &