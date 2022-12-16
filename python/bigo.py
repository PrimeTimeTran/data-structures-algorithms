# Find The Duplicates
# Given two sorted arrays arr1 and arr2 of passport numbers, implement
# findDuplicates that returns an array of all passport numbers
# in both arr1 and arr2.
# Note that the output array should be sorted in an ascending order.

# Let N and M be the lengths of arr1 and arr2, respectively.
# Solve for two cases and analyze the
# time & space complexities of your solutions:
# M ≈ N - the array lengths are approximately the same.
# M ≫ N - arr2 is much bigger than arr1.

from bisect import bisect_left


def bsearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def find_duplicates(arr1, arr2):
    # o(n^2) where n is the length of the longer of the two lists
    # result = []
    # for n in arr1:
    #   if n in arr2:
    #     result.append(n)
    # return result

    # o(nlog(m)) where n is the length of arr1 and m is the length of arr2, the longer list
    result = []
    for n in arr1:
      index = bsearch(arr2, n)
      if not index == -1:
        result.append(n)

    return result

    # O(n) where n is the length of the shorter of the two lists.
    # result = []
    # i = j = 0
    # while i < len(arr1) and j < len(arr2):
    #   if arr1[i] == arr2[j]:
    #     result.append(arr1[i])
    #     i += 1
    #     j += 1
    #   elif arr1[i] > arr2[j]:
    #     j += 1
    #   else:
    #     i += 1
    # return result


print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))  # [3, 6, 7]
print(find_duplicates([10, 20, 30, 40, 50, 60, 70],
      [10, 20, 30, 40, 50, 60, 70]))  # [10, 20, 30, 40, 50, 60, 70]
