import sys
from typing import List
sys.stdin=open("input.txt", "r")

dct={'{':'}','(':')'}
T=int(input())
for test_case in range(1,T+1):
    st=input()
    stk=[]
    ans=1
    #대상 괄호문자를 제외한 나머지는 아무 동작 X
    for ch in st:
        #열리는 괄호인 경우: 닫히는 괄호를 push
        if ch in dct: #dct의 key값 중애 있는 경우
            stk.append(dct[ch]) #나중에 비교할 때 간단하게
        elif ch in dct.values():
            if not stk or ch != stk.pop():
                ans=0
                break
            # if stk:
            #     if ch == stk.pop():
            #         pass
            #     else:
            #         ans=0
            #         break
            # else:
            #     ans=0
            #     break
        # else:
        #     pass

    if stk: #모든 처리 후 스택에 데이터가 있다면,
        ans=0

    print(f"#{test_case} {ans}")





# T=int(input())
# for test_case in range(1,T+1):
#     st=input()
#     stk=[]
#     ans =1
#     cnt=0
#     for ch in st:
#         if ch == '(' or ch == '{' or ch=='[':
#             cnt+=1
#
#     if cnt==0:
#         ans=0
#         print(f"#{test_case} {ans}")
#         continue
#
#
#     for ch in st:   #입력 문자열 하나씩 처리
#         if ch == '(' or ch == '{' or ch=='[': #push
#             stk.append(ch)
#
#         else:
#             if stk: #stk데이터가 있다면
#                 if stk[-1]=="(" and ch==")":
#                     stk.pop()
#
#                 elif stk[-1] == "{" and ch == "}":
#                     stk.pop()
#
#                 elif stk[-1] == "[" and ch == "]":
#                     stk.pop()
#
#             elif len(stk)==0 and ch==")":
#                 ans=0
#             elif len(stk)==0 and ch=="}":
#                 ans=0
#             elif len(stk)==0 and ch==']':
#                 ans=0
#
#
#     #모든 처리 완료 후 stk에 데이터가 남았다면, 오류
#     if stk:     #')'괄호 부족
#         ans = 0
#
#     print(f"#{test_case} {ans}")
