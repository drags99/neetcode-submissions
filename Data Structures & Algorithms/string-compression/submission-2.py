"""
looks like run length encoding

pop the first char from chars

use recursion to check how many of the next char is the same, returning a int for the count
ie:
f(chars=["a,a,b,a"], target="a")
    count = 0
    for c in chars, if c == target, count += 1
    return count

if it returns 0, just append the char to s and go to next

when char is empty, return the len of s
edges: empty set, but chars >= 1,
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        
        len_s = 0

        if n == 1:
            return n

        
        while len(chars) != len_s:
            temp_ptr = 0
            target = chars[0]

            while (chars[temp_ptr] == target) and (temp_ptr < (len(chars)-len_s)):
                temp_ptr += 1
                if temp_ptr == len(chars):
                    break
            temp = [str(target)]

            if temp_ptr > 1:
                temp += list(f"{temp_ptr}")
            
            len_s += len(temp)
            chars += temp
            # append then pop
            for _ in range(temp_ptr):
                chars.pop(0)

        return len(chars)
        