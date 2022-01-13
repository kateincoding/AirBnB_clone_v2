#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu /data/web_static/releases/test
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
configure="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo useradd ubuntu
sudo chown -hR ubuntu:ubuntu /data/ 
sudo sed -i "49i\ $configure" /etc/nginx/sites-available/default
sudo service nginx restart
sudo service nginx reload
