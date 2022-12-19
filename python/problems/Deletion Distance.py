from collections import Counter, OrderedDict


def deletion_distance(str1, str2):
  if str1 == str2:
    return 0

  m, n = len(str1), len(str2)
  dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  # Update first row
  for i in range(m + 1):
    dp[i][0] = i

  # Update first col
  for j in range(n + 1):
    dp[0][j] = j

  # Update the rest of the matrix
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i - 1] != str2[j - 1]:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
      else:
        dp[i][j] = dp[i - 1][j - 1]

  return dp[-1][-1]


print(deletion_distance('dog', 'frog'))
print(deletion_distance('some', 'some'))
print(deletion_distance('some', 'thing'))
print(deletion_distance('', ''))
print(deletion_distance('ab', 'ba'))


def helper1(s1, s2):
  c1 = Counter(s1)
  c2 = Counter(s2)

  res = 0
  for key, val in c1.items():
    if not c1[key] == c2[key]:
      res += 1

  for key, val in c2.items():
    if not c1[key] == c2[key]:
      res += 1

  return res


def deletion_distance(s1, s2):
  if s1 == s2:
    return 0
  if len(s1) == 0 or len(s2) == 0:
    return abs(len(s1) - len(s2))

  if helper1(s1, s2) > 0:
    return helper1(s1, s2)

  res = 0

  def helper(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
      return 0

    if s1 == s2:
      return res

    return 1 + min(helper(s1[1:], s2), helper(s1, s2[1:]))

  return helper(s1, s2)
