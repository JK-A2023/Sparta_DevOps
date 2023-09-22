![](C:\Users\Andre\Pictures\git_vs_VCS.png)

# Git Init

Set up Git within a local system using the command ```git init```. This sets up the necessary structure and files so that Git can begin tracking any changes and version of files within that directory.
After setting up a Git repository locally, you will need to add be included within this repository.

# Git Add

```git add``` is Git command that is used to then stage changes within a file. This is the act of telling Git which changes you want to later commit.
You can use ```git add``` to specify individual files: ```git add <file-name>```. 
Stage directory files with ```git add <path/to/directory>```. 
Alternatively, the ```git add .``` command stages all changes made in all files.

# Git Commit

The ```git commit``` command is used to "save" changes in the file(s) you have staged using git add.
Useful commit messages should be added in using the ```git commit -m "<commit-message-here``` to document changes made in this commit. These messages should be along the lines of why you made the change, what problem it solves, or what new feature it added. Well documented commit messages make it easier for yourself and others to understand the history of the project, and makes it easier to contribute.

# Git Remote Add Origin

This is a useful command that is often an early step in setting up a new Git repository, as well as connecting your local repository to a remote one, such as a GitHub repository.
The ```git remote add origin <https://github.com/yourusername/your-repo.git>``` command indicates that you want to add a new remote repository to your local repository's configuration, with origin being name a chosen name you wish to give to the remote repository.


# Git Push

```git push``` is a command used to send your changes from the current local Git repository to the now set remote repository. When working on larger projects, you may have to specify which branch you are pushing to: ```git push <remote-name> <branch-name>```, an example being ```git push origin tdd_branch```.
