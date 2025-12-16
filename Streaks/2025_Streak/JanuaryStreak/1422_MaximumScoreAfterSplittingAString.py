class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero_count = [0] * (n + 1)
        for i in range(n):
            zero_count[i + 1] = zero_count[i] + (1 if s[i] == '0' else 0)
        
        one_count = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            one_count[i] = one_count[i + 1] + (1 if s[i] == '1' else 0)
        
        max_score = 0
        for i in range(1, n):
            max_score = max(max_score, zero_count[i] + one_count[i])
        
        return max_score
