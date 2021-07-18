"""
@author: pradheep
"""


"dynamic programming"
def fib(n):
    ls=[0,1]
    for i in range(2,n+1):
        ls.append(ls[i-1]+ls[i-2])
    return ls[n]
print(fib(50))


"""Normal programig  method"""

"""
recursion is working in a tree like structure

"""

def fib1(m):
    if m<=2:
        return 1
    return fib1(m-1)+fib1(m-2)
print(fib1(3))

""" Another dynamic programming method  """

def fib1(m,memo={}):
    if m in memo:
        return memo[m]
    elif m<=2:
        return 1
    memo[m]=fib1(m-1,memo)+fib1(m-2,memo)
    return memo[m]
print(fib1(3))
