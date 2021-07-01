from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = 0
        d = {}
        for i in nums:
            if i in d:
                s += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return s
    n = int(input())
    list = []
    for i in range(0,n):
        a = int(input())
        list.append(a)
    print(numIdenticalPairs(1, list))