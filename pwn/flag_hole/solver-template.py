from pwn import *
import subprocess

CHAL = "flag-hole"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

# automate inputs as necessary here

p.interactive()
