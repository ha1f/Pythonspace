# -*- coding: utf-8 -*-
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:#2から√nまで探索
        while n % i == 0:#その数で割れるだけ割る
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
