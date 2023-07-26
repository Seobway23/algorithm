"""
- 1, 2 칸씩 오를 수 있음
- dp [i] => i번째 계단 최댓값
- 1 칸이 3번씩 나오면 안됨  0 -> 1 칸 오를 떄 flag ++

case1 : end - 2 
case2 : end - 1
case3 : flag & end -2 
"""

# input
T = int(input())
lst = [0] #  시작점 index 0
for _ in range(T):
    N = int(input())
    lst.append(N)
# idx 간 deepcopy 를 위함
dp = [[0, 0] for _ in range(T + 1)]

# dp[i][j]  i =>  계단 위치 / j => flag
dp[1][0] = lst[1]
# dp[1][1] = 0

# flag 가 2라면 무조건 2칸 점프 해야 함

for idx in range(2, T + 1):
    one = dp[idx-1][0] + lst[idx]
    two = dp[idx-2][0] + lst[idx]

    # CASE 1
    if one > two and dp[idx-1][1] < 1:
        dp[idx][0] = one
        dp[idx][1] = dp[idx-1][1] + 1

    # CASE 2
    elif two > one:
        dp[idx][0] = two
        dp[idx][1] = 0

    # CASE 3
    else:
        dp[idx][0] = two
        dp[idx][1] = 0
print(dp[T][0])