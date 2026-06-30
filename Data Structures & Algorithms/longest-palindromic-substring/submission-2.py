class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        dp = []
        dp.append(1)

        longest = ""

        # if string only has 2 characters, it just need to see if it reads
        # the same forward and back
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
                right = s[-1 - c] # first its the last character then its the second to last character
                if c == (-1 - c):
                    return is_pali
                if left == right:
                    continue
                else:
                    return False
            return is_pali
        
        for i in range(2,len(s)):
            last_longest_pali = dp[-1]

            sub = s[i-1-last_longest_pali:i+1]
            sub2 = s[i-last_longest_pali:i+1]

            temp = dp[-1]
            # check if sub is pali
            if check(sub):
                dp.append(len(sub))
                if len(sub) > len(longest):
                    longest = sub
                    if len(sub) > temp:
                        temp = len(sub)

            if check(sub2):
                if len(sub2) > len(longest):
                    dp.append(len(sub2))
                    longest = sub2
                    if len(sub2) > temp:
                        temp = len(sub2)

            dp.append(temp)

        return longest


