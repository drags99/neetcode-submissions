# brute force wont work well b/c of the combinations
# can try one path and back track if it doesnt work
# resembles a graph structure, starting with 0 and trying to add
# up to the target
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        remaining = target

        nums.sort()

        def bt(path,remaining,idx):
            if idx >= len(nums):
                return

            # successful path
            if remaining == 0:
                # if path in results:
                #     return
                results.append(path[:])
                return

            val = nums[idx]
            if val > remaining:
                return

            path.append(val)
            # print(path)
            bt(path,remaining - val,idx)

            # bt(path,remaining - val,idx+1)
            path.pop()

            bt(path,remaining,idx+1)



        bt(path,remaining,0)

        return results