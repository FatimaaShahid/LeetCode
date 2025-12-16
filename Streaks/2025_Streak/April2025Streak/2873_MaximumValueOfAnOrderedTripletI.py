class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, value)
                    
        return max_value
