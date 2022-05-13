class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if len(nums) == len(set(nums)) and (len(nums) == 0 or 1):
            return False
        locs = dict()
        for i in range(len(nums)):
            p = nums[i]
            n = locs.get(p, None)
            if n!=None:
                if abs(n-i) <= k:
                    return True
            locs[p] = i
