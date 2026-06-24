
"""
[0,1,2,3]
len(cost)-1 = 3 
idx=0
msum=0
cost=0
return 0 + min(search(idx+1),search(idx+2))
    idx=1, msum=0,
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # take 1 step or 2

        # if idx == (len(cost)-2), take 2 steps
        # if idx == (len(cost)-1), take 1 step
        msum = 0
        idx = 0
        cost = [0] + cost
        cache = {}
        def key(idx,msum):
            return f"{idx}_{msum}"

        def search(idx,msum,cost):
            if key(idx,msum) in cache.keys():
                return cache[key(idx,msum)]
            else:
                if idx < len(cost):
                    msum += cost[idx]
                if idx >= (len(cost)-1):
                    return msum
                else:
                    min_1 = search(idx+1,msum,cost)
                    cache[key(idx+1,msum)] = min_1
                    min_2 = search(idx+2,msum,cost)
                    cache[key(idx+2,msum)] = min_2
                    return min(min_1,min_2)

        return search(idx,msum,cost)