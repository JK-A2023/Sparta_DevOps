# Linux Commands

1. `uname`
   1. Tells you about the operating system and the rest of the system.
   2. `-a` long version
   3. `-p` processer
2. `whoami`
   1. tells you the current user.
3. `cat`
   1. print out the contents of a file
   2. `cat /etc/shells` - print the contents of the shell types
4. `history`
   1. prints the history of the commands you input.
   2. `-c` clears the history
5. `clear`
   1. clears the screen.
6. `ls`
   1. Lists the file and folders
   2. `-a` lists all hidden files
   3. `..` lists the files in directory above.
   4. `-l` lists in a bulletpoint list with info on all files.
7. `curl`
   1. Transfers data.
   2. e.g.: `curl https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg --output cat.jpg`
   3. `--output <filename.type>`
8. `file <filename>`
   1. gives information about a file.
   2. e.g.: `file cat.jpg`
9. `mv`
   1.  Two uses:
       1.  can move files
       2.  can rename files
10. `cp`
    1.  copies a file.
    2.  e.g.: cp cat.txt cat.jpg
11. `rm`
    1.  removes file / folder.
    2.  `-f` removes folders.
    3.  `-r` removes recursively inside folders.
12. `mkdir`
    1.  make a directory
    2.  `mkdir my_directory`
13. `touch`
    1.  makes a blank file.
14. `nano`
    1.  opens up text editor
15. `head`
    1.  brings back the specified amount of lines from the top of the file.
    2.  `head -3 <filename.type>` prints the top 3 lines from a file.
16. `tail`
    1.  brings back the specified amount of lines from the bottom of the file.
    2.  `tail -3 <filename.type>` prints the bottom 3 lines from a file.
17. `nl`
    1.  prints out the number lines of a file.
    2.  `nl chicken_joke.txt`:
        1.  1  why did the chicken cross the road?
        2.  2  To meet the colonel.
18. `|` "pipe" allows to add additional commands:
    1.  `cat chicken_joke.txt | grep chicken`
        1. prints "why did the chicken cross the road?" with the word chicken  highlighted, and only the line that contains it.
 19. `grep`
     1.  order is `grep <word looking for> <file>`
 20. `apt`
     1.  internal linux process to go and get a particular package, and manipulate those packages.
 21. `sudo`
     1.  super user permissions for a particular command
 22. `tree`
     1.  shows all directories
     2.  `-a ` for all
 23. `sudo su`
     1.  switch user / substitute user: changes user into super user, typically root user.
     2.  enter `exit` to go back to regular user
 24. `exit`
     1.  breaks connection to EC2 instance.


# Bash


Born Again Shell - A way of communicating with Linux
Goes off of the content of the file, not necessarily the extension.
