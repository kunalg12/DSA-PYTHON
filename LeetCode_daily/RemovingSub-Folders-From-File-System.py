from typing import List


class Solution:
    @staticmethod
    def removeSubfolders(folder: List[str]) -> List[str]:
        folder.sort()
        result = []

        for path in folder:
            if not result or not path.startswith(result[-1] + '/'):
                result.append(path)

        return result


# Test cases
def test_remove_subfolders():
    solution = Solution()

    # Test case 1
    folders1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    print("Input 1:", folders1)
    print("Output 1:", solution.removeSubfolders(folders1))  # Expected: ["/a","/c/d","/c/f"]

    # Test case 2
    folders2 = ["/a", "/a/b/c", "/a/b/d"]
    print("\nInput 2:", folders2)
    print("Output 2:", solution.removeSubfolders(folders2))  # Expected: ["/a"]


if __name__ == "__main__":
    test_remove_subfolders()