class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n =  len(questions)
        dp = [0]*(n+1)
        for i in range(n - 1, -1, -1):
            points,brainpower = questions[i]

            next_index = brainpower + i + 1

            solve = points + (dp[next_index] if n>next_index else 0)

            skip = dp[i+1]

            dp[i] = max(solve,skip)
        
        return dp[0]
        