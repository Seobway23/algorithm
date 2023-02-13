import sys
sys.stdin=open("input.txt", "r")


T=int(input())
for test_case in range(1,T+1):
    str2=input()
    cnt_1=0
    cnt_2=0
    for i in str2:
        if i=='(':
            cnt_1+=1

        else:
            cnt_2+=1



    if cnt_1==cnt_2:
        ans=1
    else:
        ans=0

    print(f"#{test_case} {ans}")