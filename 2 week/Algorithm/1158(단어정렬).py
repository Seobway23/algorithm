import sys
sys.stdin=open("input.txt", "r")


#길이가 짧은 것 부터
T=int(input())
dic={}
for test_case in range(1,T+1):
    st=input()
    dic[st]=len(st)



set(dic)
s=list(dic.keys())
s.sort() #sort는 문자열도 정렬해줌 1번은 그냥 sort
s.sort(key=len) # 2번은 key=len sort
#사전순으로 어떻게 할지 모름

for i in s:
    print(i)