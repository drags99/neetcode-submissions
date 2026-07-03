class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0        
        
        if amount in coins:
            return 1

        coins.sort()
        coins.reverse()
        cache = {}

        
        
        # upper limit of coins needed 
        #since amount < 10000, and smallest coin is 1 
        cache[amount] = 100000
        # when amount is 0
        cache[0] = 0 

        for i in range(1,amount+1):
            # build up array of min coins
            # needed by trying each coin
            # and looking back
            cache[i] = float("inf")
            for c in coins:
                # store coins that match the index
                diff = i - c
                if diff == 0:
                    cache[i] = 1
                    continue
                if c < i:
                    cache[i] = min(cache[i-c] + 1, cache[i])
        if cache[amount] != float("inf"):
            return cache[amount]
        return -1

        
