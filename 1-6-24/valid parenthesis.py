class Solution:
    def isValid(self, s: str) -> bool:
        stack = list(s)
        valid_check = []
        if len(s)%2!=0:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                valid_check.append(i)
            elif i == ")" and valid_check and valid_check[-1] == "(":
                valid_check.pop()
            elif i == "]" and valid_check and valid_check[-1] == "[":
                valid_check.pop()
            elif i == "}" and valid_check and valid_check[-1] == "{":
                valid_check.pop()
            else:
                return False
        
        if len(valid_check)==0:
            return True
        else:
            return False