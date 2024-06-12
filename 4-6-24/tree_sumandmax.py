#binary tree
def totalsum(self,root):
    if root is None:
        return 0
    else:
        leftsum=totalsum(root.left)
        rightsum=totalsum(root.right)
        return root.data+leftsum+rightsum
    
def treemax(self,root):
    if root is None:
        return 0
    else:
        leftmax=treemax(root.left)
        rightmax=treemax(root.right)
    return max(root.data,leftmax,rightmax)

def treeheight(self,root):
    if root is None:
        return 0
    else:
        leftheight = treeheight(root.left)
        rightheight = treeheight(root.right)
        return 1+max(leftheight,rightheight)
#item present in tree or not
def existintree(self,root):
    if root is None:
        return False
    else:
        inleft = existintree(root.left,value)
        inright = existintree(root.right,value)
        return root.data == value or inleft or inright
#reversing the tree
def treereverse(self,root):
    if root is None:
        return False
    else:
        treereverse(root.left)
        treereverse(root.right)
        root.left , root.right = root.right,root.left
