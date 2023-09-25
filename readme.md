## What is SSH? What is it used for? ##
SSH is a network protocol that allows users to securely access and manage remote systems and devices over a potentially insecure network, such as the internet.

#### Common uses of SSH include: ####
- Remote system administration: SSH allows system administrators to remotely log in to servers and manage them as if they were physically present.
- Secure file transfers: Tools like SFTP (SSH File Transfer Protocol) and SCP (Secure Copy) use SSH to transfer files securely between systems.
- Tunneling: SSH can create secure tunnels for forwarding network traffic, which can be used for tasks like accessing remote databases securely.
## How does SSH work? What are Private and Public keys? ##

SSH uses a pair of cryptographic keys for authentication and encryption: a private key and a public key.

The private key is kept secret and stored securely on the client-side (your computer). It should never be shared with anyone.
The public key is derived from the private key and can be shared freely with others. It's placed on the server or device you want to access securely.

When you connect to a remote server, the server checks if your public key is in its authorized keys file. If it finds a match, it will challenge you to prove you have the corresponding private key.
You use your private key to respond to the challenge, and if successful, you're granted access without needing a password.

## Why use SSH? How does it increase security? ##
SSH is essential for secure remote access because it offers several key security benefits:
- Encryption: All data transmitted over an SSH connection is encrypted, making it difficult for eavesdroppers to intercept or understand the content.
- Authentication: SSH uses cryptographic key pairs for authentication, making it resistant to common password-based attacks like brute force.
- Strong identity verification: By using key pairs, SSH ensures strong verification of the user's identity without transmitting sensitive credentials over the network.
- Protection against man-in-the-middle attacks: SSH includes mechanisms to detect and prevent attackers from intercepting or altering communication between the client. 

## How can you create an SSH key pair? ##
You can create an SSH key pair using the ssh-keygen command on your local computer (client):
- Open a terminal or command prompt.

- Use the following command to generate an SSH key pair (usually RSA or Ed25519):
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
- Replace "your_email@example.com" with your email address.

Follow the prompts to choose a location for the key files and optionally set a passphrase for added security.

After creating the key pair, you will have two files: your private key (usually id_rsa) and your public key (usually id_rsa.pub). 

You can copy the public key to the remote servers or devices where you want to use SSH for secure access. Make sure to keep your private key secure and never share it.







Note that: github uses a password while SSH uses a key. SSH uses a key and lock system. 
.ssh folder 
. mkdir ssh()
ssh-keygen -t rsa -b 4096 -C "BS@spartaglobal.com"
enter file in which to save the key: github_test
-t (type of encryption that needs to be done)



pid1200: process id used

$ eval 'ssh-agent'
$ ssh-add ~/.ssh/github_test1
$ ssh -T git@github.com
$ ssh-add ~/.ssh/github_test1
$ git remote set-url origin link. git
$ git add .
$ git commit -m "Small change for testing"

$ git push -u origin main
$ git remote -v
$ ssh -vT git@github.com
