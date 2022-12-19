# Word Count Engine
# Implement a text scanning function wordCountEngine, which receives a string text and returns a list of all unique words in
# it and their number of occurrences, sorted by the number of occurrences in a descending order.
# If two or more words have the same count, they should be sorted according to their order in the original sentence.
# Assume that all letters are in english alphabet.
# You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation(even in the middle of a word) and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

# Examples:

# input: "Practice makes perfect. you'll only get Perfect by practice. just practice!"

# output: [["practice", "3"], ["perfect", "2"],
#          ["makes", "1"], ["youll", "1"], ["only", "1"],
#          ["get", "1"], ["by", "1"], ["just", "1"]]


'''
Create state variables for dict, words, maxF.

Loop over words cleaning word, incrementing dic, and updating maxF

Create list of lists using maxF 

Add words frequency to appropriate buckets.

Iterate backwards through bucket and concatenate lists into one list

return list
'''


from collections import OrderedDict


def word_count_engine(text):
    d = OrderedDict()
    words = text.split()
    maxFrequency = 0
    for i, word in enumerate(words):
        word = "".join([c.lower() for c in word if c.isalpha()])
        d[word] = d.get(word, 0)+1
        maxFrequency = max(maxFrequency, d[word])

    bucket = [[] for _ in range(maxFrequency+1)]

    for w in d:
        fqc = d[w]
        bucket[fqc].append([w, str(fqc)])

    res = []

    for i in range(len(bucket)-1, -1, -1):
        if bucket[i]:
            res += bucket[i]
    return res


print(word_count_engine("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!") == [
      ["just", "4"], ["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["get", "1"], ["by", "1"]])
print(word_count_engine("To be, or not to be, that is the question:") == [["to", "2"], ["be", "2"], [
      "or", "1"], ["not", "1"], ["that", "1"], ["is", "1"], ["the", "1"], ["question", "1"]])
print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!") == [
      ["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"]])
