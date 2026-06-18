"""
trivial when n=1 or n=2

could simplify if im already up x stairs and only have 1 left
* to get to 4 steps, need to first take 3 then take 1 more
* to get to 5 steps, need to first take 4 then take 1 more
to start can take 1 step or 2 steps
    if take 1 step, have 2 steps remaining
    if take 2 steps, have 1 step remaining
    can sum numbers of ways 
f(3) = f(1) + f(2)
f(3) = #combinations to get to 2 + #combinations to take 1
f(4) = #combinations to get to 3 + #combinations to take 1
Example:
f(3)->3
f(2)->2
f(1)->1
    n = 4
    f(4) = 5
    f(3) = 3
    if
        f(1) = 1
        f(2) = f(1) + 1
    else
            f(n) = f(n-1) + f(n-2)

f(3) = f(2) + f(1)
f(4) = f(3) + f(2)
f(5) = f(4) + f(3)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1,2:2}
        def f(n:int) -> int:
            # base case for n 1 or 2
            if n in cache.keys():
                return cache[n]
            else:
                f_1 = f(n-1)
                f_2 = f(n-2)
                cache[n-1] = f_1
                cache[n-2] = f_2
                simplified = f_1 + f_2
                return simplified
        return f(n)