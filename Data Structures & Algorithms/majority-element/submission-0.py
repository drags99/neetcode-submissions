class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # n can be even or odd
        # can assume the element must exist
        # since it appears more than n / 2, it must be at the middle if sorted
        middle = n // 2
        nums.sort()
        return nums[middle]