from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k) - 1):
                    res[i] += code[j % N]

        return res


solution = Solution()
code = [5, 7, 1, 4]
k = 3
res = solution.decrypt(code, k)
print(res)