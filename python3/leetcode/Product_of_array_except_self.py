class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.arrayMul(nums)
        
        if self.zeroCount == 0:
            return [self.total // num for num in nums]
        
        res = [0 for _ in nums]
        
        if self.zeroCount == 1:
            res[self.zeroIdx] = self.total
        
        return res
            
        
    def arrayMul(self, nums: List[int]) -> int:
        self.total = 1
        self.zeroCount = 0
        self.zeroIdx = None
        
        for i, num in enumerate(nums):
            if num == 0:
                self.zeroCount += 1
                self.zeroIdx = i
                if self.zeroCount > 1:
                    return
            else:
                self.total *= num