# What is Git?


Git is a distributed version control system, helping to track changes in files.

Git's objectives are to achieve speed, data integrity, and support for distributed, non-linear workflows, as in some
companies, there can be thousands of parallel branches running on different systems at the same time.
    
Git thinks of data as a series of snapshots of a miniature filesystem. This means that
with each committed save of a file, Git takes a "snapshot", or a reference, to that 
what that particular file looks like at that moment.
This generates efficiencies by not redundantly saving unchanged files again, and uses
an identical link to the already stored file. 

![](C:\Users\Andre\Pictures\Git_snapshot.png)

## Git States

Git has three main states. These states are:

1. Modified: Git is aware that a file has been changed, but this change has not been stored in git yet.
2. Staged: The file has been "added" to the stage, its current version has been tagged and is ready to be stored so that it can be used in the next snapshot.
3. Committed: This data has successfully been saved by Git, and the affected files will be able to be used as snapshots when other files are updated.

These can be accomplished using the following commands:

1. git add <file_name> / git add . (to add all changed files)
2. git commit -m "<your_message_here"

In between these commands, make sure to use generous amounts of "git status" as to check the current status of files affected, and to make sure all files that need to be are added, and committed.

The *git log* command can be used to log the previous commits to see what each of them added (assuming adequate and in-depth messages have been attached to them)

![](C:\Users\Andre\Pictures\git_staging.png)