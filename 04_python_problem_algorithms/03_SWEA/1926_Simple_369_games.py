T = int(input())  # 숫자를 입력받기 위해 int()함수를 쓴다.

for ints in range(1, T+1):  # 1 ~ 100

    ints = str(ints)  # count를 하기 위해서 숫자를 문자열로 변환
    clap = ints.count('3') + ints.count('6') + ints.count('9')  # '3'이나 '6'이나 '9'가 나오면 clap에 count
    if clap == 0:  # clap에  count한 갯수가 0이면
        print(ints, end=' ')  # 숫자를 출력
    else:  # clap에  count한 갯수가 0이 아니라면
        print('-' * clap, end=' ')  # clap 갯수만큼 '-'를 출력