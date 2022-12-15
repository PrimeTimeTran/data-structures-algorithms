# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent 
# houses have security systems connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the 
# maximum amount of money you can rob tonight without alerting the police.

from functools import lru_cache

class Solution:
    # Top down brute force
    def rob(self, nums: List[int]) -> int:
        def helper(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[1],nums[0])
            return max(nums[i] + helper(i-2), helper(i-1))

        return helper(len(nums)-1)

    # Top down memoization
    def rob(self, nums: List[int]) -> int:
        def helper(i,dp={}):
            if i in dp:
                return dp[i]
            elif i < 0:
                return 0
            elif i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[1],nums[0])
            else:
                dp[i] = max(nums[i] + helper(i-2), helper(i-1))
                return dp[i]
        return helper(len(nums)-1)

    # Top down memoization
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def helper(i):
            if i < 0:
                return 0
            elif i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[1],nums[0])
            else:
                return max(nums[i] + helper(i-2), helper(i-1))

        return helper(len(nums)-1)

    # Bottom up tabulation
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
