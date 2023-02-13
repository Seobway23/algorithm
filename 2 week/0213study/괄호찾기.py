import sys
sys.stdin = open('input.txt')

dct={'{':'}','(':')'}
T = int(input())
for test_case in range(1, T+1):
    st=input()
    stk=[]
    ans=1
    #대상 괄호 문자를 제외한 나머지는 아무 동작하지 않음
    for ch in st:
        #열리는 괄호인 경우 닫히는 괄호를 push
        if ch in dct:           #dct의 key값 중에 있는 경우
            stk.append(dct[ch]) #나중에 비교할 때 간단히 하기 위해 value값 넣는다

        elif ch in dct.values():
            if not stk or ch!=stk.pop():
                ans=0
                break
        if stk:  #stk가 있다면
            ans=0

        print(f'#{test_case} {ans}')
