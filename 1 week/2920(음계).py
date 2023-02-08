#2920 음계
N=list(map(int,input().split()))
#N=[8,7,6,5,4,3,2,1]
ascending=0
descending=0
mixed=0

for i in range(len(N)-1):
    if N[i+1]==N[i]+1:
        ascending+=1

        if ascending==7:
            print('ascending')

    if N[i+1]+1==N[i]:
        descending+=1
        if descending==7:
            print('descending')


if ascending!=7 or descending!=7:
    pass

else:
    print('mixed')
