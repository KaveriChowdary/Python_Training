class Solution:
    def calPoints(self, operations):
        resstack=[]
        for i in operations:
            if i not i.isnumeric():
                match i:
                    case ' D':resstack.append(2*restack[-1])
                    case '+': restack.append(resstack[-1]+restack[-2])
                    case 'C': resstack.pop()
            else:
                resstack.append(int(i))
        return sum(resstack)
operations =list(input().split())