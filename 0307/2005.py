import sys
sys.stdin = open("input_2005.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f"#{tc}")
    for i in range(N):
        for j in range(i+1):
            if i == 0 or i == j: # 첫번째, 대각선은 1로 채움
                arr[i][j] = 1
            else: # 아니라면 윗줄에 자신의 왼쪽과 오른쪽 숫자를 더한다
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            if arr[i][j]:
                print(arr[i][j], end=" ")
        print()



