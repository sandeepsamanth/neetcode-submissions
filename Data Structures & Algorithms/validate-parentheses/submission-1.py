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
                print(stack,"-=")
                if len(stack)>0: 
                    if i in d and d[i]==stack[len(stack)-1]:
                        stack.pop()
                else:
                    return False
        
        return len(stack)==0
            



        