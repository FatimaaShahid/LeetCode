class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effect = [0] * (n + 1)
        
        for start, end, d in shifts:
            if d == 1:
                shift_effect[start] += 1
                shift_effect[end + 1] -= 1
            else:
                shift_effect[start] -= 1
                shift_effect[end + 1] += 1
        
        
        for i in range(1, n):
            shift_effect[i] += shift_effect[i - 1]
        
        
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + shift_effect[i]) % 26
            result.append(chr(ord('a') + shift))
        
        return ''.join(result)
