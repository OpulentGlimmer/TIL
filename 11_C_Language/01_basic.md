# C언어의 기본

## include <stdio.h>
- 헤더파일 선언

## int main(void)
- main 함수의 선언

```

# include <stdio.h>

int main(void)

{
	printf("Hello world \n"); 
    
    /* 문자열의 출력 */

	printf("%d\n", 12345); 
    
    /* 서식문자 %d : 정수의 출력*/

	printf("%d %d\n", 10, 20); 
    
    /* 서식문자 %d : 정수의 출력 */

	printf("My age : %d \n", 30); 
    
    /* 서식문자 %d : 정수의 출력 */

	printf("%d is my point \n", 1000); 
    
    /* 서식문자 %d : 정수의 출력 */

	printf("Good \nmorning \neverybody \n"); 
    
    /* 문자열의 출력 */

	printf("제 이름은 박은영입니다. \n제 나이는 % d입니다. \n제가 사는 곳의 번지수는 %d - %d 입니다. \n", 30, 123, 456);

	printf("%d X %d = %d \n%d X %d = %d \n", 2, 5, 10, 7, 8, 56);

	return 0; 
    
    /* 함수를 호출한 영역으로 값을 전달(전환), 현재 실행중인 함수의 종료, 0의 반환 */
}
```