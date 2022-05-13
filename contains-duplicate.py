class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        arr = dict()
        for i in range(len(nums)):
            k = nums[i]
            if arr.get(k, 0) == 0:
                arr[k] = 1
            else:
                return True
        return False
