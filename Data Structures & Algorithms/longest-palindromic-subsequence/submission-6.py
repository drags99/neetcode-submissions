"""
if len(s) then longest is 1
if is len(s)=2 and begining and end are the same, then longest is 2, else is 1
if len(s) = 3, end and begining are either the same or different, begining is same or different, or all 3 are the same.

"""
cache = {}
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def pali(start,end) -> int:
            if f"{start}_{end}" in cache.keys():
                return cache[f"{start}_{end}"]
            sub = s[start:end]
            if len(sub) <= 1:
                return len(sub)
            
            if sub[0] == sub[-1]:
                return 2 + pali(start+1,end-1)
            else:
                # check skipping first works
                f = pali(start+1,end)
                cache[f"{start+1}_{end}"] = f
                # check skipping last
                l = pali(start,end-1)
                cache[f"{start}_{end-1}"] = l
                return max(f,l)
        return pali(0,len(s))


            
        