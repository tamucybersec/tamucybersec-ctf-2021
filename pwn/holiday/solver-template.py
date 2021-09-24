from pwn import *

CHAL = "holiday"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

# automate inputs as necessary here

p.interactive()
