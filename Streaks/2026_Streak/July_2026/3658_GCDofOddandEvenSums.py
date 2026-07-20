class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0
        for i in range(1,n*2+1):
            if i%2 == 0:
                even += i
            else:
                odd += i
        ran = min(even,odd)//2
     
        for i in range(ran,0,-1):
            if even%i == 0 and odd%i == 0:
                return i
        return 1
        