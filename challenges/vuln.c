
#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
void win()
{
	printf("Your exploit1 is successfull..\n");
	system("/bin/sh");
	return;
}
void get_input()
{
	char fmt[10];
	gets(fmt);
	// printf(fmt);
}
int main(int argc, char* argv[])
{
	char buff[12];
	printf("%p\n", &main);
	get_input();
	// win();
	// system("/bin/ls");
	// gets(buff);
	// printf("Welcome %s\n", buff);
}
