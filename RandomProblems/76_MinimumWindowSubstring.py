
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        characters = [0]*128
        min_len_found = float('inf')
        left = 0
        right = 0
        missing_letters = len(t)
        min_len_left_index = 0

        for char in t:
            characters[ord(char)] += 1
        while right<len(s):
            if characters[ord(s[right])] > 0:
                missing_letters -= 1
            characters[ord(s[right])] -=1
            right += 1

            while missing_letters == 0:
                if right - left < min_len_found:
                    min_len_left_index = left
                    min_len_found = right - left
                
                if characters[ord(s[left])] == 0:
                    missing_letters += 1
                characters[ord(s[left])] += 1
                left += 1

        return "" if min_len_found == float('inf') else s[min_len_left_index:min_len_left_index + min_len_found]
