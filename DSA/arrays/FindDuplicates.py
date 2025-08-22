class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # cyclic sort
        n = len(nums)
        for i in range(n):
            while nums[i] != i+1:
                pos = nums[i]-1
                nums[i], nums[pos] = nums[pos], nums[i]
                if nums[pos]==nums[i]:
                    break

        result = []
        for i in range(n):
            if nums[i]!=i+1:
                result.append(nums[i])

        return result    
