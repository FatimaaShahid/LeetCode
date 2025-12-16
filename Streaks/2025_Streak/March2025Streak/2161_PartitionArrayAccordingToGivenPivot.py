class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        same = []
        greater = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot :
                lesser.append(num)
            else:
                same.append(num)
        ans=[]
        ans = lesser + same + greater
        return ans

        