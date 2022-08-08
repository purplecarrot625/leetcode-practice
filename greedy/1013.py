class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arraySum = sum(arr) # 数组的和
        
        if arraySum % 3 != 0: # 如果不能被3整除，直接返回不能
            return False
        
        partialSum = arraySum // 3
        part = 3 # 记录是哪一部分
        tempSum = 0 # 记录当前的一部分已经累积到多少了
        
        for i in arr:
            if tempSum + i == partialSum: # 如果该部分加到了每一部分应该有的值
                # 是否到下一个part/是否为最后一个part
                if part > 0:
                    part -= 1
                    tempSum = 0
                else:
                    tempSum += i
            else:
                tempSum += i
                
        # 如果三个部分算完了and没有剩余的了    
        if part == 0 and tempSum == 0:
            return True
        else:
            return False