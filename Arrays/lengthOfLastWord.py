class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # one line shortcut
        # return len(s.split()[-1])

        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c


# Example usage
solution = Solution()
s = 'Gursal Kunal'
print(solution.lengthOfLastWord(s))  # Output: 5
