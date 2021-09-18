#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void main() {
	setvbuf(stdout, 0, 2, 0);
    FILE* flag_file = fopen("flag.txt", "r");
    char* FLAG = malloc(64);
    if(flag_file == NULL) {
        strcpy(FLAG,"Flag file is missing, run that exploit again on the server!");
    } else {
        fgets(FLAG, 64, flag_file);
    }
	char buf[128];
	printf("You're in a cave and can hear echos. Call out?\n");
	fgets(buf, 128, stdin);
	printf(buf);
}
