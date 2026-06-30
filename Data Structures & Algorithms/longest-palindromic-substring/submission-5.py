class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        dp = []
        dp.append(1)

        longest = ""

        if s[0] == s[1]:
            dp.append(2)
            longest = s[0:2]
        else:
            dp.append(1)
            longest = s[1]

        def check(s):
            is_pali = True
            for c in range(len(s)):
                left = s[c]
                right = s[-1 - c]
                if c == (-1 - c):
                    return is_pali
                if left == right:
                    continue
                else:
                    return False
            return is_pali
        
        for i in range(2,len(s)):
            last_longest_pali = dp[-1]
            sub2 = s[i-1-last_longest_pali:i+1]
            sub1 = s[i-last_longest_pali:i+1]
            temp = dp[-1]
            sub = ""
            if check(sub1):
                sub = sub1
            elif check(sub2):
                sub = sub2
            else:
                dp.append(dp[-1])
                continue                

            if len(sub) > len(longest):
                longest = sub
                if len(sub) > temp:
                    temp = len(sub)
                    dp.append(temp)
                    continue

        return longest


