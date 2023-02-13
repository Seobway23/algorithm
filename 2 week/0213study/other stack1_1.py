import sys
from typing import List
sys.stdin=open("input.txt", "r")



T=int(input())
for test_case in range(1,T+1):
    st=input()
    N=len(st)
    stk=[]
    ans =1

    for ch in st:   #입력 문자열 하나씩 처리
        if ch == "(": #push
            stk.append(ch)
        else:
            if stk: #stk데이터가 있다면
                stk.pop()
            else: # pop해야 하는 상황인데 없다면
                ans = 0
                break

    #모든 처리 완료 후 stk에 데이터가 남았다면, 오류
    if stk:     #')'괄호 부족
        ans = 0
    print(f"#{test_case} {ans}")
