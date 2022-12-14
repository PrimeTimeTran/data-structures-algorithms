class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob2(nums[1:]), self.rob2(nums[:-1]))

    def rob2(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for n in nums:
            tmp = max(n+r1, r2)
            r1 = r2
            r2 = tmp

        return r2
