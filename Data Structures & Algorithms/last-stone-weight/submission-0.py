class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        def smash(x,y)->int:
            if x < y:
                return y - x
            else:
                return 0

        while len(stones) > 1:
            stones.sort()
            print(stones)
            x = stones.pop(-2)
            y = stones.pop(-1)
            smashed = smash(x,y)
            stones.append(smashed)
            

        return stones[0]

        