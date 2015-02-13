# coding: UTF-8

import math

def chk_prim(x):
    prim = [2,3,5,7,11,13,17,19,23,29]#3以上まで書いておく
    for i in prim
        if x==i:
            return True
        if (x%i) == 0:
            return False

    for i in range((prim[-1]+2),int(math.sqrt(x))+1,2):
        if (x%i) == 0:
            return False
    return True

a=int(raw_input())
sum = (a+1)*a/2
if chk_prim(a):
    print 'WANWAN'#素数
else:
    print 'BOWWOW'

# coding: UTF-8

num=int(raw_input())

x=[]
curl = []



for i in range(0,num):
    curl.append(map(int, raw_input().split()))
    if curl[i][0] == 1:
        x.append(curl[i][1])
    elif curl[i][0] == 2:
        x.sort()
        print(x.pop(curl[i][1]-1))

