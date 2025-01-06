class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            moves = 0
            for j in range(i+1,len(boxes)):
                if boxes[j] =="1":
                    moves += j-i
            for j in range(0,i):
                if boxes[j] == "1":
                    moves += (i-j)
            ans[i] = moves
        return ans

        