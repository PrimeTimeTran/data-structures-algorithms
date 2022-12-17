# Word Count Engine
# Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation(even in the middle of a word) and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

# Examples:

# input:  document = "Practice makes perfect. you'll only
# get Perfect by practice. just practice!"

# output: [["practice", "3"], ["perfect", "2"],
#          ["makes", "1"], ["youll", "1"], ["only", "1"],
#          ["get", "1"], ["by", "1"], ["just", "1"]]

from collections import OrderedDict


def word_count_engine(document):
  d = OrderedDict()
  words = document.split()
  max_f = 0
  for i, word in enumerate(words):
    realword = "".join([c.lower() for c in word if c.isalpha()])
    d[realword] = d.get(realword, 0)+1
    max_f = max(max_f, d[realword])

  bucket = [[] for _ in range(max_f+1)]

  for w in d:
    fqc = d[w]
    bucket[fqc].append([w, str(fqc)])

  res = []

  for i in range(len(bucket)-1, -1, -1):
    if bucket[i]:
      res += bucket[i]
  return res


print(word_count_engine(
    "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))
print(word_count_engine(
    "Practice makes perfect. you'll only \
    get Perfect by practice. just practice!") == [["practice", "3"], ["perfect", "2"],
                                                                                                   ["makes", "1"], [
        "youll", "1"], ["only", "1"],
    ["get", "1"], ["by", "1"], ["just", "1"]])
