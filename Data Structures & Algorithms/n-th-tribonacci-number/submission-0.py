class Solution:
    def tribonacci(self, n: int) -> int:
        T_n = [0,1,1]
        if n <= 2:
            return T_n[n]
        temp_n = len(T_n)
        # for some T_n just add up the last 3
        for i in range(temp_n,n+1):
            next_n = sum(T_n)
            T_n.pop(0)
            T_n.append(next_n)
        
        return T_n[-1]