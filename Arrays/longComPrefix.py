from typing import List

class Solution:
    def longCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

solution = Solution()
strs = ["flower", "flow", "flight"]
result = solution.longCommonPrefix(strs)
print(result)
