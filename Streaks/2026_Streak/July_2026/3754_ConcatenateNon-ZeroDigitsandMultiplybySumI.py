class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n ==0:
            return 0
        n = str(n)
        s = 0
        num = ""
        for i in n:
            if i!="0":
                s+=int(i)
                num += i
        return s*int(num)


        