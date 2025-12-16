class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n > 0:
            k = n-1
            j = 1
            while "0" in str(k) or "0"  in str(j):
                j+=1
                k-=1

            return [j,k]
        


        