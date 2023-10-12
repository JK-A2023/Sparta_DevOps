# Create Launch Template


1. Give it appropriate, descriptive name.

![img.png](images/launch-template/image.png)

4. Use an AMI that is already provisioned.

![img.png](images/launch-template/image-1.png)

5. Standard selections:

![img.png](images/launch-template/image-2.png) 

6. Advanced Details:
   1. Use the user_data script to cd into the app, npm install, and start the app:

![img.png](images/launch-template/image-3.png)

7. Create.

# Begin Launch Template

1. Find the actions tab while on your Launch Template.

![img.png](images/launch-template/image-4.png)

2. Select the "Launch instance from template" button.

![img.png](images/launch-template/image-6.png)

3. As this is a template, it is already set up. The only changes now are to set the resource tags:
   1. Select Name.
   2. Give the value an appropriate name.

![img.png](images/launch-template/image-5.png)

4. Launch instance.

