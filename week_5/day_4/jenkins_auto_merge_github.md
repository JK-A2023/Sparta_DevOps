# How to set up automated merging using Git Publisher in Jenkins to merge branches to master in GitHub

## Job1

### CI Job creation

1. Set up a CI job as done previously:

![img.png](images/merge/image.png)
![img.png](images/merge/image-1.png)


### Source Code Management:

1. Use SSH url.
2. Branch specifier set yo `*/branch_here`. Make sure to NOT use main.
   1. We are trying to read from the secondary branch to merge into main.

![img.png](images/merge/image-2.png)

### Build Triggers:

1. Select GitHub hook.

![img.png](images/merge/image-3.png)

### Build Environment:

1. Provide Node

![img.png](images/merge/image-4.png)

### Build:

1. Execute Shel:
   1. `cd app`
   2. `npm install`
   3. `npm test`

![img.png](images/merge/image-5.png)

### Post-build Actions:

1. We now want to specify the next job to trigger if the git push is stable.

![img.png](images/merge/image-6.png)

2. Save this job.
3. If you haven't set up the name of your next job, there may be an error here.
4. Simply set up the next job, and the error will dissapear.

## Job2

### Job Setup:

1. Set up standard job settings:

![img.png](images/merge/image-7.png)

![img.png](images/merge/image-8.png)

### Source Code Management:

1. Remeber to use SSH url for repository.
2. Branch Specifier: `*/dev`
3. Additional Behaviours:
   1. Merge before build:
   2. Name of the repository will be the origin.
   3. The branch we are merging to is main.

![img.png](images/merge/image-9.png)

4. No Build Triggers.

### Build Environment:

1. SSH Agent:
   1. Use AWS .pem file.

![img.png](images/merge/image-10.png)

2. No Build steps.

### Post-build Actions:

1. Merge Results.
2. Add Branch
   1. Branch to push: `main`
   2. Target remote name: `origin` (or whatever you've called the remote)

![img.png](images/merge/image-11.png)