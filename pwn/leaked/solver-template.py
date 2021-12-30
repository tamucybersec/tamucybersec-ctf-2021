from pwn import *

CHAL = "leaked"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

# automate inputs as necessary here

p.interactive()
