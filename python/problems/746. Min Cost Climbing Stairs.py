class Solution:
    # Top down brute force
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def helper(n):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]
            return cost[n] + min(helper(n-1), helper(n-2))
        return min(helper(n-1), helper(n-2))

    # Top down memoization
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        def helper(n):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]
            if not dp[n] == 0:
                return dp[n]
            dp[n] = cost[n] + min(helper(n-1), helper(n-2))
            return dp[n]
        dp[n] = min(helper(n-1), helper(n-2))
        return dp[n]

    # Bottom up tabulation
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])
