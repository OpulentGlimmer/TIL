import sys
sys.stdin = open('2001_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 파리가 붙여있는 곳, M : 파리채 크기(M * M)
    matrix = [list(map(int, input().split())) for i in range(N)]

    kills = []   # 파리를 잡은 갯수를 세기 위해서 만듦
    # 파리채를 내려칠 곳 탐색
    for row_one in range(N-M+1):  # row_one : 0, range(0, N)
        for col_one in range(N-M+1):  # col_one : 0, range(0, N)

            fly = 0
            # 해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색
            # row_one * col_one 크기인 파리채로 가장 많이 있는 파리(숫자)를 찾는다.
            for row_two in range(M):  # row_two : 0, row_last_two : range(0, N)
                for col_two in range(M):  # col_two : 0, col_last_two : range(0, N)
                    fly += matrix[row_one+row_two][col_one+col_two]
                    # row_one과 col_one에서 가장 큰 수 체크한 곳에서 row_two * col_two 크기인
                    # 파리채로 fly변수에 잡을 수 있는 파리의 합을 구한다.
            kills.append(fly)
	# 배열 범위 안에서 가능한 경우의 수 중에서 가장 많은 파리를 잡을 때의 수 출력
    print(f'#{tc} {max(kills)}')