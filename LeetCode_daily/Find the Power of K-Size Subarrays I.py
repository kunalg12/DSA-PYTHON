class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        # Helper function to check if a subarray is sorted and contains consecutive integers
        def is_consecutive_and_sorted(subarray):
            # Check if each element in the subarray is exactly one less than the next element
            return all(subarray[i] + 1 == subarray[i + 1] for i in range(len(subarray) - 1))

        # Get the length of the input array
        n = len(nums)
        # Initialize an empty list to store the results for each K-size subarray
        result = []

        # Iterate over all possible starting indices for K-size subarrays
        for i in range(n - k + 1):
            # Extract the current K-size subarray from nums
            subarray = nums[i:i + k]
            # Check if the current subarray is consecutive and sorted
            if is_consecutive_and_sorted(subarray):
                # If true, append the maximum value of the subarray to results
                result.append(max(subarray))
            else:
                # If false, append -1 to indicate it does not meet the criteria
                result.append(-1)

        # Return the final list of results
        return result


# Example usage:
# Create an instance of the Solution class
solution = Solution()
# Define an array and a value for k
nums = [1, 2, 3, 4, 5]
k = 3
# Call the resultsArray method and print the output
print(solution.resultsArray(nums, k))  # Output: [3, 4, 5]