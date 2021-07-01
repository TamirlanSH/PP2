from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            res[i]=res[i-1]+gain[i-1]
    
        return max(res)
    n = int(input())
    list = []
    for i in range(0,n):
        a = int(input())
        list.append(a)
    print(largestAltitude(1, list))