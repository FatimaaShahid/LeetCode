class Solution:
    def mirrorDistance(self, n: int) -> int:
        num = int(str(n)[::-1]) 
        return abs(n-num)