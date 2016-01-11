#!/bin/bash
clear

echo "Update and install dependencies"
sudo apt-get update -y
sudo apt-get install -y python-pip git
sudo pip install web.py

sudo apt-get install authbind
sudo touch /etc/authbind/byport/80
sudo chown bitnami:bitnami /etc/authbind/byport/80
sudo chmod 755 /etc/authbind/byport/80
echo " "


echo "Run a script every minute to check if the processes needs respawned"
(crontab -l ; echo "* * * * * /home/bitnami/name-checker/autorestart.sh")| crontab -

