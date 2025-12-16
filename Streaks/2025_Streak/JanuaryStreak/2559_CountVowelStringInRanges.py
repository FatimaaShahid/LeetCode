class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        ans = []
        n = len(words)
        prefix = [0]*(n+1)

        for i in range(len(words)) :
            if words[i][0] in vowels and words[i][-1] in vowels :
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]

        for l,r in queries :
            ans.append(prefix[r+1] - prefix[l])
        return ans




            


        