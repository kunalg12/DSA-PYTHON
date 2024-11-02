class Solution:
    @staticmethod
    def pattern():
        ch = "A"

        for i in range(4, 0, -1):
            for _ in range(i):
                print(ch, end=" ")
                ch = chr(ord(ch) + 1)
            print()


solution = Solution()
solution.pattern()