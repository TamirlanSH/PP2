class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n:
            rem = n % 10
            n = n // 10 
            p *= rem 
            s += rem
        return p - s
    print(subtractProductAndSum(1, int(input())))