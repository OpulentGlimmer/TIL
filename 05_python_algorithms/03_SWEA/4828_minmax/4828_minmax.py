import sys
sys.stdin = open('4828_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
    # max() / min() 안 쓰고
    # sort => [0] / [-1]

    numbers.sort()

    max_value = numbers[-1]
    min_value = numbers[0]

    # [477162, 658880, 751280, 927930, 297191]

    ans = max_value - min_value  # ans : 630739


    print(f'#{tc} {ans}')
