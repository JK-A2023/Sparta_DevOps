# PM2

## PM2 is a process manager for Node.js applications.

### What is it?

- Advanced process manager for NodeJS
- Allows you to start, control, or stop your node processes.
- Allows real-time monitoring of Node app.
- Allos for auto-restarting if a process crashes.
- Load Balances, distributing incoming traffic across multiple instances to improve performance and reliability.


### What are some useful commands?

- `pm2 start app.js`
- `pm2 stop app.js`
- `pm2 restart app.js`
  - `pm2 restart all`
- `pm2 reset <app_name>`
  - Reset the process metrics for a specific application.
- `--watch`
  - This flag will tell the PM2 manager to restart the NodeJS process whenever it detects a file change.
- `pm2 list`
  - List all managed processes.
- `pm2 logs` 
  - Displays all logs for managed proceses.
  - `pm2 logs app.js`
    - displays logs for a specific application.
- `pm2 monit` 
  - Opens the real-time monitoring dashboard in your terminal
- `pm2 save`
  - Save the currently running processes to automatically restart them on system reboot. 
- `pm2 status`
  - View the status of all managed processes. It displays process names, IDs, and status (online, stopped, errored.)
- `pm2 info <app_name>`
  - Information on specific application, incl resource usage, environment variables, and file paths.
- `--max-memory-restart <enter_value_here>`
  - You can use this option to limit the amount of memory a node app can use. It could be useful when you have a limited amount of RAM at your disposal, and you want to distribute the memory evenly amongst your applications.
- `pm2 link <secret_key> <public_key>`
  - Link a remote PM2 instance using a secret key and public key for centralized monitoring and management.

