# Linux Permissions

## Three Different Sets of Users

1. Owner (User)
   1. Owns the file or directory.
   2. Typically has the most control over it.
   3. Represented by the first three permission bits in the permission string.
2. Group
   1. Every file and firectory on Linux is associated with a "group"
   2. Group perms apply to every member associated with this group.
   3. Represented second set of three permission bits
3. Others
   1. Neither owner nor members of group associated with a file / directory.
   2. No special ownership / affiliation.
   3. Represented by the third set of permission bits

## Three Different Sets of Permissions

4. Read Access
   1. Permits the user to read the file
5. Write Access
   1. Permits the user to write to the file
6. Execute Access
   1. Permits the user to execute the file


### To change permissions:

```chmod <permissions> <file / folder>```

User permission:

```chmod u+x chicken_joke.txt```
- Gives the user permission to execute this file.

`chmod u+xw chicken_joke.txt`
- Gives the user permission to execute and write to this file.

`chmod u-x chicken_joke.txt` 
- Removes user permission to execute file.

`chmod u-xw chicken_joke.txt` 
- Removes user permission to execute and write to this file.

Group permission:

```chmod g+rwx chicken_joke.txt```

Others permission:

```chmod o+rwx chicken_joke.txt```

### Numeric Permissions:

`sudo chmod 777 chicken_joke.txt`

- Gives all access to everyone.
- https://chmod-calculator.com/




