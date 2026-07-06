class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        ptr = 0
        end_ptr = N
        while ptr < end_ptr:
            val = nums[ptr]
            
            if val == 0:
                nums.pop(ptr)
                nums.append(val) 
                end_ptr -= 1
                ptr -= 1

            ptr += 1