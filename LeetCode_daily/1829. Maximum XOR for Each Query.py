def getMaximumXor(nums, maximumBit):
    n = len(nums)
    cumulativeXor = 0

    # Calculate cumulative XOR for all elements
    for num in nums:
        cumulativeXor ^= num

    # Prepare the answer array
    answer = [0] * n
    mask = (1 << maximumBit) - 1  # Mask with maximumBit bits set to 1

    # Iterate over nums in reverse order
    for i in range(n):
        answer[i] = cumulativeXor ^ mask  # Calculate k
        cumulativeXor ^= nums[n - 1 - i]  # Remove last element for next query

    return answer


# Example usage
nums = [0, 1, 1, 3]
maximumBit = 2
print(getMaximumXor(nums, maximumBit))  # Output: [0, 3, 2, 3]