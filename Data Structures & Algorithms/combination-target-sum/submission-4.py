class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        remaining = target

        nums.sort()

        def bt(path, remaining, idx):

            if idx >= len(nums):
                return

            # successful path
            if remaining == 0:
                results.append(path[:])
                return

            val = nums[idx]
            if val > remaining:
                return

            # see if remaining is zero and add path
            path.append(val)
            bt(path, remaining - val, idx)
            path.pop()

            # see if path with next idx can set remaining to zero
            bt(path, remaining, idx + 1)

        bt(path, remaining, 0)

        return results
