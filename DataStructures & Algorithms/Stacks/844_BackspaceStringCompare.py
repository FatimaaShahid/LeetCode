class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char == "#":
                if s_stack :
                    s_stack.pop(-1)
            else:
                s_stack.append(char)
        
        for char in t:
            if char == "#":
                if t_stack :
                    t_stack.pop(-1)
            else:
                t_stack.append(char)
        
        return s_stack == t_stack
        