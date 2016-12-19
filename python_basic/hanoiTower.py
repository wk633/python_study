#-*- coding:utf-8 -*-

def hanoi(n, a, b, c):
    # a,b,c 分别表示起始盘，缓存盘和目标盘
    if n == 1:
        print a,'-->', c
        return
    hanoi(n-1, a, c, b) # 将起始柱子上的n-1个盘子移动到缓存盘里
    hanoi(1, a, b, c) # 将起始柱子上最后一个盘子移动到目标盘里
    hanoi(n-1, b, a, c) # 将缓存盘里的n-1个盘子移动到目标盘里

hanoi(3,'A','B','C')
