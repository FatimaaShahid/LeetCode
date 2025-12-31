class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()
        self.dfs(s, 0, [], 0, 0)
        return list(self.res)

    def dfs(self, string, idx, cur_res, open_cnt, close_cnt):
  
        if len(cur_res) + (len(string) - idx) < self.longest_string:
            return

        if idx == len(string):
            if open_cnt == close_cnt:
                curr = "".join(cur_res)
                if len(curr) > self.longest_string:
                    self.longest_string = len(curr)
                    self.res = {curr}
                elif len(curr) == self.longest_string:
                    self.res.add(curr)
            return

        ch = string[idx]

        if ch == '(':

            cur_res.append(ch)
            self.dfs(string, idx + 1, cur_res, open_cnt + 1, close_cnt)
            cur_res.pop()

            self.dfs(string, idx + 1, cur_res, open_cnt, close_cnt)

        elif ch == ')':
         
            self.dfs(string, idx + 1, cur_res, open_cnt, close_cnt)

          
            if open_cnt > close_cnt:
                cur_res.append(ch)
                self.dfs(string, idx + 1, cur_res, open_cnt, close_cnt + 1)
                cur_res.pop()

        else:
           
            cur_res.append(ch)
            self.dfs(string, idx + 1, cur_res, open_cnt, close_cnt)
            cur_res.pop()
