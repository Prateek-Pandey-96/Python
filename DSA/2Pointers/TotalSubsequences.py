class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, total = len(nums), 0
        low, high = 0, n-1
        mod = 1000000007
        while low<high:
            sum = nums[low]+nums[high]
            if sum > target:
                high -= 1
            else:
                total = (total + pow(2, high-low)-1)%mod
                low += 1
        
        for num in nums:
            if 2*num <= target:
                total = (total + 1)%mod
        return total
