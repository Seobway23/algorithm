'''
알파벳 대소문자로 된 단어가 주어지면. 이 단어에서 가장 많이 사용된 알파벳이
무엇인지 알아내는 프로그램을 작성하시오.
단 대소문자를 구분하지 않는다. -> 모든 문자 소문자로 만든다.

만약 많이 사용한 알파벳이 중복이라면 '?'를 출력한다.
'''

#1 딕셔너리로 받아서 딕셔너리 value값에 하나씩 추가할 것이다!
ord1=input()
ord2 = ord1.lower()
dic = {}
cnt = 0

for i in ord2:
    if i in dic:
        dic[i] += 1

    else:
        dic[i] = 1

#2 딕셔너리의 mx 밸류 값을 정한 후 변수로 놓는다!
mx = dic[max(dic,key=dic.get)]
mx_a = max(dic,key=dic.get)

#중복인지 확인하는 법
#3 변수 값을 mx로 할당해서 최대 밸류 값을 딕셔너리에서 제거한다
del dic[mx_a]

#4 제거한 후에도 값이 같은게 있다면 중복
for i in dic:
    if dic[i] == mx:
        cnt += 1
        break

if cnt == 0:
    print(mx_a.upper())

else:
    print('?')