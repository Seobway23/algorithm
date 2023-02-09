T = int(input())
lst = []
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst.append([N, S])
    cnt = 0
    
#sort의 key값은 함수밖에 올 수 없다
#인덱스를 활용하고 싶다면 lambda함수를 활용할 것!
lst.sort(key=lambda x:x[0])

for idx in range(len(lst)-1):
    # 비교1=lst[idx][0]
    # 비교2=lst[idx + 1][0]
    # 다리1=lst[idx][1]
    # 다리2=lst[idx + 1][1]
    if lst[idx][0] == lst[idx + 1][0]:
        if lst[idx][1] != lst[idx + 1][1]:
            cnt += 1

        else:
            pass


    else:
        pass

print(cnt)
