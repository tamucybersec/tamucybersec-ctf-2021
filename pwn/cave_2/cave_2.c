#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
    system("/bin/sh");
}

void main() {
	setvbuf(stdout, 0, 2, 0);
	char buf[128];
	printf("You're in a cave and can hear some faint echos. Venture deeper?\n");
	fgets(buf, 128, stdin);
	printf(buf);
    exit(0);
}
