def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


arr = [1, 2, 3, 4, 5, 1]
if containsDuplicate(arr):
    print("Array contains duplicate ")
else:
    print("Array dose not contain duplicate ")
