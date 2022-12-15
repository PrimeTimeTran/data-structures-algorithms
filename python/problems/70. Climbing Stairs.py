# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # Top down brute force
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # Top down + memorization (dictionary)
    def climbStairs(self, n, dic={1: 1, 2: 2}):
        if n not in dic:
            dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return dic[n]

    # Top down + memorization (list)
    def climbStairs(self, n):
        def helper(n, dic):
            if dic[n] < 0:
                dic[n] = helper(n-1, dic)+helper(n-2, dic)
            return dic[n]
        if n <= 2:
            return n

        dic = [-1 for _ in range(n)]
        dic[0], dic[1] = 1, 2

        return helper(n-1, dic)

    # Bottom up, memoization
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 2

        for _ in range(3, n+1):
            tmp = one + two
            one = two
            two = tmp

        return two
