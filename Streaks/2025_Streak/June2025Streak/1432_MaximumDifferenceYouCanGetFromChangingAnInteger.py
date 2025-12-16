class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        for ch in num_str:
            if ch != '9':
                a = int(num_str.replace(ch, '9'))
                break
        else:
            a = num 
        b_candidates = []

        if num_str[0] != '1':
            return a - int(num_str.replace(num_str[0],"1"))
        b = num

        for d in set(num_str[1:]):
            if d != '0' and num_str[0]!=d:
                b = min(b,int(num_str.replace(d, '0')))

        return a - b
