class Solution:
    def minPartitions(self, n: str) -> int:
        num = 0
        for char in n:
            i = int(char)
            if i>num:
                num = i
        return num 
        