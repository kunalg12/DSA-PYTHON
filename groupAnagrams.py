from collections import defaultdict
from typing import List


class Solution:

    @staticmethod
    def groupAnagram(strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        return list(ans.values())


solution = Solution()
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagram(input_strs)
print(result)
