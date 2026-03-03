class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        def invert(st):
            new = ""
            for char in st:
                if char == "0":
                    new += "1"
                else:
                    new+= "0"
            return new
        while len(s)<k:
            s = s + "1" + invert(s[::-1])
        return s[k-1]
        