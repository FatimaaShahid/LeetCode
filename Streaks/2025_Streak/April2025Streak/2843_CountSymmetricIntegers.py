class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1 ):
            s = str(i)
            if len(s)%2 == 0:
                split = len(s)//2
                left = list(s[:split])
                right = list(s[split:])
                for j in range(len(left)):
                    left[j] = int(left[j])
                for j in range(len(right)):
                    right[j] = int(right[j])
                if sum(left) == sum(right):
                    count += 1
        return count
                

        