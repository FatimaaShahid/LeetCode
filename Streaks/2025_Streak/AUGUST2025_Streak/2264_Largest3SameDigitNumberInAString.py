
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = 0
        ans = ""

        for i in range(len(num)-2):
            if num[i:i+3] == num[i]*3 and int(num[i])>=max_num:
                max_num = int(num[i])
                ans = num[i]*3
        return ans




        