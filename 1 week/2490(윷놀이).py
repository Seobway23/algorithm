'''
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 
나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 
네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 
도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 
중 어떤 것인지를 결정하는 프로그램을 작성하라.

input
0 1 0 1
1 1 1 0
0 0 1 1


output
B
A
B


'''

T=3
for test_case in range(3):
    lst=list(map(int,input().split()))
    cnt=0
    
    for i in lst:
        if i==0:
            cnt+=1
        else:
            pass
        
    dic={0:'E',1:'A',2:'B',3:'C',4:'D'}
    print(dic[cnt])
    #딕셔너리를 추가하면 더 간편하게 코드를 짤 수 있음


    #if문을 쓸 때 이렇게 써야 함
    #     if cnt==0:
    #     print('E')
        
    # if cnt==1:
    #     print('A')
        
        
    # if cnt==2:
    #     print('B')
        
    # if cnt==3:
    #     print('C')
        
    # if cnt==4:
    #     print('D')