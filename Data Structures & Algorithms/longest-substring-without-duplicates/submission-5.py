class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr_1 = 0
        ptr_2 = 0
        str_seq = []
        longest = 0
        while ptr_1 <= (len(s)):
            for idx in range(ptr_1,len(s)+1):
                # print(f"idx:{idx} ptr{ptr_1}")
                temp_seq = s[ptr_1:idx]
                # print(temp_seq)

                # see if temp_seq is valid
                if len(temp_seq) == len(set(temp_seq)):
                    if len(temp_seq) > longest:
                        longest = len(temp_seq)
                        # print(longest)
            ptr_1 += 1
        
        return longest