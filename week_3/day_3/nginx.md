# NGINX Setup Through EC2

### Prerequisites

Ensure you are connected to the correct region. In this instance, we will be using `eu-west-2`, "Ireland", marked in red:

![img.png](linux_images/region_location.png)

## Setting up EC2

1. Navigate to the Console Home on the Amazon web services page.
   1. This can searched in the Search Bar or from recently visited:

![img.png](linux_images/EC2_location_on_page.png)

2. Select the Launch Instance Button:

![img.png](linux_images/launch_instance_location.png)

3. Create a viable name.
    1. Note: this name must be globally unique.
    2. Follow the provided naming convention.

![img.png](linx_images/../linux_images/nginx_naming.png)

4. Select the required AMI.
   1. In this example, we will be browsing for alternative AMIs.
   2. Then using the Community AMI's.
   3. Following this, we then search for 18.04 LTS 1e9. This is enough input to filter down to the AMI we are searching for.

![img.png](linux_images/browse_more_amis.png)

![img.png](linux_images/community_amis_location.png)

![img.png](linux_images/ubuntu_version.png)

![img.png](linux_images/ubuntu_select.png)

5. Select Instance type.
   1. For our purposes, we do not need much computational power, and so we will use the `t2.micro`

![img.png](linux_images/ec2_instance_type_selected.png)

6. Enter your given key pair.
   1. Later, you will need access to a .pem file that acts as the private side of this key.
   2. In this instance, we are using the rsa key tech254.

![img.png](linux_images/key_pair_location.png)

7. Network settings:
   1. Leave all settings as default until you reach Security group name.
   2. Choose a unique and descriptive name here.
   3. Security group lets us assign rules to a group we will make.

![img.png](linux_images/network_settings_edit_button.png)

![img.png](linux_images/security_group_name_location.png)

### Ports

- The URL is a pointer to where you want to go.
- URL acts as a human readable IP address.
- An IP address is like a house number.

Some standard ports:

- http = port 80
- https = port 8080
- ssh = port 22

8. Add in the following Security Group Rules:
   1. `HTTP` - Leave everything as default with the exception of the source, changing it to 0.0.0.0/0 for global reach.
   2. `HTTPS` - Leave everything as default with the exception of the source, changing it to 0.0.0.0/0 for global reach.

![img.png](linux_images/security_group_rule_button.png)

![img.png](linux_images/security_group_http_type.png)

![img.png](linux_images/security_group_https_name.png)

9. Storage Configuration:
   1.  Leave as default.

![img.png](linux_images/configure_storage_section.png)

10. Summary:
    1.  Check over summary to ensure all options selected match with requirements.
    2.  Press the marked Launch Instance button.

![img.png](linux_images/summary_section.png)

## Connecting to EC2

1. Use the newly generated link to go to your EC2 page:

![img.png](linux_images/successful_ec2_init.png)

2. Click on the Connect button:

![img.png](linux_images/ec2_connect_button.png)

3. Navigate to the SSH client tab:

![img.png](linux_images/ssh_client_tab.png)

4. Locate your previously hidden .pem private key, possibly located within your hidden .ssh folder.
   1. See terminal input:
   2. Make sure the key is readable:

![img.png](linux_images/chmod_command.png)

![img.png](linux_images/chmod_terminal.png)

5. Use the provided command to connect to your ubuntu user profile on the EC2.
   1. For our use, the command is:
   2. `ssh -i "tech254.pem" ubuntu@ec2-54-155-164-225.eu-west-1.compute.amazonaws.com`
   3. `-i` identity by using:
   4. `tech254.pem` is the identity
   5. `ubunutu` this is the user we are logging in as on the server.
   6. `@ec2-54-155-164-225.eu-west-1.compute.amazonaws.com` is where we want to go.

![img.png](linux_images/ssh_connect_command_1.png)

![img.png](linux_images/ssh_terminal_input.png)

6. In the terminal, say `yes` to approve the authenticity.

![img.png](linux_images/say_yes_to_ssh.png)

7. Note the change in the terminal output and name.
   1. You are now logged in to your EC2.

![img.png](linux_images/ec2_instance_first_log_in.png)

8. Make sure your machine is up to date.
   1. `sudo apt update`
   2. The above command searches and files the available updates for your machine, but does not install and deploy them.
   3. `sudo apt upgrade -y`
   4. The above command deploys the changes from the previously cached downloads.
   5. The `-y` flag agrees to all changes automatically.
   6. Do this step before launching important applications, as later updates and upgrades may cause issues.

![img.png](linux_images/sudo_apt_update.png)

![img.png](linux_images/sudo_apt_upgrade.png)

## Setting Up NGINX

1. Install NGINX on your EC2 using the following:
   1. `sudo apt install nginx -y`

![img.png](linux_images/install_nginx.png)

2.  To verify the application has installed, start it, and then check its status:
    1.  `sudo systemctl start nginx`
    2.  `sudo systemctl status nginx`
    3.  press `q` to leave the status.

![img.png](linux_images/start_nginx.png)
![img.png](linux_images/status_nginx.png)

3. NGINX is now running.
4. Navigate back to your EC2 instance page.
   1. Find the Public IPv4 address.
   2. Copy the address.
   3. Paste this into your browser URL bar.

![img.png](linux_images/ipv4_ip.png)

![img.png](linux_images/you_did_it.png)