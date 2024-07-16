
from typing import List


class Solution:
    def longestSubarray(self, n : int, arr : List[int]) -> int:
        # code here
        a =[0]
        max_len = 0
        
        for x in range(n):
            val = 0
            l = arr[x]
            for y in range(x+1,n):
                r = arr[y]
                if l^r == val:
                    if abs(y-x+1) > max_len:
                        max_len = y-x+1
                    
                val = val^y
        return max_len

a = Solution()
print(a.longestSubarray(5,[4 ,2, 5 ,7 ,9]))