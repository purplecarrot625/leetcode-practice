class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # store pair:(temperature, index)
        stack = []
    
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i-stackIndex
            stack.append([t,i])
        return res
    
    # stack[-1][0]:我们要栈顶元素，and temperature是每个[temp, index]的第一个元素,所以是0