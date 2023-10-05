#!/bin/bash

# update & upgrade
sudo apt update -y
sudo apt upgrade -y

#install nginx & sed
sudo apt install nginx -y
sudo apt install sed -y

#change the nginx file:
sudo sed -i "s/try_files \$uri \$uri\/ =404;/proxy_pass http:\/\/localhost:3000\/;/" /etc/nginx/sites-available/default

#restart and enable nginx 
sudo system resart nginx
sudo system enable nginx

#finds the correct version of node
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

#installs the cached version of node
sudo apt install nodejs -y

# install pm2
sudo npm install pm2 -g

#clone the repo
git clone https://github.com/JK-A2023/Sparta_app.git

#move into it
cd Sparta_app/app

#update npm
npm install

#start the app
pm2 start app.js

#final restart
sudo systemctl resart nginx