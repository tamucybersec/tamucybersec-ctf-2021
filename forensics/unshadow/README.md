# Unshadow

## Description

A lazy administrator gave permissions to a new hire to change his password. He inadvertently gave the new employee permission to read /etc/passwd and /etc/shadow files and the new employee leaked those files. Can you figure out the kali user's password?

<<<<<<< HEAD
Hint: rockyou.txt contains a lot of passwords and is often a good place to start in CTFs.

Note: The flag is an alphanumeric string.
=======
Note: the flag is an alphanumeric string
>>>>>>> 7452ab01b3b6a9d96d6a72d1792cf6a168abfa16

## Solution

flag: `monkey123`

unshadow can be used to combine passwd and shadow files in a format for john to parse through. john can take files created by unshadow and a wordlist to find the password of a user as long as the wordlist contains the user's password.

```bash
#!/bin/bash

sudo unshadow passwd.txt shadow.txt > unshadow-output.txt

if [ ! -e /usr/share/wordlists/rockyou.txt ]
then
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
fi

john unshadow-output.txt --wordlist=/usr/share/wordlists/rockyou.txt

john --show unshadow-output.txt
```

```bash
❯ ./answer.sh
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
No password hashes left to crack (see FAQ)
kali:monkey123:1000:1000:Kali,,,:/home/kali:/usr/bin/zsh

1 password hash cracked, 0 left
```
