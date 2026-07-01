class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        dp = [0,0]
        dual_dp = {}

        # pass starting index, and takes
        # 1 and 2 steps backwards
        def search(start,end)->int:
            key = f"{start}_{end}"
            if key in dual_dp.keys():
                return dual_dp[key]
            if end < 0:
                return 0
            if start == end:
                return 0
            if len(nums[start:end]) <= 0:
                return 0
            # take 2 steps back or 3 and search
            step_2 = search(start,end-2) + nums[start:end][-1]
            step_3 = search(start,end-3) + nums[start:end][-1]
            s_max = max(step_2,step_3)
            dual_dp[key] = s_max
            return s_max

        for i in range(len(nums)):

            without_self = search(0,i)
            with_self = search(1,i+1)
            temp = max(dp[-1],with_self,without_self)

            dp.append(temp)



        return max(dp)

        