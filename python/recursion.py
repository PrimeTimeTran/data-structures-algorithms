# Given a string `str` of lowercase alphabetical characters, return the set
# of all permutations of those characters in upper AND lowercase.


# function permutations(str) {
#     const res = []
#     function helper(s, i) {
#         if (i >= str.length) {
#             res.push(s)
#             return
#         }
#         // HERE IS VALUE, CONSUME
#         const lower = str.charAt(i).toLowerCase()
#         const upper = str.charAt(i).toUpperCase()
#         helper(s + lower, i + 1)
#         helper(s + upper, i + 1)

#         // PROCESS CHILDREN, WHICH RETURN AGGREGATE VALUES, THEN PROCESS THEM
#         // const lower = str.charAt(i).toLowerCase()
#         // const upper = str.charAt(i).toUpperCase()
#         // var charleft = helper(lower, i+1)
#         // var charight = helper(upper, i+1)
#     }
#     helper('', 0)
#     return res
# }
