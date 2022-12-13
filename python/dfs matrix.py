
# Matrix

def dfs(r, c):
    print('Process')
    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)


class Solution:
  def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]: res = []
    res = []

    def dfs(n):
          if not n:
              return -1
          height = max(dfs(n.left), dfs(n.right))+1
          if height >= len(res):
              res.append([])
          res[height].append(n.val)
          return height
      dfs(root)
      return res
