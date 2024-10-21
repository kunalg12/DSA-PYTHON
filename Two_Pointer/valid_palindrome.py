class Solution:
    def palindrome(self, s: str):
        # skip alapha-numeric characters
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            # move pointer
            left += 1
            right -= 1

        return True


solution = Solution()
s = "A man, a plan, a canal: Panama"
result = solution.palindrome(s)
print(result)
