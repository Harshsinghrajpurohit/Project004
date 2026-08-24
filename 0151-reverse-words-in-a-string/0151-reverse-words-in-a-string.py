class Solution:
    def reverseWords(self, s: str) -> str:

        i = len(s) - 1
        res = []

        while i >= 0:

            # Skip spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            # Mark the end of the word
            end = i

            # Move left through every letter
            # until we reach a space
            while i >= 0 and s[i] != ' ':
                i -= 1

            # Extract the complete word
            res.append(s[i + 1:end + 1])

        # Join words with exactly one space
        return " ".join(res)