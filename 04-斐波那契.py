
# todo 递归    时间复杂度：o(2^n)   空间复杂度o(n)
def fib_01(n):
    if n<3:
        return 1
    return fib_01(n-2)+fib_01(n-1)

print(fib_01(8))

# todo numpy    时间复杂度：o(n)  但是会占用很多内存空间
import numpy as np
def fib_02(n):
    tmp = np.zeros(n)
    tmp[0] = 1
    tmp[1] = 1
    for i in range(2,n):
        tmp[i] = tmp[i-2] + tmp[i-1]
    return int(tmp[n-1])

print(fib_02(8))

# todo 不占用内存空间的方法
def fib_03(n):
    a,b = 1,1
    c = 0
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    return int(c)

print(fib_03(8))

# todo 斐波那契时间复杂度为o(1)  使用通项式实现
import math
def fib_04(n):
    num = math.sqrt(5)
    x1 = (1+num)/2
    x2 = (1-num)/2
    res = num/5*(math.pow(x1,n)-math.pow(x2,n))
    return int(res)

print(fib_04(8))