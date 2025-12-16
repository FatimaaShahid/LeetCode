class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if nums[0] % 2 == 0:
            flag = 1
        else:
            flag = 0
        for i in range(1,len(nums)):
            if nums[i] % 2 == 0:
                flag += 1
            else:
                flag -= 1
            if flag > 1 or flag < 0:
                return False
        return True


            

        