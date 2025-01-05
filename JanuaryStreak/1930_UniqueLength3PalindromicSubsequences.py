class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        
        for char in set(s):
            
            first = s.find(char)
            last = s.rfind(char)
            
            if first < last:  
                
                unique_middle = set(s[first + 1:last])
                result += len(unique_middle)
        
        
        return result
