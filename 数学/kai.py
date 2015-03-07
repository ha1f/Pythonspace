# coding: UTF-8

import sys
sys.setrecursionlimit(10005)

def kai(n):
	if n==1: return 1
	return n*kai(n-1)

num = 10000
print(str(num) + "!=")
print(kai(num))