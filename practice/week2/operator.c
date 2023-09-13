#include <stdio.h>

int main()
{
	int x = +4;
	int y = -2;

	printf("x + (-y) = %d\n", x + (-y)); // 부호를 이용한 int 형태의 수식을 print문 안에서 한번에 받아서 출력
	printf("-x + (+y) = %d\n", -x + (+y));

	return 0;

}