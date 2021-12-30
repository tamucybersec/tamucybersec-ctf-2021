#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* shell = "/bin/sh";

void vuln() {
	printf("oh no I dropped an address 0x%lx, would be a shame if someone were to pwn me with it :(\n", system);
	printf("Oh, well, nothing to do about it now. What's your name?\n");
	char name[32];
	gets(name);
}

void main() {
	setvbuf(stdout, 0, 2, 0);
	vuln();
}