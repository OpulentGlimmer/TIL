# C언어 연산자

```
# include <stdio.h> /* 헤더파일 선언 */

int main(void) /* main 함수의 시작 */
{
	1 + 2; /* 1과 2의 합을 명령함 */

	int num; /* num이라는 이름의 변수선언 */

	/* int : 정수의 저장이 가능한 메모리 공간을 할당 */
	/* num : 그 메모리의 공간의 이름을 num이라고 한다. */

	num = 10; /* 변수 num에 10 저장 */

	/* C언어에서는 = 기호는 값의 대입을 말한다.*/
	/* = 기호는 대입연산자라고 하며, 대입 연산자의 오른편에 오는 값을 왼편에 오는 변수에 저장하는 형태로 사용이 된다. */

	printf("%d", num);

	return 0; /* 함수를 호출한 영역으로 값을 전달(반환), 현재 실행중인 함수의 종료, 0의 반환 */
} /* main 함수의 끝 */
```

```
# include <stdio.h>

int main(void)

{
	int num1, num2; /* 정수형 변수 num1, num2의 선언 */
	int num3 = 30, num4 = 40; /* 정수형 변수 num3, num4의 선언 및 초기화 */
	double num5 = 3.14; /* 실수형 변수 num5의 선언 및 초기화 */
	
	num1 = 10; /* 변수 num1의 초기화 */
   	num2 = 20; /* 변수 num2의 초기화 */

	printf("num1 : %d \nnum2 : %d \n", num1, num2); /* num1, num2 값 출력 */
	printf("num3 : %d \nnum4 : %d \n", num3, num4); /* num3, num4 값 출력 */
	printf("num5 : %f \n", num5); /*num5 값 출력 */

	return 0; /* 함수를 호출한 영역으로 값을 전달(반환), 현재 실행중인 함수의 종료, 0의 반환 */

} /*main 함수의 종료 */
```