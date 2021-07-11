class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        for i in range(n):
            result *= x
        return result

#Brute force solution for positive values of n only 