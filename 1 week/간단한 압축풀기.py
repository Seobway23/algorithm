import sys
from pprint import pprint
sys.stdin=open("0210input.txt","r")

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst=[]
    for _ in range(N):
        string, number=input().split()
        num=int(number)
        for i in range(num):
            lst.append(string)


    print(f"#{test_case}")
    i=0
    B=''
    while i<len(lst)//10+1:
        B = ''
        try:
            for j in range(10):
                B+=lst[i*10+j]


        except IndexError:
            print(B)
            break


        print(B)


        i+=1



    # for _ in range(len(lst)//10+1+1): #10으로 나눈 수의 +1 만큼 pop하겠다
    #
    #     for i in range(10):
    #         #j=lst.pop(i)
    #         print( end='')
    #
    # lst.pop()





    print(lst)

