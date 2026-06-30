"""

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        dp = []

        # base
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))

        for i in range(2,len(nums)):
            val = nums[i] + max(dp[:-1])
            dp.append(val)
        print(dp)
        return max(dp[-1],dp[-2])