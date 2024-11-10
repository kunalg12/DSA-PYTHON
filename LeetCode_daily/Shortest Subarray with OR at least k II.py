class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32  # Count of bits set in the current window
        ans = n + 1  # Initialize answer as larger than any possible length
        s = i = 0  # Initialize sum and left pointer

        for j, x in enumerate(nums):
            s |= x  # Update the OR value of the current window
            for h in range(32):
                if x >> h & 1:
                    cnt[h] += 1  # Count bits set in x

            while s >= k and i <= j:  # Check if current window meets the condition
                ans = min(ans, j - i + 1)  # Update minimum length found
                y = nums[i]
                for h in range(32):
                    if y >> h & 1:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h  # Remove this bit from the OR
                i += 1  # Move left pointer to shrink the window

        return -1 if ans > n else ans  # Return result or -1 if no valid subarray found
