class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # cyclic sort
        n = len(nums)
        for i in range(n):
            pos = nums[i]-1
            while nums[i] != i+1 and nums[pos]!=nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos = nums[i]-1

        result = []
        for i in range(n):
            if nums[i]!=i+1:
                result.append(nums[i])

        return result    
