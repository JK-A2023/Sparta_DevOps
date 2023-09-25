# SSH

## What is SSH? 

Secure Shell is a network communication protocol for operating network services securely over potentially unsecured networks.

## What is it used for?

Its most notable applications are remote login and command-line execution.

## How does SSH work?

Operates as a layered protocol suite comprising three principal hierarchical components:
1. Transport Layer:
   1. Server Authentication.
   2. Confidentiality.
   3. Integrity.
2. User Authentication:
   1. Validates the user to the server.
3. Connection Protocol
    1. Multiplexes the encrypted tunnel into multiple logical communication channels.

Here is a simplified overview of how SSH works:

1. Establishing a connection:
2. Server Identification
3. Key Exchange
4. User Authentication
5. Encryption
6. Session Establishment.
7. User Interaction:
8. Data Exchange:
9. Session Termination.

## What are Private and Public keys?

### Public Key

- Cryptographic key that is intended to be shared openly with anyone, hence the name "public".
- When someone wants to send you an encrypted message or datas, they use your public key to encrypt it. Once encrypted with your public key, only your corresponding private key can decrypt it.
- It is computationally infeasible to derive the private key from the public key.

### Private Key

- Closely guarded secret key that must never be shared with anyone. It is used for decryption and digital signatures.
- When you receive data that has been encrypted with your public key, you use your private key to decrypt it. This ensures only you can access the original content.
- If someone gains access to your private key, they can decrypt your messages and impersonate you in digital signatures.

![](C:\Users\Andre\Pictures\encryption.png)

## How can you create an SSH key pair?

o create an SSH key pair, you can use the ssh-keygen utility, which is commonly available on Unix-based systems like Linux and macOS. Here are the steps to generate an SSH key pair:

Open a Terminal or Command Prompt:

To generate an SSH key pair, run the following command:

[//]: # (```git config --global url."git@github.com:".insteadOf "https://github.com/"```)

1. `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
2. `eval `ssh-agent``
3. `ssh-add ~/.ssh/<file-name>`
4. `ssh -T git@github.com`
5. `git remote set-url origin git@github.com:<your-git/here>.git`

Then just the regular

`git add .`
`git commit -m "<message>`
`git push -u origin main`



The -t option specifies the type of key to create, which is RSA in this case.

The -b option specifies the key's length, which is 2048 bits (a common choice for security).

The -C comment, so can put what you want there, but mostly for email address.

You can accept the default location for storing the key pair, which is typically ~/.ssh/id_rsa for the private key and ~/.ssh/id_rsa.pub for the public key.

Enter a Secure Passphrase (Optional):

You'll be prompted to enter a passphrase for added security. This passphrase is used to encrypt your private key, so even if someone gains access to it, they won't be able to use it without the passphrase.
You can choose to leave the passphrase empty for convenience, but it's highly recommended to use one for added security.
Key Generation:

ssh-keygen will generate your SSH key pair. The process may take a moment, depending on your computer's processing power.
Key Location:

Once the keys are generated, they will be stored in your home directory under ~/.ssh/ by default.
Your public key will be in a file named id_rsa.pub, and your private key will be in a file named id_rsa.
You've now successfully created an SSH key pair. Your public key (id_rsa.pub) can be shared with remote servers or services to allow you to log in securely. Keep your private key (id_rsa) safe and never share it with anyone.

To use your SSH key pair to log into a remote server, you can typically copy the contents of your public key and add it to the ~/.ssh/authorized_keys file on the server. This allows you to authenticate without a password when connecting to that server.



Bonus: Can you push to one of out GitHub repos using an SSH key rather than HTTPS (login details)?