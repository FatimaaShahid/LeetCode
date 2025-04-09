
class Solution:
    def sortArray(self, num ) :
        def merge_sort(num1,num2):
            n = len(num1)
            m = len(num2)

            if n == 0:
                return num2
            
            if m == 0:
                return num1
            num = []
            i = 0
            j = 0

            while i<n or j<m :
                if i == n :
                    num.extend(num2[j:])
                    return num
                if j == m :
                    num.extend(num1[i:])
                    return num
                if num1[i] < num2[j]:
                    num.append(num1[i])
                    i += 1
                else:
                    num.append(num2[j])
                    j+=1
                
        def merge(nums) :
            m = len(nums)
            if m<=1:
                return nums
            n = m//2

            num1 = merge(nums[0:n])
            num2 = merge(nums[n:])

            num = merge_sort(num1,num2)

            return num
        return merge(nums)



