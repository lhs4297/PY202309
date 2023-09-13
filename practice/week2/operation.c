#include <stdio.h>

int main()
{
	int x = 4;
	int y = 2;
	int z; // x, y 는 정수 지정값 및 z 는 지정값은 아니지만 정수로 받겠다

	z = x + y;
	printf("z = x + y = %d\n", z);
	z = x - y;
	printf("z = x - y = %d\n", z);
	z = x * y;
	printf("z = x * y = %d\n", z);
	z = x / y;
	printf("z = x / y = %d\n", z);
	// 연산과 즉시 프린트를 함
	// 리턴 생략 가능
}