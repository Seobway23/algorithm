import sys
sys.stdin=open("input.txt","r")
T=int(input())
for test_case in range(1,T+1):
    sd = input()
    st=list(sd)
    stk = []
    for ch in st:
        if not stk:
            stk.append(ch)

        else:
            if ch==stk[-1]:
                stk.pop()
            else:
                stk.append(ch)

    print(f"#{test_case} {len(stk)}")