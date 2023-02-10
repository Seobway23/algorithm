import sys
from pprint import pprint
sys.stdin=open("0210input.txt","r")


T=int(input())

for test_case in range(1,T+1):
    N, M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ans=0

    for i in range(N-M+1):
        for j in range(N-M+1):
            mx = 0
            #print(i,j)
            for y in range(M):
                for x in range(M):
                    dy=i + x
                    dx=j + y
                    mx+=arr[i+x][j+y]


            if mx>ans:
                ans=mx


    print(f"#{test_case} {ans}")