class Solution:
    def isValid(self, s: str) -> bool:
        d={"]":"[","}":"{",")":"("}

        a=["[","{","("]

        stack=[]
# ( [ {
        for i in s:
            if i in a:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                if d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
                    
        
        return len(stack)==0
            



        