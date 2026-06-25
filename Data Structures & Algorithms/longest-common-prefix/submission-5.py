class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # max size is the len of the smallest str in strs
        # just need to keep checking if it's in all of the strings
        # if it's not pop the last
        
        # edge case when strs only has 1 entry
        if len(strs) == 1:
            return strs[0]
        
        # find smallest string, since it sets upperbound
        min_str = strs[0]
        min_len = len(min_str)

        for i in strs:
            i_l = len(i)
            if i_l < min_len:
                min_str = i
                min_len = i_l
        
        strs.remove(min_str)
        for i in range(min_len+1):
            sub_string = min_str[:(min_len-i)]
            
            sub_string_in_all_strs = True
            for j in strs:
                if sub_string in j:
                    continue
                else:
                    sub_string_in_all_strs = False
                    break
            if sub_string_in_all_strs:
                return sub_string