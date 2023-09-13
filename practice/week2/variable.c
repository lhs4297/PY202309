#include <stdio.h>

int main() // main 함수 선언 () 안에는 void임
{
	int x;
	int y;
	int z; // x, y, z 를 int형태로 받겠다

	x = 1; //변수 지정값 선언
	y = 2;

	z = x + y; // 변수 수식 지정

	printf("%d", z); // 프린트

	return 0; // 호출

}