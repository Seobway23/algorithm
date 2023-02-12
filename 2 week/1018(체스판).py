'''
1018 체스판 다시 칠하기 문제
2023.02.12 20:39
arr[0][0]을 정한 후
[i],[j]열의 짝, 홀 수 열행에 따른 B , W를 판별하는 알고리즘을 만들었다.
하지만 10 13 과 같은, 그리고 오류가 많은 곳에서는 전혀 이상하게 알고리즘이 돌아갔다.
이유는 아직 찾지 못했지만, 내일 아침에 찾아보자!

아무래도 인덱싱 찾기에서 오류가 발생한 것 같다.
내일 아침에 컴퓨터로 디버깅을 해보자!

'''


import sys
from pprint import pprint
sys.stdin=open("input.txt","r")

def chess(board,st_B):
    black = "B"
    white = "w"
    for _ in range(2):
        cnt=0
        if st_B=="W":
            for i in range(N):
                if i%2==0:
                    for j in range(M):
                        if j%2==0 and board[i][j]==black: #아닌 경우를 카운트
                            A=board[i][j]
                            cnt+=1

                        if j%2==1 and board[i][j]==white:
                            B=board[i][j]
                            cnt+=1

                else:
                    for j in range(M):
                        if j % 2 == 0 and board[i][j] == white:  # 아닌 경우를 카운트
                            cnt += 1

                        if j % 2 == 1 and board[i][j] == black:
                            cnt += 1

            return cnt


        else:
            black, white = white, black
            st_B="W"

N, M=map(int,input().split())
board=[list(input()) for _ in range(N)]
st_B=board[0][0]
print(chess(board,st_B))
