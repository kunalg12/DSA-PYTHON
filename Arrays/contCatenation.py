from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):  # Repeat twice
            for n in nums:  # Loop through each element in nums
                ans.append(n)
        return ans


solution = Solution()
nums = [1, 2, 3]
result = solution.getConcatenation(nums)
print(result)