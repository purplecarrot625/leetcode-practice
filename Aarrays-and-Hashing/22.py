class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack
        # result
        # 只有左括号数小于n的时候添加左括号
        # 只有右括号数小于左括号数的时候添加右括号
        # 当左右括号相等且等于n时，有效
        
        stack = []
        result = []
        
        def backtrack(leftN, rightN):
            # base case
            if leftN == rightN == n:
                result.append("".join(stack))
                return 

            if leftN < n:
                stack.append("(")
                backtrack(leftN+1, rightN)
                # stack是全局的，我们没有传入到每个里面，所以当backtrack return之后要把栈里刚加的元素pop出来
                stack.pop()
            
            if rightN < leftN:
                stack.append(")")
                backtrack(leftN, rightN+1)
                stack.pop()
            
        backtrack(0,0)
        return result