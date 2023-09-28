#!/bin/bash

# update
sudo apt update -y

#upgrade
sudo apt upgrade -y

#install
sudo apt install nginx -y

#restart
sudo sysemctl restart nginx

#enable
sudo systemctl enable nginx

#install correct Nodejs version
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

#install NodeJs
sudo apt install nodejs -y

#install pm2
sudo npm install pm2 -g

#Create file to store app
mkdir nodejs_app

#Move into correct folder
cd nodejs_app

#clone from repo
git clone https://github.com/JK-A2023/Sparta_app.git

#Move into correct folder
cd Sparta_app

#Move into correct folder
cd app

#Install dependencies
npm install

#Run file
node app.js