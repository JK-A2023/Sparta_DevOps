#!/bin/bash

export DB_HOST=mongodb://<ip_here>:27017/posts

# move into the app directory
cd home/ubuntu/Sparta_app/app

#install npm dependencies
npm install

# kill any previous background processes
pm2 kill

#start the app in background with pm2
pm2 start app.js