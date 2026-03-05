class Solution:
    def minOperations(self, s: str) -> int:
        initial_1 = 0
        initial_0 = 0
        n = len(s)

        for i in range(n):
            if i%2 == 0:
                initial_0 += (1 if s[i]=="1" else 0)
                initial_1 += (1 if s[i]=="0" else 0)
            else:
                initial_1 += (1 if s[i]=="1" else 0)
                initial_0 += (1 if s[i]=="0" else 0)
        return min(initial_1,initial_0)




        