from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            curr = nums[i:i + k]  
            freq = Counter(curr)  

            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            s = 0
            for i, (key, value) in enumerate(sorted_items):
                if i == x:  
                    break  
                s += key*value

            ans.append(s) 

        return ans
