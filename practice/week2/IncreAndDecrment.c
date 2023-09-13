#include <stdio.h>

int main()
{
	int x = 1;

	printf("x=%d\n", x++);   // 후위 증가 연산자를 이용해서 x를 현재 값을 사용하고 그 후에 1 증가
	printf("x=%d\n", x++);
	printf("x=%d\n", ++x);   // 1만큼 증가하여 x값을 사용 
	printf("x=%d\n", x--);   // x를 현재값을 사용하고 1만큼 감소
	printf("x=%d\n", x--);
	printf("x=%d\n", --x);   // 1만큼 감소하고 x값을 사용

	return 0;

}
