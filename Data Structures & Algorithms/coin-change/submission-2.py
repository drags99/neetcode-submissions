class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0        
        
        if amount in coins:
            return 1

        coins.sort()
        coins.reverse()
        cache = {}
        cache[0] = 0 

        for i in range(1,amount+1):
            cache[i] = float("inf")
            for c in coins:
                # store coins that match the index
                if i == c:
                    cache[i] = 1
                    continue
                if c < i:
                    cache[i] = min(cache[i-c] + 1, cache[i])
        if cache[amount] != float("inf"):
            return cache[amount]
        return -1

        
