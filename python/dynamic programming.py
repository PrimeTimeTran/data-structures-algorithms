import time

n = 40


def timeit(func):
    start = time.time()
    print(func(n))
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


def climbStairs(n):
    # Top down - TLE
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)


timeit(climbStairs)


def climbStairs(n):
    # Bottom up, O(n) space
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]


timeit(climbStairs)


def climbStairs(n):
    # Bottom up, constant space
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b


timeit(climbStairs)


def helper(n, dic):
    if dic[n] < 0:
        dic[n] = helper(n-1, dic)+helper(n-2, dic)
    return dic[n]


def climbStairs(n):
    # Top down + memoization (list)
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return helper(n-1, dic)


timeit(climbStairs)

def climbStairs(n, dic={1: 1, 2: 2}):
    # Top down + memoization (dictionary)
    if n not in dic:
        dic[n] = climbStairs(n-1) + climbStairs(n-2)
    return dic[n]


timeit(climbStairs)
