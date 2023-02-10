# import sys
from pprint import pprint
# sys.stdin=open("0210input.txt", "")

T=1
#T=int(input())
#arr=["..#..",".#.#.",f"#.{STR}.#",".#.#.","..#.."]
for test_case in range(1,T+1):
    STR='DFSDDDDD'
    N=len(STR)
    arr = ["..#..", ".#.#.", f"#.{STR[0]}.#", ".#.#.", "..#.."]
    if len(STR)>=2:
        for i in range(1,len(STR)):
            add_a=[".#..","#.#.",f".{STR[i]}.#","#.#.",".#.."]
            for j in range(len(arr)):
                arr[j]+=add_a[j]

    for i in range(len(arr)):
        print(arr[i])