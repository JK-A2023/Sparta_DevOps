#!/bin/bash

# update
sudo apt update -y

#upgrade
sudo apt upgrade -y

#get
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -

#echo
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

#update
sudo apt update

#install
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20

# following this, sudo nano into /etc/mongod.conf
#change the ip to 0.0.0.0