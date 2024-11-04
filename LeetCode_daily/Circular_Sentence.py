class Solution:

    def Circular_Sentence(self, sentence: str) -> bool:
        # split the sentence into words
        words = sentence.split()
        # Number of word in sentence
        n = len(words)

        # Check the circular conditions
        for i in range(n):
            # last char of first word
            first_char = words[i][-1]
            # next char of current word 
            next_char = words[(i + 1) % n][0]

            # comparing both char if they don't match it's not circular
            if first_char != next_char:
                return False
        return True


solution = Solution()
sentence = "leetcode exercises sound delightful"
res = solution.Circular_Sentence(sentence)
print(res)
