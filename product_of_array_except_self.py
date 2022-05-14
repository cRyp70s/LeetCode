import array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = array.array('i', [1]*n) if n > 10 else [1]*n
        for i in range(1, n):
            prev = nums[i-1]*res[i-1]
            res[i] *= prev
        prev = 1
        for i in range(n-2, -1, -1):
            prev = nums[i+1]*prev
            res[i] *= prev
        return res
