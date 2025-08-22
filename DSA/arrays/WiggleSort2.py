class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        temp = sorted(nums)
        n = len(nums)
        ptr = n - 1

        for i in range(1, n, 2):
            nums[i] = temp[ptr]
            ptr -= 1
        
        for i in range(0, n, 2):
            nums[i] = temp[ptr]
            ptr -= 1

