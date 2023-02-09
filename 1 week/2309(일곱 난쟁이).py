'''
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 
일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 
뛰어난 수학적 직관력을 가지고 있던 백설공주는, 
다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 
백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
'''

T=9
lst=[]
cnt=0
for test_case in range(T):
    N=int(input())
    lst.append(N)


for i in range(T-1):
    for j in range(i+1,T):
        if cnt==1:
            break
        lst_s = copy.deepcopy(lst)
        lst_s.remove(lst[i])
        lst_s.remove(lst[j])
        if sum(lst_s) == 100:
            cnt=1
    if cnt==1:
        break


lst_s.sort()
for i in lst_s:
    print(i)

print(lst_s)

# 런타임 에러 났음 ㅜㅜ