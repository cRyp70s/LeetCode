class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        n = len(nums)  
        idx = sorted(range(len(nums)), key=lambda k: nums[k])
        nums_sorted = [nums[i] for i in idx]
        
        for i in range(n):
            for j in range(i,-1,-1):
                if i==j:
                    continue
                if abs(nums_sorted[i] - nums_sorted[j]) > t:
                    break
                if abs(idx[i] - idx[j]) <= k:
                    return True
            
            for j in range(i, n):
                if i==j:
                    continue
                if abs(nums_sorted[i] - nums_sorted[j]) > t:
                    break
                if abs(idx[i] - idx[j]) <= k:
                    return True
                    
            
                
