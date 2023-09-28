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
