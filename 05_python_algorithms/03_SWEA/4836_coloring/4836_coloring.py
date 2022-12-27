import sys
sys.stdin = open('4836_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if matrix[row][col] == color:
                    continue
                matrix[row][col] += color

    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] >= 3:
                count += 1

    print(f'#{tc} {count}')