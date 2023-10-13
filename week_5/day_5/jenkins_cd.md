# Jenkins CD

### Prerequisites:

1. Database EC2
2. App EC2

## Database EC2:

1. Ubuntu
2. SSH into VM using SSH command, utilizing `-y` to skip asking for permission step.
3. Run MongoDB script:
   1. update
   2. upgrade
   3. get MongoDB 3.2
   4. Add MongoDB repo to sources.list
   5. Update
   6. Install MongoDB 3.2 packages
   7. bindIP set to 0.0.0.0
   8. start, enable, and status of mongod.

## App EC2:

1. Ubuntu
2. SSH into VM using SSH command, utilizing `-y` to skip asking for permission step.
3. Run App script:
   1. update, upgrade
   2. install,restart, enable nginx
   3. get correct node version
   4. install node
   5. install pm2
   6. make folder for app
   7. cd into app
   8. git clone repo main branch
   9. cd into Sparta_app / app
   10. install npm dependencies
   11. start app with pm2

## Jenkins Job3:

This can deploy on AWS.

1. Create a third job
2. Uses SSH agent, using .pem file added.
3. Create Security Group that allows port 8080.