class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
                continue
            if i=="-":
                num1,num2=stack.pop(),stack.pop()
                stack.append(num2-num1)
                continue
            if i=="*":
                stack.append(stack.pop()*stack.pop())
                continue
            if i=="/":
                num1,num2=stack.pop(),stack.pop()
                stack.append(int(num2/num1))
                continue
            else:
                stack.append(int(i))
        return stack[0]