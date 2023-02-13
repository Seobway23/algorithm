import sys
sys.stdin=open('input.txt', 'r')
#
# while True: # N=0일 때 break하는 while문 만들기
#     N=int(input())
#     if N==0:
#         break
#     lst=[]
#     while True: #리스트화 시키기
#         if N==0:
#             break
#         lst.append(N%10)
#         N=N//10
#
#     if lst==lst[::-1]:
#         print("yes")
#
#     else:
#         print("no")

# 애초에 n을 스트링으로 보면 더 쉽게 할 수 있음
while True: # N=0일 때 break하는 while문 만들기
    N=input()
    if N=='0':
        break

    if N==N[::-1]:
        print("yes")

    else:
        print("no")
