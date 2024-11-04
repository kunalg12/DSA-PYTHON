# Python Solution
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        index = 0
        size = len(word)

        while index < size:
            char = word[index]
            count = 0
            while index < size and word[index] == char and count < 9:
                count += 1
                index += 1
            comp += str(count) + char

        return comp