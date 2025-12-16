class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) < k or not nums:
            return -1
        s = list(set(nums))
        if k in s:
            s.remove(k)
        return len(s)
            

        
        