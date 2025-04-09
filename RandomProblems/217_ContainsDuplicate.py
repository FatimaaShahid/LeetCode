from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for dig,f in count.items():
            if f>1 :
                return True
        return False
        
        