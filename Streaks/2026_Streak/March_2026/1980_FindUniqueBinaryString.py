class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        for i in range(2**n):
            req = bin(i)[2:]
            req = "0"*(n-len(req)) + req
            if req not in nums:
                return req
        return -1
        