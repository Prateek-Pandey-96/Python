class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if k == 1:
            return 0
        min_diff = nums[k-1]-nums[0]

        for i in range(k, n):
            min_diff = min(min_diff, nums[i]-nums[i-k+1])
        
        return min_diff

