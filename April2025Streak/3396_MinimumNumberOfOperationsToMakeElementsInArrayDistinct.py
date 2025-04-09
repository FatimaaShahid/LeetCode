class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        operations = 0
        while nums:
            if len(set(nums)) == len(nums)  :
                return operations 
            if len(nums) < 3 :
                return operations + 1
            nums = nums[3:]
            operations += 1
        return operations
        
            
        