class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        ans = []
        b_n = (bin(n)[::-1])[0:-2]
        for i,char in enumerate(b_n):
            num = (2**i)*int(char)
            if num != 0:
                powers.append(num)
        powers.sort()
        for left,right in queries:
            curr = 1 
            for j in range(left,right+1):
                curr*=powers[j] if powers[j] else 1
            ans.append(curr%(10**9 + 7))
        return ans
            

        

        