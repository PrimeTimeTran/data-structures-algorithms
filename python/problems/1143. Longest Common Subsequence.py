# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the
# relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down brute force
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1+lcs(i+1, j+1)
            return max(lcs(i, j+1), lcs(i+1, j))
        return lcs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down recursive memoization
        def lcs(i, j, dp={}):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1+lcs(i+1, j+1)
                return dp[(i, j)]
            dp[(i, j)] = max(lcs(i, j+1), lcs(i+1, j))
            return dp[(i, j)]

        return lcs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up tabulation
        res = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    res[i][j] = 1 + res[i+1][j+1]
                else:
                    res[i][j] = max(res[i+1][j], res[i][j+1])
        return res[0][0]
