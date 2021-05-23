#!/bin/bash

sudo unshadow passwd.txt shadow.txt > unshadow-output.txt

if [ ! -e /usr/share/wordlists/rockyou.txt ]
then
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
fi

john unshadow-output.txt --wordlist=/usr/share/wordlists/rockyou.txt

john --show unshadow-output.txt
