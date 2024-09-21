from typing import List


class Solution:
    def replaceElement(self, arr: List[int]) -> List[int]:
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(maxRight, arr[i])
            arr[i] = maxRight
            maxRight = newMax
        return arr

solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
result = solution.replaceElement(arr)
print(result)