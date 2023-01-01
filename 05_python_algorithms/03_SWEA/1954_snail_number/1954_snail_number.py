# 1954_input.txt 파일에 있는 것
# 2 : #1,  #2를 의미
# 3 : N
# 4 : N

import sys
sys.stdin = open('1954_input.txt')

T = int(input())  # 입력한 숫자 2을 T 변수에 할당

for tc in range(1, T+1):  # T = 2(#1, #2만들기 위해 필요)
    N = int(input())  # 입력한 숫자 3을 N 변수에 할당
    snail = [[0] * N for i in range(1, N+1)]  # n = 3이면 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    length = N  # length 변수에 N = 3을 할당
    step = "right"  # step 변수에 "right"를 할당
    number = 1  # number 변수에 1을 할당, 가로와 세로에 있는 숫자
    row = 0  # row 변수에 0을 할당, 가로 0
    col = 0  # col 변수에 0을 할당, 세로 0
    while(length != 0):  # length가 0이 아닌 경우 반복해라!
        if step == "right":  # 오른쪽으로 움직일 때
            for _ in range(length):  # 0, 1, 2
                snail[row][col] = number  # 0.0 = 1, 0.1 = 2, 0.2 = 3
                number += 1  # 2, 3, 4
                col += 1  # 0.1, 0.2, 0.3
            length -= 1  # 3 - 1 = 2(아래로 2번만 가니까 설정)
            step = "down"  # 1.2을 만들기 위해 필요
            row += 1  # row = 0 + 1 = 1
            col -= 1  # col = 3 - 1 = 2, 0.3 -> 0.2
        elif step == "down":  # 아래로 움직일 때
            for _ in range(length):  # 2(아래로 2번 0 ,1)
                snail[row][col] = number  # 1.2 = 4, 2.2 = 5
                number += 1  # 5, 6
                row += 1  # row = 2, row = 3 # 2.3
            step = "left"  # 2.1을 만들기 위해 필요
            row -= 1  # row = 3 - 1 = 2
            col -= 1  # col = 2 - 1 = 1
        elif step == "left":  # 왼쪽으로 움직일 때
            for _ in range(length):  # 2(왼쪽으로 2번, 0, 1)
                snail[row][col] = number  # 2.1 = 6, 2.0 = 7
                number += 1  # 7, 8
                col -= 1  # col = 1 - 1 = 0 , col = 0 - 1 = -1
            length -= 1  # 1(위로 1번가기 위해 설정)
            step = "up"  # 1.0을 만들기 위해 필요
            row -= 1  # row = 2 - 1 = 1
            col += 1  # col = -1 + 1 = 0
        elif step == "up":  # 위로 움직일 때
            for _ in range(length):  # 1(위쪽으로 1번, 0)
                snail[row][col] = number  # 1.0 = 8
                number += 1  # 9
                row -= 1  # row = 1 - 1 = 0
            step = "right"  # 오른쪽으로 움직일 때
            row += 1  # row  = 0 + 1 = 1
            col += 1  # col = 0 + 1 = 1
    print(f'#{tc}')

    for i in range(N):  # N = 3  # 0, 1, 2
        print(*snail[i])  # * 붙이면 []가 삭제된다.

        # print(snail)하면
        # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

        # print(snail[0])하면
        # [1, 2, 3]
        # [1, 2, 3]
        # [1, 2, 3]

        # print(snail[1])하면
        # [8, 9, 4]
        # [8, 9, 4]
        # [8, 9, 4]

        # print(snail[2])하면
        # [7, 6, 5]
        # [7, 6, 5]
        # [7, 6, 5]

        # print(snail[i])하면
        # [1, 2, 3]
        # [8, 9, 4]
        # [7, 6, 5]

        
        