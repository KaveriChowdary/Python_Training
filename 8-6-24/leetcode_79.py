def dfs(self,board,word,visited,i,j,ch):
    def backtrack(i,j,k):
        if k==len(word):
            return True
        if i < 0 or i>len(board) or j<0 or j>len(board) or board[i][j]!=word[k]:
            return False
        temp=board[i][j]
        board[i][j] =' '
        if backtrack(i+1,j,k+1) or backtrack(i-1,j,k+1) or backtrack(i,j-1,k+1) or backtrack(i,j+1,k+1):
            return True
        board[i][j]=temp
        return False
    for i in range(le(board)):
        for j in range(len(board[0])):
            if backtrack(i,j,0):
                return True
    return False