class Solution:
    def isSubSequence(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


solution = Solution()
s = "ace"
t = "ahcge"
result = solution.isSubSequence(s, t)