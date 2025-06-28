
def convert(s, numRows) :
    if numRows == 1 or numRows >= len(s):
        return s
    ans = ['' for _ in range(numRows)]
    i = 0     
    down = True 

    for char in s:
        ans[i] += char
        if i == 0:
            down = True
        elif i == numRows - 1:
            down = False
        i += 1 if down else -1
    return ''.join(ans)
