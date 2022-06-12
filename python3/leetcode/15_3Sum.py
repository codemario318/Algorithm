from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        twoSum = set()
        numCounter = Counter(nums)

        