#include <stdio.h>

int main()
{
	int x = 4;
	int y = 2;
	int z; // x,y는 지정값이며 x, y, z 모두 int형태

	z = (x + y) * (x - y);
	printf("z = (x + y) * (x - y) = %d\n", z); // x, y로 이루어진 수식을 z로받고 그걸 프린트해라

	z = (x * y) + (x / y);
	printf("z = (x * y) + (x / y) = %d\n", z); // 동일

	z = x + y + 2004;
	printf("z = x + y + 2004 = %d\n", z); // x, y 그리고 정수형으로 이루어진 수식을 받아서 z를 프린트해라

	return 0;

}
