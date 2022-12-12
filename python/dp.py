# Top down - TLE
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)


print(climbStairs(10))

# Bottom up, O(n) space


def climbStairs(n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]


print(climbStairs(10))

# Bottom up, constant space


def climbStairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b


print(climbStairs(10))
# Top down + memoization (list)


def helper(n, dic):
    if dic[n] < 0:
        dic[n] = helper(n-1, dic)+helper(n-2, dic)
    return dic[n]

def climbStairs(n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return helper(n-1, dic)


print(climbStairs(10))




# Top down + memoization (dictionary)


def climbStairs(n, dic={1: 1, 2: 2}):
    if n not in dic:
        dic[n] = climbStairs(n-1) + climbStairs(n-2)
    return dic[n]


print(climbStairs(10))
