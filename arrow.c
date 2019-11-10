#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student {
	char name[80];
	int age;
	float percentage;
};

struct student* foo = NULL;

int main()
{
	foo = (struct student*)
		malloc(sizeof(struct student));
	
	foo->age = 19;
	strcpy(foo->name, "FOO");
	foo->percentage = 85.5;
	
	printf("%s\n%d\n%f\n", foo->name,foo->age,foo->percentage);
	
	return 0;
}