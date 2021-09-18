#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* shell = "/bin/sh";

void vuln() {
	printf("Hah! You have no addresses now so i'm safe!  Pwn me if you can!\n");
	char buf[32];
	gets(buf);
}

void main() {
	setvbuf(stdout, 0, 2, 0);
	vuln();
}