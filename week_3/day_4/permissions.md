# Linux Permissions

## Three Different Sets of Users

1. Owner
2. User
3. Anyone else

## Three Different Sets of Permissions

4. Read Access
   1. Permits the user to read the file
5. Write Access
   1. Permits the user to write to the file
6. Execute Access
   1. Permits the user to execute the file


### To change permissions:

`chmod <permissions> <file / folder>`

User permission:
`chmod u+x chicken_joke.txt`
    - Gives the user permission to execute this file.

`chmod u+xw chicken_joke.txt`
    - Gives the user permission to execute and write to this file.

`chmod u-x chicken_joke.txt` 
    - Removes user permission to execute file.

`chmod u-xw chicken_joke.txt` 
    - Removes user permission to execute and write to this file.

OR NUMERIC VERSION:

`sudo chmod 777 chicken_joke.txt`

Gives all access to everyone.
https://chmod-calculator.com/

Public:
    `sudo chmod +x chicken_joke.txt`



