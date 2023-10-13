#!/bin/bash

# update
sudo apt update -y

#upgrade
sudo apt upgrade -y

#install, restart, enable
sudo apt install nginx -y
sudo systemctl restart nginx
sudo systemctl enable nginx

#install tree, git
sudo apt install tree -y
sudo apt install git-all

#install correct Nodejs version
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

#install NodeJs, pm2
sudo apt install nodejs -y
sudo npm install pm2 -g

#Create file to store app
mkdir nodejs_app

#Move into correct folder
cd nodejs_app

#clone from repo
git clone https://github.com/JK-A2023/Sparta_app.git

#Move into correct folder
cd Sparta_app/app

#Install dependencies
npm install -y

#Run file
pm2 start app.js