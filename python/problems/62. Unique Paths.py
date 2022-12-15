# There is a robot on an m x n grid. The robot is initially located at the top-left corner(i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner(i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    # Top down brute force
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m,n):
            if m < 0 or n < 0:
                return 0
            if m == 1 and n == 1:
                return 1

            return helper(m-1,n) + helper(m,n-1)
        return helper(m,n)

    # Top Down recursive memoization
    def uniquePaths(self, m: int, n: int, dic={}) -> int:
        def helper(m,n):
            if (m,n) in dic:
                return dic[(m,n)]
            if m < 0 or n < 0:
                return 0
            if m == 1 and n == 1:
                return 1

            dic[(m,n)] =  helper(m-1,n) + helper(m,n-1)
            return dic[(m,n)]

        return helper(m,n)

    # Bottom up tabulation
    def uniquePaths(self, m: int, n: int, dic={}) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(m+1):
            for j in range(n+1):
                cur = dp[i][j]
                if i + 1 <= m:
                    dp[i+1][j] += cur
                if j + 1 <= n:
                    dp[i][j+1] += cur
        return dp[m][n]
