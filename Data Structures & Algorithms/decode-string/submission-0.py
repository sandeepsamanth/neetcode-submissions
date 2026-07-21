class Solution:
    def decodeString(self, s: str) -> str:

        #  2 [ a 3 [ b 
        stack=[]
        for i in s:
            if i !="]":
                stack.append(i)
            else:
                substr=""
                while stack and  stack[-1]!="[":
                    substr=stack.pop()+substr

                stack.pop()

                numb=""
                while stack and stack[-1].isdigit():
                    numb=stack.pop()+numb

                stack.append(substr*int(numb))
        return "".join(stack)

        