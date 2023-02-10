import sys
sys.stdin=open("1979.txt","r")
from pprint import pprint

T=int(input())
for test_case in range(1,T+1):
    N, K= map(int,input().split())
    arr=[[0]*(N+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(N) ]+ [[0]*(N+2)]
    #pprint(arr)
    cnt=0

    for j in range(N+2):
        for i in range(N-K+1):
            #가로
            lst = []
            for k in range(K+2):
                lst.append(arr[j][i+k])

                if lst == [0] + [1] * K + [0]:
                    cnt+=1

            #세로
            lst = []
            for k in range(K + 2):
                lst.append(arr[i + k][j])

                if lst == [0] + [1] * K + [0]:
                    cnt+=1


    print(f"#{test_case} {cnt}")