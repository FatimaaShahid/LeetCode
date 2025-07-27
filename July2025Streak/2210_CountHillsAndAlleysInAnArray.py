class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        found = 0
        if len(nums)<3:
            return found
        seen_valley = set()
        seen_hill = set()

        for i in range(1,len(nums)-1):
            curr = nums[i]
            left = None
            right = None
            for a in range(i-1,-1,-1):
                if nums[a]!=curr:
                    left = nums[a]
                    l = a
                    break
            for a in range(i+1,len(nums)):
                if nums[a]!=curr:
                    right = nums[a]
                    r = a
                    break
            if right and left:
                if curr<left and curr<right and (l,r) not in seen_valley:
                    seen_valley.add((l,r))
                    found += 1
                if curr>left and curr>right and (l,r) not in seen_hill:
                    seen_hill.add((l,r))
                    found += 1
        return found





        