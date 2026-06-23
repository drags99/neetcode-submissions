import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        cache = {}
        initial_set = []

        def make_key(nums):
            key = "_"
            for i in nums:
                key = key + f"_{i}"
            return key

        
        def in_cache(nums,cache)->bool:
            key = make_key(nums)
            if key in cache.keys():
                return True
            return False

        def re_sub(nums):
            
            key = make_key(nums)
            print(f"re_sub called from {key}")

            # base case
            if len(nums) == 0:
                return

            # add self if not in cache
            if not (key in cache.keys()):
                cache[key] = nums
                initial_set.append(nums[:])
            

            # recursion on subsets
            for i in range(len(nums)):
                temp_nums = nums[:i] + nums[i+1:]
                temp_key = make_key(temp_nums)
                
                if temp_key in cache.keys():
                    continue
                else:
                    # print(f"not in cache: {temp_key}")
                    cache[temp_key] = temp_nums
                    initial_set.append(temp_nums)
                    re_sub(temp_nums)
                    

        re_sub(nums)
        return initial_set