#include <stdio.h>
#include <stdlib.h>

struct Point {
	int x;
	int y;
};

//Constructor no allocation

void Point__init(struct Point* self, int x, int y) {
	self->x = x;
	self->y = y;
}

// Allocation and initialization
struct Point* Point__create(int x, int y) {
	struct Point *result = malloc(sizeof(*result));
	Point__init(result, x, y);
	return result;
}

//Destructor no deallocation
void Point__reset(struct Point* self) {
	
}

//Destructor w/ deallocation (deletes point)
void Point__destroy(struct Point* point) {
	if (point) {
		Point__reset(point);
		free(point);
	}
}

//getters

int Point__x(struct Point* self) {
	return self->x;
}

int Point__y(struct Point* self) {
	return self->y;
}

struct Point* midPoint(struct Point* a, struct Point* b) {
	struct Point *mid = malloc(sizeof(*mid));
	
	mid->x = (a->x + b->x) / 2;
	mid->y = (a->y + b->y) / 2;
	return mid;
}

float findSlope(struct Point* a, struct Point* b) {
	float result;
	//if (b->x - a->x == 0) would like to figure out a fix to undefined slope
	//	return ;
	result = (float)(b->y - a->y) / (float)(b->x - a->x);
	return result;
}

int main()
{
	struct Point* foo = Point__create(0, 0);
	struct Point* bar = Point__create(6,20);
	struct Point* mid = midPoint(foo, bar);
	printf("Midpoint is: (%d, %d)\n", Point__x(mid), Point__y(mid));
	printf("Slope is: %.3f\n", findSlope(foo, bar));
	return 0;
}