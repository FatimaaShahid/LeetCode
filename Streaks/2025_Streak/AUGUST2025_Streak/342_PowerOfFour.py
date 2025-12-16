class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>4:
            n/=4
        return n==4 or n==1 
        