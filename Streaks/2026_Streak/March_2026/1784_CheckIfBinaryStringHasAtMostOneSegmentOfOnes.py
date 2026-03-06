class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev = -1
        n = len(s)
        for i in range(n):
            print(s[i],i,prev)
            if s[i] == "1" :
                if (prev == -1) or (i-prev == 1):
                    prev = i
                else:
                    return False
            
        return True


        