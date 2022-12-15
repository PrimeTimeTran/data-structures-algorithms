class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
          for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
              res[i][j] = 1 + res[i+1][j+1]
            else:
              res[i][j] = max(res[i+1][j], res[i][j+1])

        return res[0][0]
