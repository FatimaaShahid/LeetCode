class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        max_happiness = 0
        happiness.sort(reverse = True)

        for i in range(k):
            max_happiness += max(0,happiness[i]-i)
        return max_happiness

        