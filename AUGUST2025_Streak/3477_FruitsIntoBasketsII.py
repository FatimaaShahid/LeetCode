class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = 0
        for amount in fruits:
            for i in range(len(baskets)):
                if baskets[i]>=amount:
                    placed += 1
                    baskets[i] = 0
                    break
        return len(fruits)-placed

        