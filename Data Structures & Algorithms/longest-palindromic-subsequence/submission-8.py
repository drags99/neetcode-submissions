"""
if len(s) then longest is 1
if is len(s)=2 and begining and end are the same, then longest is 2, else is 1
if len(s) = 3, end and begining are either the same or different, begining is same or different, or all 3 are the same.

"""
cache = {}
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)+1
        cache = [[-1] * n for _ in range(n)]
        longest = ""

        def pali(start,end) -> int:

            if cache[start][end] != -1:
                return cache[start][end] 

            sub = s[start:end]

            if len(sub) <= 1:
                return len(sub)
            
            if sub[0] == sub[-1]:
                return 2 + pali(start+1,end-1)
            else:
                # check skipping first works
                f = pali(start+1,end)
                cache[start+1][end] = f
                # check skipping last
                l = pali(start,end-1)
                cache[start][end-1] = l
                return max(f,l)
        
        for i in range(len(s)):
            pali(0,i)

        return pali(0,len(s))


            
        