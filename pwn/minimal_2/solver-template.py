from pwn import *
import subprocess

CHAL = "minimal-2"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

# automate inputs as necessary here

p.interactive()
