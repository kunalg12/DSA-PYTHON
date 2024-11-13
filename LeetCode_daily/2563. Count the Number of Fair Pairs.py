from bisect import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        n = len(nums)
        count = 0

        for i in range(n - 1):
            low_val = lower - nums[i]
            up_val = upper - nums[i]

            start = bisect.bisect_left(nums, low_val, i + 1)
            end = bisect.bisect_right(nums, up_val, i + 1) - 1

            if start <= end:
                count += end - start + 1

        return count