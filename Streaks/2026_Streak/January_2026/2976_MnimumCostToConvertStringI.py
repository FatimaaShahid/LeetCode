from math import inf
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        dist = [[inf]*26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = 0
        for s, t in zip(source, target):
            if s != t:
                d = dist[ord(s)-97][ord(t)-97]
                if d == inf:
                    return -1
                ans += d

        return ans
