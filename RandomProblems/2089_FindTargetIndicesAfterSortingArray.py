class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)

        for i in range(m-1) :
            min_pos = i
            for j in range(i+1,m) :
                if nums[min_pos] > nums[j] :
                    min_pos = j
            if min_pos != i :
                nums[i] , nums[min_pos] = nums[min_pos] , nums[i]
        ans= []
        for i in range(len(nums)):
            if nums[i] == target :
                ans.append(i)
        return ans