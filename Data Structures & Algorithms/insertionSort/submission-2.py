# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        # if len(pairs) == 0:
        #     return states
        # states += [pairs.copy()]
        for i in range(len(pairs)):
            # states += [pairs.copy()]
            j = i - 1
            ikey = pairs[i].key
            while(j>=0 and pairs[j].key>ikey):
                # states += [pairs.copy()]
                tmp = pairs[j]
                pairs[j] = pairs[i]
                pairs[i] = tmp
                i=j 
                j-=1
            states += [pairs.copy()]

        return states
        