from pwn import *

CHAL = "cave-2"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

# automate inputs as necessary here

p.interactive()
