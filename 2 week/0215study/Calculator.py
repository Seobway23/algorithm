import sys
sys.stdin=open('input.txt','r')

def calculator(a, b, k):
    if k=='+':
        return a + b
    if k == '-':
        return a - b
    if k == '*':
        return a * b
    if b!=0 and k=='/':
        return int(a/b)
    else:
        return 'error'

def stk_opr(str1):
    # stack and list 만들기
    stk=[];
    number=[];
    dic_opr={'+':1}

    for i in str1:
        if i in list(dic_opr.keys()): #0 i가 연산자라면
            if stk: #1stk이 있다면
                while stk and dic_opr[stk[-1]] >= dic_opr[i]: #2 token값이 작거나 같으면
                    B=stk.pop()                     # top의 stk 꺼내기
                    number.append(B)                # 꺼낸 것 number에 저장
                #while이 끝났으면 추가
                stk.append(i)

            else:   #1 stk가 없다면 연산자 stk에 저장
                stk.append(i)
        else:       #0 i가 숫자라면
            number.append(int(i))

    while True: #위 stk과 number를 분리하는 작업이 다 끝난 후에도 stk가 남아있다면 꺼내준다.
        if stk:
            number.append(stk.pop())
        else:   #
            if stk:
                S=stk.pop()
                number.append(S)

            else: #함수의 return값은 number로 한다.
                return number

def stk_sum(alst): # sum 하다가 말았음
    num_list = alst.append('.')

    for i in alst:
        if i == '.':
            a





T=1
for test_case in range(1,T+1):
    N=int(input())
    str1=input()
    #후위 표기식의 stack number list 만들기

    alst=stk_opr(str1)
    #stk_sum(str1)

    print(f"#{test_case} {stk_opr(str1)}")