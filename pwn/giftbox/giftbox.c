#include <stdio.h>   
#include <stdlib.h> 

struct box {
	char* (* contents)();
};

struct box* boxes[3];

char* box1() {
	return "a pair of bright pink socks!";
}
char* box2() {
	return "a nice book!";
}
char* box3() {
	return "a hand-knit scarf!";
}
char* box4() {
	return "a smaller box!";
}
char* box5() {
	return "a potato!";
}

char* (* contents[5])() = { box1, box2, box3, box4, box5 };

void win() {
	system("/bin/bash");
}

void take_box() {
	puts("Which space would you like to place it in? ");
	int select;
	scanf("%d", &select);
	getchar();
	if(select >= 0 && select < 3) {
		struct box* b = malloc(sizeof(struct box));
		b->contents = contents[rand() % 5];
		boxes[select] = b;
	} else {
		puts("You can't fit a box in that space.");
	}

}

void open_box() {
	puts("Which box would you like to open? ");
	int select;
	scanf("%d", &select);
	getchar();
	if(select >= 0 && select < 3 && boxes[select] != NULL) {
		printf("You open the box and find... %s\n", boxes[select]->contents());
		free(boxes[select]);
	} else {
		puts("You can't fit a box in that space.");
	}
}

void leave_note() {
	puts("How long of a note would you like to leave? ");
	int select;
	scanf("%d", &select);
	getchar();
	char* note = malloc(select);
	fgets(note, select, stdin);
}

int menu() {

	puts("What would you like to do? ");
	puts("1. Take a box");
	puts("2. Open a box");
	puts("3. Write a thank you note");
	puts("4. Leave");

	int select;
	scanf("%d", &select);
	getchar();

	if(select == 1) {
		take_box();
	} else if (select == 2) {
		open_box();
	} else if (select == 3) {
		leave_note();
	} else if (select == 4) {
		exit(0);
	} else {
		puts("Invalid menu option. ");
	}
}

int main() {
	while(1) {
		menu();
	}
}