# exposed

Oh no I left the address to `system` lying around. RIP ASLR, huh. 

### hint

libc is dynamically linked which means the ENTIRE library is just sitting around somewhere in your address space. Good thing ASLR means you don't know where it is, right? 