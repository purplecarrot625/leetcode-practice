class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #对tokens进行遍历，如果是数字就压到栈里，如果是操作符，弹出栈里的两个数字进行运算
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]