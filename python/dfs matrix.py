
# Matrix

def dfs(r, c):
    print('Process')
    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)
